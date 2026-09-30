---
title: "Section 2 Quiz"
aliases:
  - "Section 2 Quiz"
type: quiz
section: 2
lesson: 7
duration: ""
status: done
tags:
  - jira
  - section/02
  - quiz
  - flashcards
---

# Section 2 Quiz

[Course home](../README.md) › [Section 2: Jira Fundamentals](README.md) › Quiz

> [!IMPORTANT]
> The official Udemy quiz questions are not reproduced here. The practice questions and flashcards below are original and cover the same topics.

## Topics covered

- [Team-Managed vs Company-Managed Spaces](01-team-managed-vs-company-managed-spaces.md)
- [Understanding Jira Work Types & Hierarchy](02-work-types-and-hierarchy.md)
- [Create Work Items: Epics, Stories & Subtasks](03-create-epics-stories-subtasks.md)
- [Parent-Child Hierarchy vs Linked Work Items](04-parent-child-vs-linked-work-items.md)
- [Understanding Jira Boards: Scrum, Kanban & Filters](05-boards-scrum-kanban-filters.md)
- [How Jira Is Structured: Spaces, Boards & Work Items](06-how-jira-is-structured.md)

## Practice questions

<details>
<summary>1. Your first Jira space was created automatically and you need to follow the course demos. What should you check first?</summary>
Whether the space is team-managed or company-managed. The course uses a company-managed Scrum space. If yours is team-managed, create a new company-managed space with a deliberate name and key.
</details>

<details>
<summary>2. A product owner asks for one story to roll up to two epics for reporting. Can Jira's hierarchy do that?</summary>
No. A story, task, or bug can have only one epic parent. Use a work item link such as relates to for a secondary association, or pick the primary epic.
</details>

<details>
<summary>3. You create epics but only see stories on the backlog. Where are the epics?</summary>
In the Epics panel. Epics are kept out of the main backlog list so they do not clutter sprint planning. Open the Epics panel from the backlog toolbar.
</details>

<details>
<summary>4. A story sits at the top of the backlog after drag-and-drop, but its Priority field is Medium. Is that a mistake?</summary>
Not necessarily. Priority and backlog rank are independent. Rank controls order in the backlog; priority is a separate field the team may use differently.
</details>

<details>
<summary>5. Subtask SP-15 Gather requirements must finish before SP-16 Create design starts. What should you create?</summary>
A work item link: SP-15 blocks SP-16. Parent-child hierarchy organizes epics and stories; links express sequencing dependencies.
</details>

<details>
<summary>6. A company-managed story in space SP needs an epic parent from another company-managed space. Is that allowed?</summary>
Yes. Parent-child hierarchy can cross company-managed spaces. The story stays in SP but rolls up to the external epic.
</details>

<details>
<summary>7. Can a company-managed story use a team-managed epic as its parent?</summary>
No. Parent-child hierarchy requires the same management type on both sides. Use work item links if you need a relationship across types.
</details>

<details>
<summary>8. You delete the SP Kanban board by accident. Are the work items gone?</summary>
No. Boards are views only. Work items belong to the space and remain on other boards and in search.
</details>

<details>
<summary>9. Your Scrum board opens to an empty Active sprints view. What is the most likely explanation?</summary>
No sprint has been started yet. Switch to Backlog to see epics and stories, then create a sprint when ready (covered in Section 3).
</details>

<details>
<summary>10. You want a Kanban board that shows only items linked to three specific epics. How was this done in the course demo?</summary>
Create a saved filter for those epics, then create the board with the Advanced option and select that filter as the board's query.
</details>

<details>
<summary>11. Where do subtasks appear in the backlog list?</summary>
Nested under their parent story, task, or bug. They do not appear as separate top-level backlog cards. Expand the parent or open its detail view.
</details>

<details>
<summary>12. You move a card to In Progress on the Kanban board. Will the Scrum board show the same status?</summary>
Yes. All boards display the same underlying work items. Status changes sync everywhere the item appears.
</details>

## Flashcards

Team-managed vs company-managed main difference?::Configuration and governance—team-managed lets the team configure locally; company-managed uses shared site-wide configuration
Why pick a space key carefully?::It prefixes every work item (e.g. SP-1); changing it later means editing every filter and gadget that uses the old key
Can a team-managed space be converted to company-managed?::Not in place; create a new space of the other type and bulk-move the work items
Default three-level hierarchy?::Epic → story/task/bug → subtask
Can a story have two epic parents?::No—one parent only in the hierarchy
Where do epics appear in the backlog?::In the Epics panel, not as main backlog cards
Priority vs backlog rank?::Priority is a field; rank is order by drag-and-drop in the backlog—they are independent
Work item key format?::Space key plus sequence number, e.g. SP-12; numbers are never reused
Two ways to assign a story to an epic?::Parent picker on the card, or drag the story onto the epic in the Epics panel
Do subtasks show as top-level backlog cards?::No—they nest under their parent work item
Parent-child vs work item link?::Hierarchy organizes epic/story/subtask levels; links express blocks, duplicates, relates to, etc.
Cross-space epic parent rule?::Allowed between company-managed spaces (or between team-managed), but not mixed management types
Can links cross team-managed and company-managed?::Yes—link types like blocks work across types and spaces
Do boards own work items?::No—items belong to spaces; boards are views
Delete a board—what happens to issues?::Nothing to the work items; only the view is removed
Scrum board main views?::Backlog and Active sprints
Kanban board main focus?::Status columns and continuous flow; optional separate backlog view
How to add Kanban backlog view?::Board settings → Columns → map a status (e.g. Open) to the Kanban backlog column
Why create a board from a saved filter?::To show a subset of work or combine items from multiple spaces
Can subtasks have subtasks?::No—subtasks are the bottom level; Add on a subtask creates links, not nested hierarchy
What does "blocks" link mean?::The source item must be completed before the blocked item can proceed (by team agreement)

## Easy to confuse

| Concept A | Concept B | How to tell them apart |
|---|---|---|
| Space | Board | A space holds work items. A board is a view that displays matching items; deleting a board does not delete work. |
| Parent-child hierarchy | Work item link | Hierarchy fixes levels (epic → story → subtask). Links add typed relationships (blocks, duplicates) without changing level. |
| Epic | Story | An epic groups many sprint-sized items over multiple sprints. A story is deliverable work that flows through the backlog and sprints. |
| Priority field | Backlog rank | Priority is a labeled field on the item. Rank is visual order from drag-and-drop; they can disagree. |
| Team-managed space | Company-managed space | Team-managed = local team config. Company-managed = shared workflows and fields across spaces. One parent-child chain can't mix the two types. |
| Scrum board | Kanban board | Scrum centers on backlog + sprints. Kanban centers on columns + flow, with an optional backlog column to configure. |

---

Previous: [How Jira Is Structured: Spaces, Boards & Work Items](06-how-jira-is-structured.md) · Next: [Section 3: Agile in Jira: Scrum and Kanban](../03-agile-scrum-and-kanban/README.md)
