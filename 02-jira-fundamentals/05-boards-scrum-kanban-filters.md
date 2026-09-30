---
title: "Understanding Jira Boards: Scrum, Kanban & Filters"
aliases:
  - "Understanding Jira Boards: Scrum, Kanban & Filters"
type: lesson
section: 2
lesson: 5
duration: "7:48"
status: done
tags:
  - jira
  - section/02
  - topic/boards
  - topic/filters
---

# Understanding Jira Boards: Scrum, Kanban & Filters

[Course home](../README.md) › [Section 2: Jira Fundamentals](README.md) › Lesson 5 · 7:48

## TL;DR

Boards are **views** of work items, not containers. Work items belong to a **space**; boards decide which items to show and how columns are arranged. You can create many boards for the same space, and changes to a work item on one board appear everywhere. **Scrum** boards emphasize a **backlog** and **sprints**; **Kanban** boards emphasize **columns** and continuous flow. A board can include all items from one space or a subset defined by a **saved filter**, including items from multiple spaces.

## Key concepts

- **Board**: A visual representation of work items matching a filter. Creating, editing, or deleting a board does not create or delete work items.
- **Scrum board**: Has **Backlog** and **Active sprints** views. The backlog holds prioritized work; sprints are time-boxed subsets pulled from the backlog.
- **Kanban board**: Shows status **columns** (for example To Do, In Progress, Done). Work flows across columns without sprints by default.
- **Saved filter**: A stored JQL or UI query that defines which work items match. Boards can be built on a filter instead of "all items in this space."
- **Kanban backlog**: An optional second view on a Kanban board. Statuses mapped to the backlog column hold future work that is not yet on the main board.
- **Synchronized status**: Moving a card on any board updates the work item's status site-wide. All boards showing that item reflect the change.

## Scrum vs Kanban boards

| | Scrum board | Kanban board |
|---|---|---|
| Main views | Backlog + Active sprints | Status columns |
| Planning unit | Sprints | Continuous flow |
| Default empty state | Active sprints empty until a sprint starts | Columns may show To Do items immediately |
| Optional backlog column | Built into backlog view | Must be configured in board settings |
| Best when | Work is planned in iterations | Work is pulled continuously |

## How to do it in Jira

### Create a board from a space

1. Open the space (for example **Stamps and Points App**).
2. Find **Create board** (often a **+** near the board name or in the space menu). Exact placement varies by Jira version.
3. Choose **Kanban** or **Scrum**.
4. Name the board (for example *SP Kanban board* alongside the existing *SP Scrum board*).
5. Pick what to include:
   - **Space items** — all work items from the current space (simplest).
   - **Advanced** — base the board on a **saved filter** for finer control (for example only items linked to certain epics).
6. Select **Create**.

### See work on a Scrum board

1. Open the Scrum board and switch to **Backlog** if **Active sprints** is empty.
2. Enable the **Epics** panel to filter or inspect epic groupings.
3. When ready for iterative work, create a sprint from the backlog (covered in Section 3).

### Add a backlog view to a Kanban board

1. Open the Kanban board and go to **Board settings** (gear or **⋯** menu).
2. Open **Columns** (sometimes under **Layout**).
3. Assign a status such as **Open** to the **Kanban backlog** column so new items land off the main board.
4. Return to the board. Items in backlog statuses appear in the **Backlog** tab; items in **To Do** and beyond appear on the column view.
5. Drag items from backlog to **To Do** when the team is ready to start them.

### Verify cross-board updates

1. Move a work item to **In Progress** on the Kanban board.
2. Open the Scrum board backlog or active sprint view. The same item shows **In Progress** there as well.

## Examples

The demo space **SP** starts with an auto-created **SP Scrum board**. A second **SP Kanban board** is built with the **Advanced** option and a saved filter called *first three epics*, so only work linked to selected epics appears.

Workflow statuses in the demo include **Open**, **To Do**, **In Progress**, and **Done**:

- **Open** — newly created, not yet prioritized (Kanban backlog).
- **To Do** — ready to start; appears on the Kanban column board.
- **In Progress** / **Done** — active and completed work.

A board spanning multiple spaces might use a filter such as:

```sql
project in (ABC, XYZ) AND status != Done
```

That board shows matching items from spaces ABC and XYZ even though it was created from one space.

## Tips and pitfalls

- **Boards do not own work items.** Deleting a board is safe for the underlying data; only the view disappears.
- **Expect to land on Active sprints.** Many spaces open the sprint view by default. An empty sprint view is normal before the first sprint.
- **Filters unlock multi-space boards.** "All items from this space" is easy, but saved filters let one board serve a program or cross-team slice.
- **Kanban backlog is optional.** Without configuring backlog columns, new items may appear directly on the Kanban board.
- **Interface labels move.** **Create board** may appear as **+** or under a space menu; search board settings if the layout differs.

> [!NOTE]
> Section 3 goes deeper into running Scrum sprints and Kanban flow. This lesson establishes what boards are and how they relate to spaces, filters, and work items.

## Review questions

<details>
<summary>Do work items belong to boards or to spaces?</summary>
Work items belong to spaces. Boards are views that display items matching their configuration or filter.
</details>

<details>
<summary>What happens if you delete a board?</summary>
Nothing happens to the work items or the space. Only the visual board view is removed.
</details>

<details>
<summary>What is the main structural difference between Scrum and Kanban boards?</summary>
Scrum boards center on a backlog and sprints. Kanban boards center on status columns and continuous flow, with an optional separate backlog view.
</details>

<details>
<summary>Why use the Advanced option when creating a board?</summary>
It lets you base the board on a saved filter so you can show a subset of items or combine work from multiple spaces instead of all items from one space.
</details>

<details>
<summary>If you move a card on one board, do other boards update?</summary>
Yes. Boards display the same underlying work items. Changing status on one board updates the item everywhere it appears.
</details>

## Related

- [Glossary](../reference/glossary.md)
- [Scrum vs Kanban](../reference/scrum-vs-kanban.md)
- [JQL Cheat Sheet](../reference/jql-cheat-sheet.md)
- [Scrum Workflow in Jira: Sprints, Planning, and Execution](../03-agile-scrum-and-kanban/01-scrum-workflow-sprints.md)
- [Creating and Saving Filters in Jira for Quick Access](../05-filters-and-jql/02-creating-and-saving-filters.md)

---

Previous: [Parent-Child Hierarchy vs Linked Work Items](04-parent-child-vs-linked-work-items.md) · Next: [How Jira Is Structured: Spaces, Boards & Work Items](06-how-jira-is-structured.md)
