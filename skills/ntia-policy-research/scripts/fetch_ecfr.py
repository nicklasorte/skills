#!/usr/bin/env python3
"""Fetch a CFR part or section from the eCFR API with an "as of" date.

Writes three outputs to the output directory:

  <stem>.md            Readable text, one heading per section, with the
                       authority, source, and amendment history.
  <stem>.json          The same content as structured data, for the skill.
  sections/<n>.md      One file per section, so long parts can be read in
                       chunks instead of pasted whole.

Examples:

  python3 fetch_ecfr.py --title 47 --part 302 --out runs/part-302
  python3 fetch_ecfr.py --title 47 --section 300.1 --date 2023-03-06 --out runs/300-1
  python3 fetch_ecfr.py --title 47 --section 300.1 --compare 2022-01-19 --out runs/300-1

The eCFR is authoritative but unofficial. For a legal citation, confirm
against the official annual CFR on govinfo.gov.
"""

import argparse
import difflib
import gzip
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

API = "https://www.ecfr.gov/api/versioner/v1"
WEB = "https://www.ecfr.gov"
USER_AGENT = "ntia-policy-research/1.0 (eCFR fetch script)"


def get(url, retries=5):
    """Return the response body for url, retrying transient failures."""
    # The eCFR full-text endpoint refuses uncompressed responses (406).
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept-Encoding": "gzip"})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                body = resp.read()
                if resp.headers.get("Content-Encoding", "").lower() == "gzip":
                    body = gzip.decompress(body)
                return body
        except urllib.error.HTTPError as err:
            # eCFR intermittently answers 403 under rate limiting; back off.
            if err.code in (403, 429, 500, 502, 503, 504) and attempt < retries - 1:
                time.sleep(5 * (attempt + 1))
                continue
            if err.code == 404:
                raise SystemExit(f"Not found in eCFR (the part or section may not exist on that date): {url}")
            hint = " eCFR may be rate limiting; wait a minute and rerun." if err.code in (403, 429) else ""
            raise SystemExit(f"eCFR request failed ({err.code}): {url}.{hint}")
        except urllib.error.URLError as err:
            if attempt < retries - 1:
                time.sleep(2 * (attempt + 1))
                continue
            raise SystemExit(f"Can't reach eCFR ({err.reason}): {url}")
    return b""


def title_status(title):
    """Return the eCFR status record for a title (dates and reserved flag)."""
    data = json.loads(get(f"{API}/titles.json"))
    for rec in data["titles"]:
        if rec["number"] == title:
            return rec
    raise SystemExit(f"Title {title} not found in eCFR.")


def scope_params(args):
    return {"section": args.section} if args.section else {"part": args.part}


def fetch_xml(title, date, params):
    query = urllib.parse.urlencode(params)
    return get(f"{API}/full/{date}/title-{title}.xml?{query}")


def fetch_versions(title, params):
    """Return amendment records for the scope, newest first."""
    query = urllib.parse.urlencode(params)
    data = json.loads(get(f"{API}/versions/title-{title}.json?{query}"))
    versions = data.get("content_versions", [])
    return sorted(versions, key=lambda v: v.get("date", ""), reverse=True)


def clean(text):
    return re.sub(r"\s+", " ", text or "").strip()


def text_of(el):
    return clean("".join(el.itertext()))


def parse_sections(xml_bytes):
    """Return part metadata and a list of section dicts from eCFR XML."""
    root = ET.fromstring(xml_bytes)
    part = {"heading": "", "authority": "", "source": ""}
    part_div = root if root.get("TYPE") == "PART" else root.find(".//DIV5[@TYPE='PART']")
    if part_div is not None:
        head = part_div.find("HEAD")
        part["heading"] = text_of(head) if head is not None else ""
        auth = part_div.find("AUTH")
        src = part_div.find("SOURCE")
        part["authority"] = clean(re.sub(r"^Authority:", "", text_of(auth))) if auth is not None else ""
        part["source"] = clean(re.sub(r"^Source:", "", text_of(src))) if src is not None else ""

    sections = []
    for div in root.iter("DIV8"):
        if div.get("TYPE") != "SECTION":
            continue
        number = div.get("N", "")
        head = div.find("HEAD")
        heading = text_of(head) if head is not None else ""
        paragraphs = []
        citation = ""
        for child in div:
            tag = child.tag
            if tag == "HEAD":
                continue
            if tag == "CITA":
                citation = text_of(child).strip("[]")
                continue
            body = text_of(child)
            if body:
                paragraphs.append(body)
        reserved = "[Reserved]" in heading or (not paragraphs and "Reserved" in heading)
        sections.append({
            "section": number,
            "heading": heading,
            "paragraphs": paragraphs,
            "source_note": citation,
            "reserved": reserved,
        })
    return part, sections


def section_url(title, number, date=None):
    base = f"{WEB}/on/{date}" if date else f"{WEB}/current"
    return f"{base}/title-{title}/section-{number}"


def history_by_section(versions):
    hist = {}
    for v in versions:
        hist.setdefault(v.get("identifier", ""), []).append({
            "date": v.get("date"),
            "amendment_date": v.get("amendment_date"),
            "issue_date": v.get("issue_date"),
            "type": v.get("type"),
            "removed": v.get("removed", False),
            "substantive": v.get("substantive"),
        })
    return hist


def render_section_md(title, sec, date, history):
    lines = [f"## § {sec['section']} {clean(re.sub(r'^§+\s*[\d.]+', '', sec['heading']))}", ""]
    lines.append(f"Source text: {section_url(title, sec['section'], date)}")
    lines.append("")
    for p in sec["paragraphs"]:
        lines.append(p)
        lines.append("")
    if sec["source_note"]:
        lines.append(f"*Source note:* {sec['source_note']}")
        lines.append("")
    if history:
        dates = ", ".join(sorted({h["date"] for h in history if h.get("date")}))
        lines.append(f"*eCFR version dates:* {dates}")
        lines.append("")
    return "\n".join(lines)


def compare(title, params, date_a, date_b, out_dir, stem):
    """Write a unified diff of the scope's text between two dates."""
    def flat(date):
        _, secs = parse_sections(fetch_xml(title, date, params))
        out = []
        for s in secs:
            out.append(f"§ {s['section']} {s['heading']}")
            out.extend(s["paragraphs"])
            out.append("")
        return out

    a, b = flat(date_a), flat(date_b)
    diff = difflib.unified_diff(a, b, fromfile=f"as of {date_a}", tofile=f"as of {date_b}", lineterm="")
    path = out_dir / f"{stem}-diff-{date_a}-to-{date_b}.txt"
    path.write_text("\n".join(diff) + "\n", encoding="utf-8")
    return path


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--title", type=int, required=True, help="CFR title number, such as 47")
    scope = ap.add_mutually_exclusive_group(required=True)
    scope.add_argument("--part", help="Part number, such as 302")
    scope.add_argument("--section", help="Section number, such as 300.1")
    ap.add_argument("--date", help="Point-in-time date (YYYY-MM-DD). Default: the title's up-to-date-as-of date.")
    ap.add_argument("--compare", metavar="DATE", help="Also diff the text as of DATE against --date.")
    ap.add_argument("--out", required=True, help="Output directory")
    args = ap.parse_args()

    status = title_status(args.title)
    date = args.date or status["up_to_date_as_of"]
    params = scope_params(args)
    stem = f"{args.title}cfr-" + (f"part-{args.part}" if args.part else f"section-{args.section}")

    out_dir = Path(args.out)
    (out_dir / "sections").mkdir(parents=True, exist_ok=True)

    part, sections = parse_sections(fetch_xml(args.title, date, params))
    if not sections:
        raise SystemExit(f"No sections found for {params} as of {date}.")
    history = history_by_section(fetch_versions(args.title, params))

    label = f"Part {args.part}" if args.part else f"§ {args.section}"
    scope_url = (f"{WEB}/on/{date}/title-{args.title}/part-{args.part}" if args.part
                 else section_url(args.title, args.section, date))

    header = [
        f"# {args.title} CFR {label}" + (f": {clean(re.sub(r'^PART\s+\d+\s*[—-]*', '', part['heading']))}" if part["heading"] else ""),
        "",
        f"- As of: {date} (eCFR point-in-time)",
        f"- Title {args.title} last amended: {status.get('latest_amended_on')}",
        f"- Fetched from: {scope_url}",
        f"- Sections: {len(sections)}",
    ]
    if part["authority"]:
        header.append(f"- Authority: {part['authority']}")
    if part["source"]:
        header.append(f"- Source: {part['source']}")
    header += ["", "The eCFR is authoritative but unofficial. Confirm legal citations against the official annual CFR on govinfo.gov.", ""]

    body = []
    for sec in sections:
        md = render_section_md(args.title, sec, date, history.get(sec["section"], []))
        body.append(md)
        safe = sec["section"].replace("/", "_")
        (out_dir / "sections" / f"{safe}.md").write_text(md + "\n", encoding="utf-8")

    (out_dir / f"{stem}.md").write_text("\n".join(header + body), encoding="utf-8")

    record = {
        "title": args.title,
        "scope": params,
        "as_of": date,
        "title_latest_amended_on": status.get("latest_amended_on"),
        "source_url": scope_url,
        "part": part,
        "sections": [dict(s, url=section_url(args.title, s["section"], date),
                          history=history.get(s["section"], [])) for s in sections],
    }
    (out_dir / f"{stem}.json").write_text(json.dumps(record, indent=2), encoding="utf-8")

    print(f"{label} as of {date}: {len(sections)} sections -> {out_dir / (stem + '.md')}")
    if args.compare:
        path = compare(args.title, params, args.compare, date, out_dir, stem)
        print(f"Diff {args.compare} -> {date}: {path}")


if __name__ == "__main__":
    sys.exit(main())
