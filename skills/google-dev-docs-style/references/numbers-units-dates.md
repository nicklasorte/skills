# Numbers, units, dates, and times

Paraphrased from the Google developer documentation style guide (CC BY 4.0): Numbers, Units of measurement, Dates and times.

## Words or numerals

**Spell out**
- Zero through nine in ordinary counts ("four options," "nine developers").
- A number that starts a sentence ("Fifteen directories are created"), or rewrite so the number isn't first. A four-digit year may start a sentence, though it's not ideal.
- A number directly followed by a numeral ("fifteen 100,000-byte files").
- Approximate or casual quantities ("thousands of combinations," "a million songs").
- All ordinals: *first*, *twelfth*, *forty-third* — not 1st, 12th.

**Use numerals**
- 10 and greater.
- Always, even under 10: versions, technical quantities (memory, disk, queries, limits), page/chapter/section numbers, step numbers, prices, numbers without units, measurements, negative numbers, decimals, percentages, dimensions, ranges.
- Any number under 10 in a sentence that also has a number ≥10 ("15 options, 6 of them deselected").

Avoid Roman numerals except for sub-sub-steps.

## Formatting

- Commas in four-digit-and-larger numbers: 1,532,784; 2,000. No separators right of the decimal.
- Leading zero for decimals under 1: 0.3. Treat decimals as plural: "1.0 inches."
- Fractions: prefer decimals (0.75). If words, hyphenate: two-fifths, one and one-half.
- Percent: numeral + % with no space (40%). At sentence start: "Forty percent."
- Dimensions: lowercase x, no spaces: 192x192.
- Exponents: standard notation, no space between base and exponent.
- Suspended hyphens: "one-, two-, or three-hour intervals."
- Write "10 times faster," not "10x faster."
- Thousands with *k*: no space, and add a noun ("55k download operations").
- Pair numbers with real-world meaning where useful (link to a pricing calculator, give a comparison).

## Ranges

- Bare numbers: hyphen, no spaces, no en dash: 2012-2016.
- Unit is a symbol or abbreviation (°C, GB, MHz, $): repeat the unit and use *to*: "-40 °C to 85 °C," "10 GB to 20 GB." A hyphen could read as subtraction.
- Unit is a spelled-out noun (minutes, files, sites): hyphen, no repeat: "5-10 minutes," "8-20 files."
- Versions: "version 2.2 or later" (not *higher* or *2.2+*); "2.2 or earlier" (not *lower*).

## Units

- Space (nonbreaking where possible) between number and unit: 64 GB, 25 mm, 50 MHz.
- No space for currency, percent, or angle degrees: $10, 65%, 180°.
- Temperature: space before the degree sign, none between sign and scale: 50 °C. Kelvin: 300 K (no degree sign).
- Number + unit modifying a noun: no hyphen unless needed ("200 GB disk"); spelled-out units do hyphenate ("128-bit system").
- Multiplied units: hyphenate (5 vCPU-hours, 40 person-hours).
- Rates: *per* in prose ("requests per day"); slash only in tight spaces. Established *p* abbreviations are fine: Gbps, Mbps, MBps. Not Gb/s.
- Don't use *per* outside rates ("per the guide" → "according to the guide"; "per Pod" → "for each Pod").
- Bytes: match the system you're documenting. kB/MB/GB are decimal (1000); KiB/MiB/GiB are binary (1024). Don't write MB when you mean MiB.

## Currency

- Make the currency unambiguous; use a code prefix if needed: US$10.
- US dollars: $ before the amount, comma thousands separators, period for cents, nothing after the decimal: $10,000; $0.006653 per vCPU hour.

## Dates

- Default: full month, day, four-digit year: January 19, 2017. With weekday: Tuesday, April 27, 2021.
- Month and year only: no comma ("January 2017").
- Mid-sentence full date: comma after the year ("The January 19, 2017, release…").
- Abbreviate only where space is tight (tables, headings), all parts at once, three letters, no periods: Mon, Sep 3, 2018. Be consistent.
- Numeric-only: ISO 8601 `YYYY-MM-DD` (2017-04-15). Never 04/05/09-style. In invented examples, pick a day >12 so it can't be mistaken for a month.
- Date and time together: date first ("May 4, 2009, at 6 PM").
- Don't use seasons or "the holidays" — use months or quarters.

## Times

- 12-hour clock with a space and capital AM/PM, no periods: 3:45 PM. Drop :00 for round hours: 3 PM. *Noon* and *midnight* are fine.
- Use 24-hour time only when the UI or code uses it, then consistently.
- Avoid time zones unless necessary. When needed, spell out the region and give the UTC offset: "US and Canadian Pacific Standard Time (UTC-8)." Don't abbreviate zone names (no "PST"). "10 AM your local time" when it's local.
