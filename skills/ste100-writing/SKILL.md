---
name: "ste100-writing"
description: "Write, rewrite, or audit technical text in ASD-STE100 Simplified Technical English (Issue 9). Use when the user asks for STE, ASD-STE100, controlled language, or procedures that can't be misread."
---

# ASD-STE100 Simplified Technical English

ASD-STE100 is a controlled language for technical documentation. Issue 9 (January 2025) has 53 writing rules in 9 sections (Part 1) and a dictionary of about 900 approved words (Part 2).

This skill paraphrases the rules. It doesn't reproduce the official text or dictionary. ASD owns the copyright and the trademark. The free official copy is at https://www.asd-ste100.org (request form). For an authoritative word ruling, tell the user to check the dictionary.

## When this skill governs

- Use STE when the user names STE, ASD-STE100, or controlled language.
- Use STE for procedures, checklists, test steps, and safety instructions the user wants to be unambiguous.
- Where STE and the google-developer-writing-style skill conflict, STE governs for that text. Keep Google style for formatting that STE doesn't address (headings, code font, link text).

## Modes

Ask which mode only if the request doesn't make it clear.

- **Strict:** Apply all rules below, including vocabulary discipline. Flag every word you aren't sure is approved.
- **STE-inspired:** Apply the sentence and grammar rules. Relax the vocabulary rule. Use this for briefings, READMEs, and email.
- **Audit:** Don't rewrite. Return a table of violations: location, rule, problem, and suggested fix.

## Step 1: Classify the text

| | Procedural | Descriptive |
|---|---|---|
| Purpose | Tell the reader what to do | Tell the reader what a thing is or does |
| Verb form | Imperative ("Set the attenuator to 10 dB.") | Simple present, past, or future |
| Maximum sentence length | 20 words | 25 words |
| Unit | One instruction per sentence | One topic per paragraph |

Don't mix the two types in one paragraph.

## Step 2: Apply the rules

### Words

- Use one word for one meaning. Use each word as one part of speech only.
- Use the same term for the same thing every time. Don't vary it for style.
- Use technical names from the subject field as nouns (for example, "antenna", "emission mask", "coordination zone", "EIRP"). Don't use a technical name as a verb.
- Use technical verbs from the subject field only when no approved verb works.
- Don't use words that are vague or that have many meanings. Replace them with a specific approved word.
- Don't use contractions.
- Don't use intensifiers or difficulty words such as "very", "just", "simply", or "easily".

### Noun clusters

- Don't use more than three nouns in a row. Break longer clusters with prepositions or a hyphen.
  - Not STE: "interference protection criteria threshold value"
  - STE: "the threshold value of the interference protection criteria"

### Verbs

- Use only these forms: imperative, simple present, simple past, simple future, infinitive, and the past participle as an adjective.
- Don't use the past participle with "has", "have", or "had" (no perfect tenses).
- Don't use the -ing form, except in a technical name.
- Use the active voice. In descriptive text, use the passive only when you don't know the agent.

### Sentences

- Write one topic per sentence.
- Don't omit words to make text shorter. Keep the subject, verb, and articles ("the receiver", not "receiver").
- Don't use semicolons. Make two sentences.
- Use a vertical list for complex text.
- Count each code token, identifier, number with its unit, and quoted string as one word.

### Procedures

- Write one instruction per sentence. Two actions can share a sentence only if the reader does them at the same time.
- Start each instruction with the verb.
- Put a condition before the instruction ("If the alarm comes on, stop the test.").
- Put a description or note in a separate sentence, not inside the instruction.

### Descriptions

- Give one new fact per sentence.
- Use key words ("first", "then", "because", "but") to show the logic.
- Keep paragraphs to six sentences or fewer.

### Safety instructions

- Start a warning or caution with a clear command ("Do not touch the feed horn.").
- Then give the risk in a short sentence ("High RF power can cause burns.").
- Keep each warning specific. Don't use one warning for many hazards.

### Punctuation

- Use a colon only before a list. Don't use semicolons.
- Don't use parentheses for more information that belongs in its own sentence.

## Step 3: Check before you return text

Run this checklist. Fix each item.

1. Count the words in the three longest sentences. Split any sentence over 20 (procedural) or 25 (descriptive).
2. Search for perfect tenses: "has been", "have", "had" + past participle.
3. Search for -ing words that aren't technical names.
4. Search for passive constructions in procedures.
5. Search for semicolons and contractions.
6. Look for noun clusters of four or more nouns.
7. Look for two instructions joined with "and" or "then".
8. Look for missing articles.
9. In strict mode, list each word you aren't sure is approved.

## Common substitutions (illustrative, not the official dictionary)

| Avoid | Use |
|---|---|
| utilize | use |
| ensure | make sure |
| prior to | before |
| in order to | to |
| commence | start |
| terminate | stop |
| verify | make sure, examine |
| sufficient | enough |
| approximately | approximately is approved in some uses; check the dictionary |

## Output

- **Rewrite:** Return the STE text first. Then give a short list of the main changes, only if the user asks or the change affects meaning.
- **Audit:** Return a table with columns Location, Rule, Problem, and Fix.
- If a rewrite changes the technical meaning, stop and ask the user before you finalize it.

## Disclaimer

This skill is an unofficial aid. ASD and the STEMG don't affiliate with or endorse it. No tool can certify STE compliance.
## Coordinated skill handoffs

Primary owner when ASD-STE100 or controlled-language drafting/audit is requested. Its language rules override Google Developer Writing Style on conflicts. Do not claim official STE compliance without the authoritative standard and a supported verification process.

For a multi-skill request, follow the repository `skill-router` and `AGENTS.md` when available. Keep one primary owner, preserve source evidence and outstanding decisions, and avoid duplicate work. A handoff is an instruction for the host agent to consider another skill, not a direct executable call. Do not bypass this skill's own required approval, template, data-handling, or verification gates.
