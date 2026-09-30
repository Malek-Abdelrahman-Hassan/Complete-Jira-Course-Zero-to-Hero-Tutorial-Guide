---
title: "Customizing Your Jira Board View Without Admin Access"
aliases:
  - "Customizing Your Jira Board View Without Admin Access"
type: lesson
section: 6
lesson: 1
duration: "10:00"
status: done
tags:
  - jira
  - section/06
  - topic/boards
---

# Customizing Your Jira Board View Without Admin Access

[Course home](../README.md) › [Section 6: Projects, Boards, Workflows, and Statuses](README.md) › Lesson 1 · 10:00

## TL;DR

Board settings let anyone with **board administrator** rights shape how a Scrum or Kanban board looks and behaves—without being a Jira site admin. You can trim the space menu, adjust the board filter, set working days and estimation, map statuses to columns, add WIP limits and swimlanes, and tune card layout and quick filters. The most common surprise is **unmapped statuses**: work items in a status with no column vanish from both the board and the backlog until you map them.

## Key concepts

- **Board administrator**: A person who can open **Board settings** for a specific board. Board admins can be added by an existing board admin; this is separate from Jira site administration.
- **Board filter**: The saved JQL query that decides which work items (formerly *issues*) appear on the board. One filter can include work from multiple spaces (formerly *projects*).
- **Unmapped status**: A workflow status not assigned to any board column. Work items in that status disappear from the board—and from the Scrum backlog—until the status is mapped.
- **Column constraint (WIP limit)**: A maximum number of work items allowed in a column, based on issue count or issue count excluding subtasks. Exceeding the limit highlights the column but does not block the move.
- **Days in column**: A card-layout field that shows how many days a work item has stayed in its current status, displayed as dots along the bottom of the card.
- **Sub-filter (Kanban)**: An extra JQL clause on Kanban boards, often hiding work tied to released versions so completed releases do not clutter the board.
- **Completed-issues visibility (Kanban)**: How long done work items stay visible on the board—commonly two weeks, or everything if you choose to show all completed items.

## How to do it in Jira

### Trim the space menu and open board settings

1. Open the space and use the **More** (⋯) menu beside the space navigation tabs.
2. Uncheck views the team does not use—**Code**, **Releases**, **Forms**, **Pages**, **Shortcuts**, and similar items—to reduce clutter.
3. On the board, open **⋯** > **Board settings**.

### General settings

1. **Board name** — rename for clarity; it does not affect the underlying filter or work items.
2. **Administrators** — add board admins (for example, a teammate). Click outside the field to save; a confirmation appears when the role is assigned.
3. **Location** — controls which space the board appears under in the sidebar menu.
4. **Filter** — view or switch the saved filter, edit its JQL, and open **Details** to see included spaces, viewers, and edit permissions.
5. **Working days** — set the team time zone, regular working days, and one-off holidays for more accurate sprint-capacity planning.
6. **Estimation** — choose **Story points**, **Time estimate**, or **Issue count**. The course recommends story points. Time tracking can be enabled separately but adds overhead with limited planning value for most teams.
7. **Timeline** — a Gantt-style view for roadmap planning on boards whose filter covers a single space. It may be unavailable when the filter spans multiple spaces.

### Layout: columns, swimlanes, cards, and filters

1. Open **Layout** > **Columns**.
2. Check for **Unmapped statuses** at the top. Create a column for each unmapped status, assign the correct **status category** (To Do, In Progress, or Done), and map the status into that column.
3. Optionally set **Min** and **Max** WIP constraints per column (issue count, or issue count excluding subtasks).
4. Under **Swimlanes**, group rows by assignee, epic, query, or another rule. On the live board, use **Group by** to switch swimlane views.
5. Under **Card colors**, pick a field such as assignee and adjust individual colors if needed.
6. Under **Card layout**, add fields to cards. Settings are separate for **Backlog** and **Active sprints** on Scrum boards. Enable **Days in column** to surface stagnation.
7. Under **Quick filters**, review built-in filters and create new ones with JQL snippets the team uses often.

### Kanban-specific options

1. In **General settings**, review the **Sub-filter**—often a clause like unreleased versions only—so released work drops off the board automatically.
2. Set **Completed issues** visibility (for example, two weeks vs show everything).
3. In **Layout** > **Columns**, choose whether epics appear as cards or in an epic panel. Drag a status into the **Kanban backlog** column to recreate a backlog view if the board did not start with one.

## Examples

On the *Stamps and Points* Scrum board, a **Testing** status existed in the workflow but had no column. Any story moved to Testing vanished from both **Active sprints** and **Backlog** until a **Testing** column was created with category **In Progress** and the status mapped into it.

After mapping, WIP limits of 3 were set on **To Do** and **In Progress**, swimlanes were left off but card colors were set by assignee, and **Days in column** was enabled. A card showing three dots had sat in its current status for three days—a signal to discuss blockers.

On the Kanban board, the default sub-filter hides work from released versions. With **Show everything** for completed issues, the **Done** column quickly fills with old work items.

## Tips and pitfalls

- **Board admin is enough.** You do not need Jira site admin rights to configure columns, swimlanes, or card layout—only membership as a board administrator.
- **Lost work items? Check columns first.** An unmapped status is the first place to look when a card disappears after a status change.
- **Press Enter on WIP limits.** Typed limits sometimes fail to save until you confirm the field.
- **Card layout differs by view.** Backlog and active-sprint card fields are configured separately on Scrum boards; enable **Days in column** on both if you want the indicator everywhere.
- **Kanban backlog is optional.** Drag a status into the backlog column mapping to bring back a separate backlog tab when the team wants one.

> [!TIP]
> **Days in column** turns age-in-status into a visible signal. Many dots on one card mean the item has not moved for several days—worth a conversation in standup.

> [!WARNING]
> Choosing **Show everything** for completed Kanban issues keeps every done card on the board indefinitely. That is useful for audits but quickly clutters day-to-day flow.

## Review questions

<details>
<summary>Why would a work item disappear from both the Scrum board and the backlog after a status change?</summary>
Its status is not mapped to any board column. Unmapped statuses hide work items from the board and from the backlog until an admin maps the status in Board settings > Layout > Columns.
</details>

<details>
<summary>What is the difference between a board filter and a Kanban sub-filter?</summary>
The board filter defines which work items the board can show at all (often one or more spaces). The sub-filter is an extra JQL clause—commonly hiding released-version work—that further narrows what appears on a Kanban board.
</details>

<details>
<summary>Who can open Board settings and add another board administrator?</summary>
Anyone listed as a board administrator for that board. This does not require Jira site admin rights.
</details>

<details>
<summary>What does Days in column show on a card, and why is it useful?</summary>
It shows how many days the work item has been in its current status, as dots along the bottom of the card. Too many dots highlight stagnation so the team can unblock or finish the item.
</details>

<details>
<summary>Why might Timeline be unavailable in board settings?</summary>
Timeline is designed for single-space filters. If the board filter includes multiple spaces or a query that Timeline does not support, the option may be disabled or hidden.
</details>

## Related

- [Glossary](../reference/glossary.md)
- [Scrum vs Kanban](../reference/scrum-vs-kanban.md)
- [Understanding Jira Boards: Scrum, Kanban & Filters](../02-jira-fundamentals/05-boards-scrum-kanban-filters.md)
- [Visualizing Work with WIP Limits and Swimlanes in Jira](../03-agile-scrum-and-kanban/05-wip-limits-and-swimlanes.md)
- [Using Basic Search and Quick Filters in Jira](../05-filters-and-jql/01-basic-search-and-quick-filters.md)

---

Previous: [Section overview](README.md) · Next: [Workflow States and Transitions: What You Can See and Do](02-workflow-states-and-transitions.md)
