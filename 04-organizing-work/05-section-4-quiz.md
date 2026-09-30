---
title: "Section 4 Quiz"
aliases:
  - "Section 4 Quiz"
type: quiz
section: 4
lesson: 5
duration: ""
status: done
tags:
  - jira
  - section/04
  - quiz
  - flashcards
---

# Section 4 Quiz

[Course home](../README.md) › [Section 4: Organizing Your Work](README.md) › Quiz

> [!IMPORTANT]
> The official Udemy quiz questions are not reproduced here. The practice questions and flashcards below are original and cover the same topics.

## Topics covered

- [Using Issue Labels and Priorities to Organize Work in Jira](01-labels-and-priorities.md)
- [Structuring Work with Components in Jira Projects](02-components.md)
- [Planning and Releasing with Versions in Jira](03-versions-and-releases.md)
- [Creating Templates and Reusable Tasks for Efficiency](04-templates-and-reusable-tasks.md)

## Practice questions

<details>
<summary>1. Your team wants a "parking lot" for ideas that are not ready for a sprint, but the workflow has no Parking Lot status. What is a lightweight approach shown in the course?</summary>
Create a shared label (for example <code>wishlist</code> or <code>parking-lot</code>) and apply it to those work items. Use the label click or JQL to filter, and optionally add a board quick filter.
</details>

<details>
<summary>2. A product owner drags stories to reorder the backlog, then sets Priority to High on several items. The backlog order does not change. Why?</summary>
Backlog order comes from rank (drag-and-drop), not from the Priority field. Priority is a separate indicator and does not move cards up or down.
</details>

<details>
<summary>3. Two stories must appear under both the "Retention OKR" initiative and their normal epics, but each story can have only one epic parent. What field helps?</summary>
Labels. Multiple labels can tag cross-cutting themes while each story keeps a single epic parent.
</details>

<details>
<summary>4. On the Stamps and Points space, you need separate ownership for iOS and Android work with admin-controlled names. Labels already exist site-wide. Which feature fits better?</summary>
Components. They are defined in Space settings by an admin, stay within one space, and support a component lead and default assignee.
</details>

<details>
<summary>5. A developer opens the Component field on a work item and sees "No match is found." What must happen first?</summary>
A space admin must create components in Space settings (switch to Jira components if Compass is shown). Users cannot invent new component names from the work item alone.
</details>

<details>
<summary>6. You create a new Bug and select the iOS component first. The component's default assignee is the iOS lead. What often happens to Assignee?</summary>
The new work item is assigned to the component's default assignee (often the component lead) when that component is the first one selected at creation time.
</details>

<details>
<summary>7. An epic "Social activity" spans login in release 1.0, avatars in 1.1, and comments in 2.0. Which Jira fields represent the time-based slices?</summary>
Fix versions (versions). The epic is the theme; fix versions plan which release includes each piece of work.
</details>

<details>
<summary>8. You release version 1.0 but one story is still In Progress. What does Jira typically ask before completing the release?</summary>
Where to move unresolved work items (for example to version 2.0) or whether to leave them unresolved, plus an optional release date and release notes.
</details>

<details>
<summary>9. Where can you assign a fix version by dragging a backlog card without opening the work item?</summary>
On the Versions panel on the backlog (similar to the Epics panel): drag the work item onto the target version.
</details>

<details>
<summary>10. The team repeats the same six-step sprint planning checklist every sprint. Jira has no template library. What workflow does the course recommend?</summary>
Create one Task labeled <code>template</code> with the checklist in the description or as subtasks, then clone it each sprint with subtasks included and rename the copy (for example Sprint 2 planning checklist).
</details>

<details>
<summary>11. Why use work type Task instead of Story for a sprint planning checklist template?</summary>
The checklist is internal team process work with no direct customer value. Stories represent user-facing deliverables; tasks suit operational checklists.
</details>

<details>
<summary>12. Write JQL to list all work items in fix version 2.0 for space ABC that are not Done.</summary>
<code>project = ABC AND fixVersion = "2.0" AND status != Done</code>
</details>

## Flashcards

What is a Jira label?::A free-form tag on a work item; new names are created by typing and confirming in the Labels field
Who can create a label?::Anyone who can edit the work item
Do labels stay inside one space?::No; the same label name is available across the whole Jira site
How do you filter by a label from a work item?::Click the label; Jira runs a search and shows the JQL
What is backlog rank?::The order of work items in the backlog, changed by drag-and-drop
Does the Priority field change backlog rank?::No; rank and priority are separate
Default priority for new work items?::Usually Medium
What is a component?::A space-level category for grouping work, often by platform or subsystem
Who creates components?::Space admin in Space settings
Can a work item have multiple components?::Yes
What is a component lead?::The person responsible for work in that component
When does default assignee on a component apply?::Typically when the work item is created and that component is selected first
Labels vs components — scope?::Labels are site-wide; components belong to one space only
What is a fix version?::The target release a work item is planned to ship in
Other names for fix version?::Version, release version (UI varies)
What JQL field targets versions?::fixVersion
What is the Versions panel?::A backlog sidebar to filter by version or drag items onto a version
What happens when you release a version?::It is marked shipped; unresolved items can move elsewhere; release notes may be generated
Can one epic span multiple versions?::Yes; epics are themes, versions are time-based releases
Does Jira Cloud have built-in work item templates?::No; use a labeled master work item and Clone
How do you mark a template master?::Add the label `template` and a clear summary prefix such as "Template —"
Clone with subtasks?::Enable include subtasks so checklist steps copy to the new work item
Why Task not Story for internal checklists?::Tasks suit non-customer process work; stories are user-facing

## Easy to confuse

| Concept A | Concept B | How to tell them apart |
|---|---|---|
| Label | Component | Labels are invented on any work item and work site-wide. Components are admin-defined lists inside one space with optional lead and default assignee. |
| Label | Epic | An epic is a parent work item with one child link per story. Labels are tags; many labels per item, no parent-child relationship. |
| Priority | Backlog rank | Priority is a field (Highest … Lowest). Rank is list order from drag-and-drop; changing priority does not reorder the backlog. |
| Fix version | Epic | Fix version plans when work ships in a release. Epic groups work by feature theme; one epic often crosses several versions. |
| Version (unreleased) | Version (released) | Unreleased versions accept new assignments and show progress. Releasing marks the version shipped and triggers release-note and cleanup options. |
| Template master | Cloned checklist | The master stays labeled <code>template</code> and is not executed. Each clone is renamed and assigned for a specific sprint or event. |

---

Previous: [Creating Templates and Reusable Tasks for Efficiency](04-templates-and-reusable-tasks.md) · Next: [Section 5: Filters and JQL](../05-filters-and-jql/README.md)
