---
name: "oxford-tutorial-lessons"
description: "Formats technical lessons as Oxford-style tutorials: one weekly question, a short paper plus MATLAB code, and a Socratic review. Use when writing, planning, or reformatting any lesson, weekly question, tutorial paper, or mentor guide in Nick's training series, or when he asks for next week's lesson. Do not use for general MATLAB coding help; use matlab-builtin-first."
---

# Oxford tutorial lesson framework

Use this framework to write or reformat every lesson in a training series. Each lesson is one week. The learner gets one question, reads and runs an analysis, and submits two things: a short paper that answers the question and the MATLAB code that produced its results. Then the learner defends both in a tutorial with the mentor.

Apply the Google developer documentation style guide to everything this skill produces.

## How the Oxford tutorial works

These points come from Oxford's own descriptions of the method. Keep them; they are what make the format work.

- **Small and personal.** Traditionally one tutor and one or two students meet for about an hour, once or twice a week.
- **One question drives the week.** The student reads with the question in mind and drafts an answer early, rather than collecting notes first.
- **The written work is the entry ticket.** Many tutors read the essay or problem sheet before the session so they can prepare challenges. Others ask the student to summarize the argument at the start.
- **Socratic questioning, not lecture.** The tutor probes the student's reasoning, asks them to justify assumptions, and widens the discussion to other views. The goal is to draw out the student's thinking, not to fill them with facts.
- **Low stakes, high effort.** Weekly work doesn't count toward the degree, so students can experiment. First papers are expected to be imperfect.
- **Sciences adapt the format.** Engineering and physics tutorials often use problem sheets, with essays, literature reviews, or project plans for some topics. This framework combines the two: the paper is the essay, and the MATLAB code is the problem sheet.

Research on the method (Ashwin, 2005) found that students experience tutorials anywhere from "the tutor explains what I got wrong" to "the tutor and I exchange views and both reach a new understanding." Aim every session at the second end.

Known failure modes: sessions can feel intense, and the method is labor-intensive for the mentor. Keep questions focused so the weekly load is realistic.

## Don't give the learner the steps

The learner works out how to do the analysis. The learner's sections state what the code and paper must produce and the requirements they must meet, never the procedure, the function names, or the order of operations. Put the procedure, a reference function list, reference tests, and any reference code in the mentor-only tutorial guide, where the mentor uses them to review the learner's design. A learner's design can differ from the reference and still be correct.

Background that explains how the domain works, such as how to read the Table of Allocations or what a record note means, is fine in the learner's sections. Steps for building the code are not.

## The weekly cycle

| Day | Learner | Mentor |
| --- | --- | --- |
| 1 | Receive the question and reading list. Write a first-guess answer in two or three sentences. | Issue the question; be available for scoping questions only. |
| 1-4 | Read with the question in mind. Design, write, and test the MATLAB code. Draft the paper section by section. | None. |
| 5 | Submit the paper and code together at least 24 hours before the tutorial. | Read the paper, run the code, and pick three to five challenges from the tutorial guide. |
| 6 or 7 | Attend the 60-minute tutorial. | Run the tutorial (see protocol below). |
| After | Write a one-paragraph reflection: what changed in your answer, and why. Fix code issues raised in the tutorial before the next week builds on it. | Record two or three feedback points with the rubric. |

Adjust the days to the learner's schedule, but keep the order: question, independent work, paper and code, tutorial, reflection.

## Lesson format

Write every lesson with these sections, in this order. The first eight sections go to the learner. The tutorial guide is for the mentor only.

### 1. Week and title

`Week N: <topic>`. One line.

### 2. The question

One question, in one or two sentences. A good tutorial question:

- Requires a judgment or a defended position, not recall. Prefer "how confident," "which should drive," "what would have to change," and "is X the right basis for Y."
- Can be answered only by doing the week's reading and running the analysis in code.
- Ties to the series' end project, so each week's answer feeds the capstone.
- Has more than one defensible answer, so the tutorial has something to argue about.

Bad: "What fields are in a GMF record?" Good: "What must a spectrum report tell the FCC to protect in this band, and which systems should drive the plan?"

### 3. Why this question matters

Two or three sentences connecting the question to the end project and to a real decision someone will make. Where the office has a standard workflow or report section that the lesson feeds, such as Section 2 of a spectrum report, name it.

### 4. Background and reading

- **Background:** short primers on how the domain works, in the order an analyst uses them. Explain concepts, not code steps.
- **Core reading:** two to four sources, each with a link, the edition or date, and the exact sections to read.
- **Further reading:** optional sources for learners who want depth.
- **Ask:** the person to contact when the reading runs out, from the series contact list.

### 5. MATLAB assignment

The code is a required submission, not an optional exercise. State only the outcome and the requirements:

- **The task:** what the code must accomplish, in one or two sentences, such as "Use MATLAB to filter the GMF. Your first result is the set of assignments under a primary allocation."
- **What it must produce:** the tables, figures, and values the paper uses, in the order the paper presents them.
- **Requirements:** the code standards, testing against known answers, and any data-handling rules. Don't name the functions or prescribe the design; tell the learner they'll defend their design in the tutorial.
- **Builds on:** which previous week's outputs it reuses.

If the task uses controlled or classified data, such as the GMF, state the handling rule: work only on approved systems, and keep the code, outputs, and paper at the same classification as the data.

### 6. Code standards

Every submission meets these standards. Include this section in each lesson, or link to it once for the series.

- **Structure:** one function per file, plus a driver script named `weekNN_main.m` that runs the whole analysis from raw inputs and regenerates every figure and table in the paper.
- **Help text:** each function starts with a help block: one-line summary, inputs and outputs with units, and an example call.
- **Units:** name variables with their units where it helps, such as `dist_km` and `loss_dB`. Convert units in one place, using the helper functions from earlier weeks.
- **Tests:** a test script, `weekNN_tests.m`, using `assert` or `matlab.unittest`, that runs clean before submission.
- **Clean code:** no warnings from the MATLAB Code Analyzer (`checkcode`), no hard-coded file paths, and no unexplained constants. Name constants and cite their source in a comment.
- **Reproducible:** list MATLAB release, toolboxes, and data sources at the top of the driver script. The mentor should be able to run it and get the paper's figures.
- **Version control:** commit the week's work to the series repository with a short message, if one is in use.
- **Reuse:** later weeks call earlier weeks' functions rather than copying them. Fix a bug in the original file.

### 7. The paper

Default specification; the mentor can change it per lesson. When the lesson feeds a standard report section, write the paper as a draft of that section and put the reasoning in short analyst notes after it.

- **Length:** 1,500-2,500 words, or three to five pages, plus figures. Shorter is fine if the argument is complete.
- **Structure:**
  1. **Answer:** the learner's answer to the question in the first paragraph.
  2. **Approach:** what you did and why, briefly. Name the functions that do each step.
  3. **Evidence:** results from the code, with figures and tables. Every figure is produced by the driver script.
  4. **Assumptions and limits:** what you assumed, and how the answer changes if you're wrong. Where you can, show this with a sensitivity run in the code.
  5. **Alternatives:** the strongest case against your answer, and why you still hold it or don't.
  6. **So what:** what this means for the end project.
- **Appendix:** a list of the submitted code files with one line each, and the data sources.
- **Style:** Google developer documentation style. Units on every number. Cite sources with links.

### 8. Deliverables for the next week

The tested code and data the learner carries forward, described by what they do rather than by prescribed file names. Later weeks depend on these, so they must run.

### 9. Tutorial guide (mentor only)

Mark this section clearly and remove it before sending the lesson to the learner.

- **What a strong answer looks like:** three to five bullet points, not a model essay.
- **Reference solution outline:** a typical order of operations, a reference function list with inputs and outputs, reference tests with expected values, and any reference code. Note that the learner's design can differ and still be correct.
- **Question ladder:** six to ten prepared questions, ordered from clarifying to transferring:
  1. Clarify: "What do you mean by...?" "Walk me through this figure."
  2. Assumptions: "What did you assume here? How would the answer change if that were wrong?"
  3. Evidence: "How do you know? What would convince you otherwise?"
  4. Alternatives: "What's the strongest argument against your answer?"
  5. Implications: "If you're right, what follows for the end project?"
  6. Transfer: "Where else would this reasoning apply?"
- **Code review questions:** three to five, such as "Show me where this number comes from in your code," "What does this function do with a blank field?" and "How did you test this against a known answer?"
- **Likely misconceptions:** two to four common errors, in the reasoning or the code, and the question that exposes each one.
- **Bridge:** one question that sets up next week's topic.

## Tutorial protocol (60 minutes)

1. **Opening, 5 minutes:** the learner states their answer in under three minutes, without slides.
2. **Probe, 30 minutes:** the mentor works the question ladder, following the learner's reasoning rather than a script. Ask, then wait. Don't lecture until the learner has tried.
3. **Code walkthrough, 10 minutes:** the learner traces one key result from raw input to figure in their code and explains their design. The mentor asks the code review questions.
4. **Widen, 5 minutes:** bring in other views, real cases, or how the office has handled similar questions.
5. **Close, 10 minutes:** the learner says what changed in their thinking. The mentor gives two or three feedback points, lists any code fixes needed before next week, and introduces the bridge question.

Mentor rules:

- Treat the session as an exchange; the mentor should be willing to change their own view.
- Challenge the argument and the code, not the person.
- When the learner is stuck, narrow the question rather than giving the answer.

## Feedback rubric

Score each criterion 1 to 4 for the learner's own tracking. The scores don't grade the learner; use them to pick next week's focus.

| Criterion | 1 | 4 |
| --- | --- | --- |
| Answers the question | Describes the topic | States and defends a clear answer |
| Evidence and analysis | Unsupported or wrong | Correct, sourced, and sufficient |
| Assumptions | Hidden | Explicit, with sensitivity shown |
| Alternatives | Ignored | Strongest counterargument addressed |
| Clarity | Hard to follow | Answer first, clean figures, units throughout |
| Project relevance | None stated | Clear consequence for the end project |
| Code correctness | Doesn't run, or results don't match the paper | Runs clean, tests pass, reproduces every figure |
| Code quality | Undocumented, hard-coded | Meets every code standard; reusable next week |

## When reformatting an existing lesson

1. Keep the existing reading, links, contacts, and exercises; don't drop sources.
2. Rewrite the objective as one tutorial question that meets the criteria above.
3. Turn the exercise into the MATLAB assignment: state the task, the outputs, and the requirements. Move any existing steps, function names, and code snippets into the reference solution outline in the mentor guide.
4. Point the paper at the question and at the code's outputs.
5. Write the tutorial guide last, including the reference solution outline and code review questions.
6. Show the reformatted lesson to Nick for confirmation before applying the format to the rest of the series.

## Example: Week 1 for the 2.7 GHz radar retuning series

**Week 1: Allocations and incumbent federal systems**

**The question:** What must a spectrum report tell the FCC to protect in and around 2700-2900 MHz? Establish what is allocated in the band, which federal systems operate under those allocations and where, and whether each assignment is primary, secondary, or non-interference basis (NIB). Then defend which systems should drive the retuning plan.

**MATLAB task (learner sees this):** Use MATLAB to filter the GMF. Your first result is the set of frequency assignments that operate under a primary allocation. Then account for the secondary, NIB, and nonconforming assignments.

**Paper:** a draft Section 2 of a spectrum report, with analyst notes.

**Reference outline (mentor only):** load the extract and keep 2655-3100 MHz; build the allocation table; map station class to service and match each assignment to its allocation; keep the primary-allocation assignments; separate secondary and nonconforming ones; apply the record notes, moving P032 assignments to NIB.

**Bridge to week 2:** "Your table has peak power and bandwidth for every radar. What else do you need before you can say whether one radar interferes with another?"

## Sources

- Palfreyman, D. (2018). A primer for exploring the concept of "the Oxford tutorial." OxCHEPS. https://oxcheps.new.ox.ac.uk/papers/OxCHEPS_OP70b.pdf
- Ashwin, P. (2005). Variation in students' experiences of the Oxford tutorial. Higher Education, 50(4), 631-644. https://eprints.lancs.ac.uk/27328/
- St Hugh's College. Studying at Oxford 2023-24. https://www.st-hughs.ox.ac.uk/wp-content/uploads/2023/08/Studying-at-Oxford-2023-24-1.pdf
- TutorChase. The Oxbridge tutorial system explained. https://www.tutorchase.com/blog/the-oxbridge-tutorial-system-explained
- Engineering Tutorials (CCCU GlobalEd, Oxford program guide). https://cccuglobaled.org/wp-content/uploads/2020/12/Engineering-Tutorials.pdf