---
title: "How to Use This Repo"
aliases:
  - "How to Use This Repo"
  - "Start here"
type: guide
tags:
  - jira
  - guide
---

# How to Use This Repo

[Course home](../README.md) · Next: [Study plan](study-plan.md)

## Ways to study

Every path works best with a free Jira Cloud site to practice on; [Set Up Your Free Jira Cloud Site (Optional Hands-On Setup)](../01-introduction/04-set-up-free-jira-cloud-site.md) shows how to create one.

### Full course (about three weeks)

Follow the [study plan](study-plan.md): 15 sessions of 45-90 minutes. For each lesson, read the note's TL;DR, watch the video while repeating the steps in your own site, then answer the review questions. Finish every section with its hands-on practice and its quiz note.

### One-day recap (four to six hours)

For readers who have finished the course or already use Jira:

1. Read the [course recap](../reference/course-recap.md) from start to finish.
2. Skim [Jira terminology changes](../reference/jira-terminology-changes.md), so older articles and screenshots still make sense.
3. For each section, answer the practice questions and flashcards in its quiz note. Reopen the linked lesson for anything you miss.
4. Take the [final practice test](../reference/final-practice-test.md). A score of 20 out of 24 or better means the course material is solid.
5. Keep the [JQL cheat sheet](../reference/jql-cheat-sheet.md) and [keyboard shortcuts](../reference/keyboard-shortcuts.md) open while you work.

### JQL only (two to three hours)

1. Work through [Section 5: Filters and JQL](../05-filters-and-jql/README.md) in order, running every example query in your own site.
2. Rewrite the queries in the [JQL cheat sheet](../reference/jql-cheat-sheet.md) with your own space key and save the useful ones as filters.
3. Answer the [Section 5 Quiz](../05-filters-and-jql/07-section-5-quiz.md).
4. Put a saved filter to work on a dashboard with [Creating Personal and Team Dashboards in Jira](../08-dashboards-and-reports/01-personal-and-team-dashboards.md).

## Reading the notes

**On GitHub:** start from the course map in the [README](../README.md) and use the *Previous / Next* links at the bottom of each note to move through the course in order.

**In Obsidian:**

1. Clone or download the repository.
2. In Obsidian, choose **Open folder as vault** and select the repository folder.
3. The shared settings in `.obsidian/` already set up:
   - Markdown links with relative paths, so links created in Obsidian also work on GitHub.
   - Automatic link updates when a file is renamed or moved.
   - New attachments (pasted screenshots) saved to an `assets/` folder next to the note.
   - `_templates/` as the folder for the core **Templates** plugin.
4. Optional community plugins:
   - **Spaced Repetition**: turns the `Question::Answer` flashcards in each section quiz into review decks.
   - **Dataview**: builds live lists from note properties (see *Dataview examples* at the end of this guide).

## Track your own progress

1. Fork the repository to keep your progress in your own copy on GitHub, or clone it to keep everything local.
2. Copy [`_templates/study-log.md`](../_templates/study-log.md) to `_personal/study-log.md` and fill in the *Commitment* and *Jira sandbox* sections. Everything in `_personal/` is git-ignored, so it is never published, even from a public fork.
3. After each session, add an entry from `_templates/study-session.md` (in Obsidian: **Insert template**) and tick the session in the tracker.
4. With the Spaced Repetition plugin, review the flashcards of every quiz note you have finished. The quiz notes carry the `flashcards` tag, so they appear as decks without extra setup.
5. Record your quiz scores in the log and use the *Review reminders* list to schedule the spaced reviews from the [study plan](study-plan.md).

## Folder structure

| Path | What it contains |
|---|---|
| `00-start-here/` | This guide and the [study plan](study-plan.md) |
| `01-introduction/` ... `10-best-practices/` | One folder per course section |
| `NN-section/README.md` | Section overview: objectives, lesson table, key takeaways, hands-on practice |
| `NN-section/NN-lesson.md` | One note per course item, numbered in course order |
| `NN-section/NN-section-N-quiz.md` | Original practice questions, flashcards, and easy-to-confuse pairs |
| `NN-section/assets/` | Images used by the notes in that section |
| `NN-section/transcripts/` | Video transcripts (local only) |
| `NN-section/materials/` | Course downloads such as slides and PDFs (local only) |
| `reference/` | Glossary, cheat sheets, the course recap, and the final practice test |
| `_templates/` | Templates for lesson notes, quizzes, section overviews, study sessions, and the study log |
| `_personal/` | Private study space (local only) |
| `scripts/` | Maintenance scripts |

## Local-only content

Some folders exist in the repository but their contents are ignored by git:

| Folder | Put here | Why it is not published |
|---|---|---|
| `NN-section/transcripts/` | Video transcripts, named like the lesson note (for example `03-jql-basics.md`) | Copyrighted course content |
| `NN-section/materials/` | Slides, PDFs, and other course downloads | Copyrighted course content |
| `_personal/` | Study log, private notes, sandbox site details, certificate | Personal |

These files still show up in Obsidian, so they can be searched and linked from other local files. Public notes should never link to them, because those links would be broken for other readers.

## Conventions

### Properties (front matter)

| Property | Values | Purpose |
|---|---|---|
| `title` | Official item title | Readable name (file names are short slugs) |
| `aliases` | Usually the title | Lets Obsidian's quick switcher find the note by its title |
| `type` | `lesson`, `quiz`, `certificate`, `section`, `guide`, `reference` | Kind of note |
| `section`, `lesson` | Numbers | Position in the course |
| `duration` | `m:ss` | Video length |
| `status` | `todo`, `draft`, `done` | Whether the note is written |
| `tags` | `jira`, `section/NN`, `topic/<topic>` | Browsing by section or topic |

### Links

Use relative Markdown links, for example `[JQL cheat sheet](../reference/jql-cheat-sheet.md)`. Wikilinks (`[[...]]`) do not work on GitHub.

### Callouts

Use only the callout types that both GitHub and Obsidian render:

> [!NOTE]
> Background information.

> [!TIP]
> A shortcut or better way of doing something.

> [!IMPORTANT]
> Something needed to succeed.

> [!WARNING]
> Something that can cause problems.

> [!CAUTION]
> Something that can cause data loss or other serious harm.

### Review questions

Each lesson ends with self-check questions. The answer stays hidden until it is expanded:

<details>
<summary>What is the difference between a label and a component?</summary>
Anyone who can edit a work item can add labels freely. Components are defined by space admins and can have a lead and a default assignee.
</details>

Answers are plain text because Markdown is not rendered inside `<details>` blocks.

### Flashcards

Section quiz notes contain one flashcard per line:

```text
What does WIP stand for?::Work in progress
```

### JQL

JQL is written in code blocks tagged `sql`, which gives useful highlighting on GitHub and in Obsidian:

```sql
project = ABC AND assignee = currentUser() AND statusCategory != Done
```

### Images

Save images to the section's `assets/` folder as `<lesson-number>-<short-description>.png` and embed them with a relative link: `![Board with WIP limits](assets/05-wip-limits.png)`.

### File names

Lowercase kebab-case with a two-digit prefix, for example `03-jql-basics.md`. The full title lives in the `title` property.

## Maintaining the notes

This part is for anyone who edits the notes, whether in a fork or in a pull request.

### Updating progress

The progress tables in the README and the section overviews are generated from each note's `status`. After changing notes, run:

```bash
python scripts/update_progress.py
```

Use `python scripts/update_progress.py --check` to verify that the tables are up to date without changing anything.

### Commit messages

Small, focused commits make the history easy to follow:

| Example | Use for |
|---|---|
| `notes(s03): add WIP limits and swimlanes lesson` | Lesson or quiz notes (`s03` = section 3) |
| `ref: add time-based JQL examples` | Changes in `reference/` |
| `docs: clarify Obsidian setup` | Guides and READMEs |
| `chore: update progress tables` | Generated or maintenance changes |

## Dataview examples

With the Dataview plugin installed, these queries list notes by status:

````text
```dataview
TABLE section, lesson, duration
WHERE type = "lesson" AND status != "done"
SORT section ASC, lesson ASC
```
````

````text
```dataview
LIST
FROM #topic/jql
SORT file.name ASC
```
````
