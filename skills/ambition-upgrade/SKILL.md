---
name: "ambition-upgrade"
description: "Upgrades substantive work requests (analysis, briefings, memos, decks, code) for altitude, depth, and range, runs the in-scope upgrade, and offers bigger rungs. Use automatically on such requests, or when asked to raise the bar or run /ambitious."
---

# Ambition upgrade

This skill makes an ordinary work request more ambitious, then does the work. It is adapted from Felix Rieseberg's post [How to be more ambitious: A tutorial for humans with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/) (October 2026).

The post names four kinds of ambition:

- **Speed:** the same work in less time. This is the default, so this skill skips it.
- **Altitude:** aim at the outcome the task serves, not the task itself.
- **Depth:** do the task the way a field-leading expert would, using their raw material, methods, and tools.
- **Range:** bring in fields that the task doesn't obviously need.

## Modes

- **Auto mode (default).** Use when the skill triggers on its own. Triage, rewrite, run the depth upgrade, then offer bigger rungs. Don't stop to ask before running.
- **Full mode.** Use when the user asks to raise the bar, go bigger, upgrade a prompt, or runs `/ambitious`. Build the full ladders and ask which rung to run.

## Step 1: Triage

Skip the skill entirely, and just do the task, when the request is any of these:

- A quick question, lookup, or definition.
- A small edit, reformat, or fix to existing text or code.
- An explicit instruction to do exactly X, or a request for a quick or rough version.
- A fixed procedure run by another skill, such as a recurring report with a set format.
- Personal or non-work, unless the user asks for the upgrade.
- Out of scope by the user's standing instructions or the project's instructions.

Triage is one quick decision. Don't explain it to the user.

## Step 2: Rewrite (auto mode)

1. Restate the task in one sentence: the deliverable, the audience, and the decision or action it feeds.
2. Answer the four depth questions (see Depth) silently.
3. Rewrite the request as the depth-upgraded version. Keep the same deliverable and scope.
4. Show one line before starting the work: `Upgraded to: <the rewritten request in one sentence>.` The user can stop or redirect from there.

## Step 3: Run

Do the upgraded task. While working:

- Start from raw, authoritative sources rather than digested summaries.
- Use the methods and tools a field expert would use.
- Run the outside checks in the next section before reporting results.
- If a step needs data, tools, or access you don't have, name what's missing and continue with what you can verify. Never simulate missing data or tool output.

## Step 4: Check (tiered)

Match the checks to the stakes. Never let the model grade its own work.

1. **Self-run checks (always).** Run every check you can execute: test suites, unit and dimensional checks, physical sanity bounds, reproduction of a published reference result before trusting new runs, and a match of every number in the deliverable against its source.
2. **Independent agent review (high-stakes work).** For work going to senior decision-makers, regulators, or the public, have a separate agent that didn't see the drafting try to break the result. Fix or report what it finds.
3. **Human review (always required for).** Policy judgment, and anything that leaves the organization. State this in the final response; don't treat the self-run checks as approval.

In the final response, list which checks ran and their results in one or two lines.

## Step 5: Offer bigger rungs

After the work, offer at most two rungs that would change the deliverable or need new access, one line each. Typical offers:

- An altitude rung, such as drafting the decisions the work points to, or redesigning the process the deliverable serves.
- A range rung, such as bringing in a specific outside field's method.

Don't run these without the user's yes.

## Data boundaries

Follow the user's or project's source restrictions, for example public and cleared material only. When a rung needs restricted, internal, or controlled data:

1. Name the dataset or source it would need.
2. Don't request, infer, or reconstruct it.
3. Do the strongest version possible with permitted sources and say what the restricted data would add.

## Altitude: aim at the outcome

Ask: what does the user want to happen after this deliverable exists? What is the goal behind the goal?

The ladder, from least to most ambitious:

1. **Full context.** Use all the relevant data, not just what a template needs. Report what changed, why, and what to do about it.
2. **Decisions.** Find the few most urgent decisions the work points to and draft options with arguments for and against each.
3. **Redesign the process.** Name the purpose the deliverable exists for. Design a better way to serve it, show from past data that it would have worked better, and run it alongside the current process for one cycle.

Altitude fits work that leads to a meeting, a decision, or a recurring cycle. It fits poorly for creative work. High altitude usually needs workflow changes first, such as a live data feed or a test environment where the agent can verify its own work. List that access when you offer the rung.

## Depth: work like the best in the field

Push past expert vocabulary to expert methods:

- **Use the experts' instruments.** Replace markdown tables with databases, statistical models, or simulations where the task warrants it.
- **Start from raw material.** Replace pre-digested inputs with source data.
- **Set a stretch target and hold it.** Aim well past what was requested. If a goal seems impossible, keep working on it before concluding it is.
- **Test what you believe.** Name a working assumption and try to reproduce it from the raw data, adversarially.
- **Produce new knowledge.** Once deep in the data, look for a signal or pattern nobody has named, and test it on held-out data.
- **Use an outside judge.** See Step 4.

The four depth questions:

1. What would a top professional do here that the request doesn't ask for?
2. What raw, undigested material would they start from?
3. What specific methods and tools would they use?
4. What evidence, from outside the model and the user, would show the result is right?

Depth means deeper, not bigger. Don't inflate the scope.

## Range: draw on other fields

- **Replace nouns with verbs.** Describe the deliverable by what it must accomplish. A briefing isn't a deck; it's getting busy people to believe a cause-and-effect story and decide under uncertainty in a short meeting.
- **Assemble the crew.** List four to six specialists you'd recruit if the stakes were extreme, including one red-team role that attacks the work.
- **Borrow methods, not voices.** State what each specialist does (their analysis or test), not how they write. Avoid role play.
- **Parallelize when possible.** If subagents are available, give each field's method to a separate agent and merge the results.

## Domain pack: spectrum and RF policy

Use these defaults for spectrum management, interference analysis, auctions, and federal-commercial coordination work.

**Raw sources (public):** ITU-R Recommendations and Reports, FCC dockets and ECFS filings, 47 CFR, Federal Register notices, the NTIA Manual, published NTIA technical reports, terrain and clutter datasets, census and population data, and published auction results.

**Expert methods:** Monte Carlo interference aggregation, propagation models matched to the scenario (for example ITU-R P.452 or P.2108 and P.2109 where applicable), I/N and protection-criteria analysis, sensitivity analysis on key assumptions, CDFs instead of single worst-case numbers, and coordination-zone sizing tied to population and auction value.

**Crew (methods, not voices):** an RF engineer (link budgets and propagation), an auction economist (valuation and encumbrance effects), a federal operations planner (mission impact and operational constraints), a regulatory attorney (what survives challenge), a data journalist (the clearest single chart), and, as red team, the opposing filer (the strongest technical rebuttal).

**Outside checks:** reproduce a published reference case before new runs, run the analysis code's test suite, check results against physical bounds such as free-space loss, and cross-check every figure in the deliverable against the analysis output.

## Full mode output

For each dimension that fits, give:

- A one-line reason it fits.
- Two or three numbered rewritten prompts, ready to paste.
- Prerequisites for each rung.
- The outside check for each rung.

End with one question: which rung should run first?

## Example (auto mode)

**Request:** Summarize the public comments filed on a proposed rule.

**Upgrade line:** `Upgraded to: Code every comment by issue and position in a database, report where commenters agree and split and what new evidence they introduced, and verify the coding on a random sample.`

**Checks reported:** second-pass agreement on a 10 percent sample; every cited comment matched to the docket.

**Offers:** (1) Draft the three decisions the agency faces before a final rule, with options. (2) Have a red-team pass write the strongest challenge to the likely final rule.

## Guardrails

- Don't let the model judge its own output.
- Don't simulate data, access, or tools you don't have.
- Keep a human decision gate before any irreversible action, publication, or external message.
- Don't paste long passages from sources; paraphrase and cite.