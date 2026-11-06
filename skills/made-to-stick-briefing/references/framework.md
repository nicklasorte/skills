# Sticky Briefing Framework

Five tools, used in this order:

1. **Sticky Brief canvas.** Think before designing.
2. **Diagnostic grid.** Find where the message breaks.
3. **Pattern decision guide.** Pick the move that fixes it.
4. **Slide checklist.** Triage every slide.
5. **Outsider test.** Measure what actually stuck.

Source examples and page references are in `playbook.md`.

---

## 1. Sticky Brief canvas

Fill this in before any slide exists. If a box can't be filled from the source material, that is a finding: mark it **GAP** and ask, don't invent.

| Box | Prompt | Principle |
|---|---|---|
| **Core** | The one sentence a non-expert repeats in the next meeting. Lead with it. | Simple |
| **Commander's intent** | "If they remember nothing else, they must know ___." | Simple |
| **Wrong assumption** | What does this audience believe that the analysis overturns? | Unexpected |
| **The gap** | The question they'll want answered after the hook. | Unexpected |
| **Protagonist** | One real, named thing to follow (a site, system, person). | Concrete |
| **Analogy** | A familiar thing that keeps producing correct intuitions (pomelo test). | Simple / Concrete |
| **Hardest case** | The Sinatra example: "if it works there, it works anywhere." | Credible |
| **Testable check** | What can the audience verify themselves, in a minute, without a model? | Credible |
| **Vivid detail** | One specific detail that makes the claim feel real. | Credible |
| **Big number → relationship** | Each large figure, restated as a comparison, ratio, or time. | Credible |
| **Who is affected** | A named role or place; what goes wrong for them. | Emotional |
| **Why this audience cares** | Their self-interest or identity: what it means for *their* decision. | Emotional |
| **Episodes** | 3–5 beats with a turn; which plot (challenge, connection, creativity)? | Story |
| **Associations** | What the audience already values that the idea can borrow, and worn-out words to avoid. | Emotional |
| **Twist** | The plausible answer that fails, and why. | Unexpected / Story |
| **Pending / caveats** | What's placeholder, unverified, or missing, stated plainly. | Credible |
| **Ask** | The decision or action wanted. | Story (act) |

---

## 2. Diagnostic grid

The audience journey from the book's epilogue, crossed with the six principles. For a draft, mark each row **OK**, **WEAK**, or **BROKEN**, note the evidence, and fix BROKEN rows first, top to bottom (no attention means nothing else matters).

| Audience stage | Primary principle | Symptom when broken | Diagnostic question | Go-to fixes |
|---|---|---|---|---|
| **1. Pay attention** | Unexpected | Phones out by slide 3; "we know this already" | What expectation does slide 1 break? | Break a schema; predict-first; open a gap |
| **2. Understand and remember** | Concrete (+ Simple) | Can't retell it the next day; jargon questions | Could they draw it? Is there a named thing? | Protagonist; analogy; prop; concrete goal |
| **3. Believe** | Credible | "Says who?" "That's just the model." | Can they check it themselves? | Testable check; Sinatra case; human-scale stats; vivid detail |
| **4. Care** | Emotional | "Why is this on my desk?" | Who is affected, and what's in it for this audience? | Stakes by role; one named person; identity; self-interest |
| **5. Act** | Story | Agreement but no decision | Can they simulate what happens next? | Process episodes; springboard story; clear ask |
| **Throughout** | Simple | Ten points of equal weight | Is there one core, stated first? | Commander's intent; cut to backup |

**Typical pattern for technical briefings:** stage 2 (abstraction, acronyms) and stage 4 (no person, no stakes) break first. Stage 3 often looks fine to analysts but fails for decision-makers, because model output is not a testable credential.

---

## 3. Pattern decision guide

Start from the problem you have, then pick a pattern. Book sources and examples are in `playbook.md` Sections 4 and 7.

| If the problem is… | Use | How |
|---|---|---|
| A big number nobody can feel | **BB bucket** | One unit → a familiar cluster → the whole, as a build |
| | **Popcorn comparison** | Set the figure beside familiar things |
| | **Time scale** | Convert a count into time at human pace |
| | **Human-scale scene** | Recast percentages as a team or room |
| "They won't trust the model" | **Where's the beef** | Hand them the check; give them a minute |
| | **Sinatra test** | Show the hardest case working |
| | **Edible-fabric stack** | Hard case + vivid detail + ratio together |
| | **Antiauthority** | Someone whose experience is the proof (the Doe Fund driver) |
| Too abstract | **Follow one named thing** | One real entity through every slide |
| | **Generative analogy** | Map onto a familiar puzzle that keeps working |
| | **Prop** | A physical stand-in for the idea |
| | **Concrete goal** | Specify like the 727: number, place, time |
| They don't see why it matters | **Stakes by role** | Name who is hurt and how |
| | **Imagine yourself** | Have them picture using the result in their own job |
| | **No Analytical Hat** | Don't put a calculation next to the emotional beat |
| | **Rokia** | One identifiable case before any aggregate |
| | **Identity** | "What would someone in your role do?" |
| The method is complex | **Mystery structure** | Puzzle first, then rival explanations |
| | **Rounds as story** | Numbered episodes that simulate the process |
| They agree but won't act | **Pick the plot** | Challenge to inspire effort, connection to inspire cooperation, creativity to inspire new approaches |
| | **Testable rule** | Reduce the method to a rule anyone can apply |
| The audience thinks they already know | **Predict first** | Ask for a guess, then reveal |
| | **Good-enough-isn't twist** | Show a plausible answer failing |
| Too many messages | **Commander's intent** | One sentence; everything else to backup |
| Experts insist on detail | **Conference storybook** | Keep their stories up front, details in backup |

---

## 4. Slide checklist

Ask six yes/no questions of each slide:

1. **One point?** Can you state the slide's single takeaway in under 12 words? (Simple)
2. **Gap?** Does it open or close a question the audience cares about? (Unexpected)
3. **Named thing?** Is there a real place, system, person, or object? (Concrete)
4. **Checkable?** Is the claim testable by the audience, or clearly sourced and caveated? (Credible)
5. **Person?** Is someone affected, or is it tied to this audience's interests? (Emotional)
6. **Moves the story?** Would removing it break the sequence? (Story)

**Triage rule:**
- **0–1 yes** → move to backup or cut.
- **2–3 yes** → revise, starting with the first "no."
- **4+ yes** → keep.

Every main-deck slide must also pass the accuracy guardrails in `playbook.md` Section 12, regardless of score.

---

## 5. Outsider test protocol

This measures stickiness, which an expert can't judge from inside (the tappers and listeners problem).

1. **Pick the tester.** Someone smart and outside your field: a staffer from another office, or a family member. Not a colleague who knows the work.
2. **Brief them in two minutes.** Use the main deck only, at normal pace. No Q&A.
3. **Wait at least a day.**
4. **Ask three questions:**
   - "What was that about?" (tests the core)
   - "What do you remember?" (tests what stuck)
   - "Why does it matter?" (tests the stakes)
5. **Score the retelling:**
   - Core repeated correctly → Simple works.
   - Specific names or images recalled → Concrete works.
   - A number recalled as a relationship (as a comparison, not a raw figure) → Credible works.
   - Can say who is affected → Emotional works.
   - Retells it as a sequence → Story works.
6. **Look at what they got wrong.** Distortions show where the Curse of Knowledge is. Fix those slides first.
7. **Record it.** Note what stuck and what dropped, so the next briefing starts from evidence.

Speakers-and-stickers rule of thumb from the book: listeners keep the stories and lose the statistics. If the retelling contains only conclusions and no story, the deck is still too abstract.
