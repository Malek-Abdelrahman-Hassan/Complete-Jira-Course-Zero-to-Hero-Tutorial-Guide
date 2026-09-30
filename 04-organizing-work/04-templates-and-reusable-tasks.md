---
title: "Creating Templates and Reusable Tasks for Efficiency"
aliases:
  - "Creating Templates and Reusable Tasks for Efficiency"
type: lesson
section: 4
lesson: 4
duration: "6:04"
status: done
tags:
  - jira
  - section/04
  - topic/templates
---

# Creating Templates and Reusable Tasks for Efficiency

[Course home](../README.md) › [Section 4: Organizing Your Work](README.md) › Lesson 4 · 6:04

## TL;DR

Jira Cloud has no dedicated template library for work items (formerly *issues*). The lesson's pattern is to create a master **Task** once, mark it with a `template` label, and **clone** it whenever the team repeats the same checklist — for example a sprint planning checklist each sprint. Checklist items can live in the description or as **subtasks**; cloning can include subtasks so each copy is ready to work through.

## Key concepts

- **Template work item**: A reusable master record the team does not execute directly. It holds standard summary text, description, subtasks, or labels for repeated processes.
- **Clone**: An action on a work item that duplicates fields and, optionally, subtasks into a new work item with a new key.
- **Internal task**: Work that does not deliver customer value (for example sprint housekeeping). The lesson uses work type **Task** rather than **Story** for this reason.
- **Subtask checklist**: Breaking template steps into subtasks gives assignable, trackable items that clone with the parent.

## How to do it in Jira

### Build a template work item

1. Open the *Stamps and Points* space and create a work item with work type **Task** (not Story).
2. Set **Summary** to something clearly marked as a template (for example `Template — Sprint planning checklist`).
3. Leave **Parent** empty unless the team groups admin work under a dedicated epic.
4. In **Description**, list recurring steps, for example:
   - Review carried-over items from the previous sprint
   - Groom top backlog items and confirm estimates
   - Ensure dependencies are visible
   - Align with product owner priorities
   - Prepare the board for planning
5. Add label `template` so the team can filter or avoid editing the master.
6. Create the work item. It appears in the backlog like any other task.

### Optional: convert steps to subtasks

1. Open the template work item.
2. For each checklist line, choose **Add** > **Subtask** and enter a short summary (for example `Review carried-over items`).
3. Save. Subtasks appear under the parent in the detail view and on the card when expanded.

### Clone the template for real use

1. Open the template work item.
2. Open **Actions** (**⋯** or **More**) and choose **Clone**.
3. Update **Summary** — remove words like `Template` or `Clone` and name the instance (for example `Sprint 1 planning checklist`).
4. Set **Assignee** and other fields for this sprint.
5. Enable **Include subtasks** (or equivalent) so checklist subtasks copy across.
6. Confirm **Create**. The new work item gets its own key; the template stays unchanged.

### Repeat each sprint

Clone the same template at the start of each sprint, rename, assign, and work through the subtasks or description checklist. Delete or close completed sprint copies; keep the template at the bottom of the backlog or filter it out with `labels = template`.

## Examples

The *Stamps and Points* team clones **Template — Sprint planning checklist** into **Sprint 1 planning checklist**, assigned to a scrum master, with six subtasks copied automatically. Customer-facing stories still use Story; the checklist Task never ships to users but keeps planning consistent.

To find all live checklist copies without the master template:

```sql
summary ~ "planning checklist" AND project = ABC AND labels != template
```

## Tips and pitfalls

- **Protect the master.** Use the `template` label and a clear summary prefix so nobody closes or edits the template thinking it is real sprint work.
- **Description vs subtasks.** Descriptions clone quickly and need no extra keys. Subtasks add assignees and status per step but multiply work items when cloned.
- **Clone is not automation.** Each sprint still needs a manual clone unless a later automation rule creates the checklist (covered in a later section).
- **Refresh if the board looks wrong.** Occasionally after refresh, card titles may render oddly; reloading the page usually clears it.

> [!TIP]
> For longer recurring processes (release checklist, onboarding a new shop), the same pattern works: one labeled template, clone with subtasks, rename per event.

## Review questions

<details>
<summary>Does Jira Cloud provide a built-in template gallery for work items?</summary>
No. The lesson uses a labeled master work item plus Clone as a practical workaround.
</details>

<details>
<summary>Why does the sprint planning example use Task instead of Story?</summary>
The checklist is internal team work with no direct customer value. Stories represent user-facing deliverables; tasks suit operational or process work.
</details>

<details>
<summary>What should you enable when cloning a template that has subtasks?</summary>
Include subtasks in the clone dialog so each checklist step copies to the new work item.
</details>

<details>
<summary>How does the team mark the master so it is not confused with active work?</summary>
Add a <code>template</code> label and use a summary prefix such as <code>Template —</code> so filters and naming make the master obvious.
</details>

<details>
<summary>What is the main benefit of subtasks over a description checklist in a template?</summary>
Each step becomes its own work item with assignee and status, so progress is visible on the board without splitting one description into manual tracking.
</details>

## Related

- [Glossary](../reference/glossary.md)
- [Create Work Items: Epics, Stories & Subtasks](../02-jira-fundamentals/03-create-epics-stories-subtasks.md)
- [Using Issue Labels and Priorities to Organize Work in Jira](01-labels-and-priorities.md)
- [What Can Be Automated in Jira by Non-Admins?](../09-automation/01-what-non-admins-can-automate.md)

---

Previous: [Planning and Releasing with Versions in Jira](03-versions-and-releases.md) · Next: [Section 4 Quiz](05-section-4-quiz.md)
