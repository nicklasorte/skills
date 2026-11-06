# Language, grammar, and punctuation details

Paraphrased from the Google developer documentation style guide (CC BY 4.0). For anything not here, check https://developers.google.com/style.

## Voice, tense, person

- **Second person**: address the reader as *you*. Use *we* only for the organization speaking ("We recommend…") and sparingly.
- **Active voice**: name who acts. Passive is acceptable when the actor is unknown or irrelevant, or to avoid blaming the reader ("The file is deleted" after an error).
- **Present tense**: describe what happens, not what *will* happen. Future tense only for events that truly occur later.
- **Prescriptive word choice**:
  - *must* — required. Also "you need to."
  - *can* — permission, ability, or an optional action.
  - *might* — possibility.
  - *may* — reserve for legal or policy text.
  - Generally avoid *should* (ambiguous between required and recommended). Say "We recommend that you…" or *must*. *Should* is OK for a widely recognized recommendation ("You should use a strong password").
  - Avoid *could* where *can* works; avoid *shall*; avoid hypothetical *would*.
- **Anthropomorphism**: don't give software feelings or intent ("the server wants," "the app thinks").
- **Contractions**: common ones are fine (*don't*, *it's*, *you're*). Prefer negation contractions (*isn't*, *don't*, *can't*), because readers can miss a standalone *not*. Avoid nonstandard contractions where *'s* or *'re* means *is* or *are* after a noun (*the browser's slow*, *guides're*) and three-word contractions (*mightn't've*).

## Tone checklist

Avoid:
- Buzzwords and unexplained jargon; define unavoidable jargon on first use.
- Idioms, metaphors, sports or pop-culture references, and figurative language ("out of the box," "low-hanging fruit," "silver bullet," "hang" for unresponsive).
- Filler and placeholder phrases: *please note*, *at this time*, *in order to* (use *to*).
- Subjective qualifiers (from the guide): *simply*, *just*, *easy*, *quickly*, *carefully*, *thoroughly*, *proper*, *properly*, *performant*.
- *(Skill addition)* Similar words the guide doesn't list but that fail the same test: *obviously*, *of course*, *basically*, *actually*, *robust* without evidence.
- Starting many sentences the same way ("You can… You can…").
- *Let's*, exclamation points, internet slang (tl;dr, ymmv, RTFM).

Do:
- Write so a reader with intermediate English and a machine translator both get it: short sentences (aim for fewer than 26 words), one idea each, consistent terms, keep helper words like *that* and *then* ("if… then").
- Use transitions to keep paragraphs from feeling choppy.

## Global-audience sentence rules

- Prefer a single verb to a phrasal verb ("uses," not "makes use of"; "find," not "find out").
- Don't stack more than two noun modifiers ("the instance configuration settings page" → "the settings page for instance configuration").
- Put *only* immediately before what it modifies ("Request only one token").
- Replace ambiguous *using* with *by using* or *that uses* ("Connect by using SSH").
- Avoid gerund objects where an infinitive works ("describes how to set up," not "describes setting up").
- Avoid double negatives.
- Repeat a word when it removes ambiguity ("if the VM has started and if you can connect").
- Replace an ambiguous *it* or *this* with the noun it refers to.
- Don't use *while* to mean *although*; don't use *with* to mean *has* ("a phone that has 2 GB of RAM").

## Accessibility in prose

- Don't use all caps or camel case for emphasis in running text.
- Don't name a casing style ("camel case," "snake case"); describe it and give an example.
- Don't force line breaks inside paragraphs.
- Use exclamation marks, question marks, and semicolons sparingly; some screen readers don't voice them clearly.
- Don't rely on directional or color-only cues ("the green button on the right").

## Global and inclusive language

- Use the singular *they* for unknown people; avoid *he/she*, *(s)he*, *guys*.
- Avoid ableist or violent figurative terms (*crazy*, *sane*, *sanity check* → *quick check*; *cripple* → *slow*; *kill* → *stop*; *nuke*; *blast radius* → *affected area*).
- Replace *master/slave* with precise pairs (*primary/replica*, *controller/worker*); *blacklist/whitelist* with *denylist/allowlist* (nouns only, not verbs) or a rewrite describing the action.
- Avoid *native* for features (use *built-in*), *grandfathered* (use *legacy* or *exempt*), *man-hours* (use *person-hours*).
- Say *the US*, not *America*, for the country.

## Abbreviations

- Spell out unfamiliar abbreviations on first use, with the abbreviation in parentheses: *Border Gateway Protocol* (*BGP*). Google italicizes both parts in that introduction.
- Capitalize the long form only if it's a proper noun: data manipulation language (DML).
- Then use the abbreviation alone. If you use it only once, include the abbreviation only if it's as common as the spelled-out term; otherwise leave it out.
- Don't spell out very common ones: AI, API, CPU, PDF, HTML, RAM, URL, USB, OS, MB/GB/GiB.
- Don't spell out where the expansion doesn't help (PDF).
- Don't abbreviate off-topic terms just to save words.
- No *e.g.*, *i.e.*, *approx.*, *aka*; avoid *etc.*
- No periods in acronyms and initialisms; periods on shortened words (*Dr.*) except date/time abbreviations; no periods for state or country codes.
- Plurals: add *s* (APIs, VMs); no apostrophe.
- Don't use abbreviations as verbs (*ssh into*, *RDP to*).
- *a* or *an* follows pronunciation: *an SAP system*, *a SQL query*, *an HTTP request*.

## Capitalization

- Sentence case for headings, titles, table headers, captions, and button-like labels you write.
- Don't capitalize common nouns for emphasis or because they're important in your domain ("the cloud," "internet," "machine learning").
- Match the official capitalization of product names and UI labels.

## Punctuation

- **Commas**:
  - Serial comma always.
  - After an introductory word or phrase ("In the console, click **Save**").
  - Before a coordinating conjunction joining two independent clauses, unless both are very short.
  - Before nonrestrictive *which*; never before restrictive *that*.
  - Not before *because*, unless it opens a nonrestrictive clause.
  - With conjunctive adverbs (*however*, *therefore*, *otherwise*): semicolon, period, or dash before; comma after.
- **Colons**: after an independent clause to introduce a list, example, or explanation. Lowercase after a colon unless what follows is a proper noun, a heading, a quotation, or text after a notice label (**Note:** The…).
- **Em dashes** (—) with no spaces, for breaks or to introduce an example ("Enter a name—for example, `vm-01`."). Don't use dashes in description lists; use a colon.
- **Hyphens**:
  - Hyphenate compound modifiers before a noun when needed for clarity ("read-only file," "high-availability cluster"); not after ("the cluster has high availability"). No hyphen after *-ly* adverbs.
  - Avoid compound modifiers of three or more words; move words after the noun.
  - Generally close prefixes (*reenter*, *preconfigured*), except: always hyphenate *self-* and *cross-* (*self-managed*, *cross-region*); *non-* is often hyphenated (*non-integer*, *non-key*); hyphenate when the root is capitalized or numeric (*pre-2020*, *non-Google*) or the closed form is confusing.
  - At the start of a sentence or heading, capitalize only the first part of a hyphenated word ("Read-only access").
- **Text formatting**:
  - **Bold**: only for UI elements, run-in headings, and notice labels.
  - *Italics*: emphasis, words used as words, a term's first introduction, titles of full-length works, and version variables (1.4.*x*).
  - Underline: only for links.
  - Don't use all caps for emphasis.
- **Parentheses**: use sparingly; prefer rewriting. Period goes inside only if the whole sentence is inside.
- **Quotation marks**: straight (`"` and `'`), never curly. Double quotes, American style (periods and commas inside, unless it's code or a literal string the reader types). Single quotes only inside a double-quoted quotation or in code. Don't use quotes for emphasis or around link text.
- **Periods with URLs**: avoid ending a sentence with a URL; put it on its own line without a period, or use link text.
- **Semicolons**: allowed between closely related independent clauses, but usually two sentences read better.
- **Slashes**: avoid *and/or* (write "A, B, or both"); avoid slashes meaning "or" in prose.
- **Ellipses**: avoid in prose; OK in code syntax for repetition.
- **Exclamation points**: avoid.
- **Ampersand**: don't use for *and* in prose or headings.
- One space after periods.

## Possessives

- Don't make product, feature, or trademark names possessive. Use the name as a modifier or rewrite with *of*: "BigQuery API limits" or "the limits of the BigQuery API," not "the BigQuery API's limits." A company name used as a company is fine ("Google's office").
- Don't make an abbreviation possessive right after defining it ("the rule that the FTC issued," not "the FTC's rule").
- For code items, make the following noun possessive, not the code ("the `wordCount` method's return value").
- Singular nouns ending in *s* take *'s* (the class's methods); plural nouns ending in *s* take only an apostrophe (the models' capabilities). Rewrite awkward possessives.

## Pronouns

- Use *that* for restrictive clauses (no comma) and *which* for nonrestrictive clauses (with a comma).
- Keep the optional *that*: "the link that you want to open," not "the link you want to open."
- Follow *this*, *that*, *these*, and *those* with a noun: "Set this value to `true`," not "Set this to `true`."
- Replace an *it* that could refer to more than one thing with the noun.

## Sentence order

- Condition or goal first, instruction second: "If you use a proxy, set `HTTPS_PROXY`."
- Put the most important information early in the sentence and paragraph.
- Use *because* for causation, not *since* or *as*. Use *after*, not *once*, for time order.
