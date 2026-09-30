---
title: "Visualizing Work with WIP Limits and Swimlanes in Jira"
aliases:
  - "Visualizing Work with WIP Limits and Swimlanes in Jira"
type: lesson
section: 3
lesson: 5
duration: "10:31"
status: done
tags:
  - jira
  - section/03
  - topic/kanban
  - topic/boards
---

# Visualizing Work with WIP Limits and Swimlanes in Jira

[Course home](../README.md) › [Section 3: Agile in Jira: Scrum and Kanban](README.md) › Lesson 5 · 10:31

## TL;DR

Kanban relies on **work visualization**—making every item, bottleneck, and problem visible on the board. **WIP limits** cap how many work items may sit in a column at once, surfacing overload with a red highlight. **Swimlanes** split the board horizontally by assignee, epic, query, or other rules. **Status mapping** ties workflow statuses to columns; an unmapped status makes work items vanish from the board. These settings apply to both Kanban and Scrum boards.

## Key concepts

- **Work visualization**: Showing all relevant work and its state on the board so the team spots delays and bottlenecks immediately.
- **WIP limit (work in progress limit)**: A maximum (and optionally minimum) number of work items allowed in a column. Limiting WIP helps items finish faster even if total calendar time is similar.
- **Status mapping**: The link between a workflow status and a board column. Every status the team uses must map to a column or the item disappears from the board.
- **Swimlane**: A horizontal row on the board that groups work items—by assignee, epic, JQL query, or other criteria.
- **Query swimlane**: A swimlane driven by a filter such as `labels = blocked`, separating matching items into their own row.
- **Card layout**: Controls which fields (for example, story points) appear on board cards.

## How to do it in Jira

### Set WIP limits and map statuses

1. On the board, open **⋯** > **Board settings** > **Layout** > **Columns**.
2. For each column, set **Min** and **Max** WIP values. Teams usually focus on **Max**. A common guideline: set max below team size (for example, 3–4 for a five-person team) to encourage collaboration.
3. To add a column for a new workflow status (for example, **Testing**): click **Create column**, name it, drag it after **In Progress**, and map the **Testing** status into that column.
4. Press **Enter** after typing a WIP number—limits sometimes fail to save without confirmation.
5. Return to the board. When items exceed the max, the column header turns **red**. Jira still allows the move, but the highlight is a signal to finish or swarm on work before starting more.

### Configure swimlanes and cards

1. In **Board settings** > **Layout** > **Swimlanes**, choose a default grouping: none, queries, stories, assignees, epics, or projects.
2. For **Queries**, define swimlanes with JQL—for example, `labels = blocked` for a blocked row and a catch-all for everything else.
3. On the live board, use the **Group by** menu to switch swimlane views. Query-based lanes require **Group by: Queries** to appear.
4. Under **Layout**, explore **Card colors** (by priority or assignee), **Card layout** (add fields like **Story points** to cards), and epic display options.

### Remove a separate backlog (optional)

Map the **Open** status into the **To Do** column if you want every open item on the board at once. The separate backlog menu entry disappears when no backlog status remains.

## Examples

On the *Stamps and Points* Kanban board, **In Progress** and **Testing** each get a WIP max of **2**. Moving a third item into **In Progress** turns the column red.

A **Testing** status was added to the workflow but initially unmapped—work items moved to Testing vanished from the board until a **Testing** column was created and the status mapped to it.

A query swimlane with `labels = blocked` separates blocked stories into their own row. Story point values (2, 8, 3) appear on cards after adding the field in card layout settings.

```sql
project = ABC AND labels = blocked AND status != Done
```

## Tips and pitfalls

- **Unmapped statuses hide work items.** This is one of the most common reasons cards "disappear" from Scrum and Kanban boards—always map new workflow statuses to columns.
- **Keep workflows simple.** Four or five statuses are usually enough. Too many columns discourage daily updates, defeating the purpose of the board.
- **Set WIP limits with the whole team.** Limits should reflect agreed capacity, not one person's preference.
- **WIP red means "pay attention," not "blocked by Jira."** The board still accepts the move when the team deliberately exceeds a limit.

> [!IMPORTANT]
> Board layout settings—including WIP limits, swimlanes, and column mapping—apply to the Scrum board's active sprint view as well as Kanban boards.

> [!TIP]
> If WIP limits do not appear after saving, reopen **Board settings** > **Columns**, re-enter the value, and press **Enter** explicitly.

## Review questions

<details>
<summary>Why does limiting work in progress help a Kanban team?</summary>
Finishing fewer items at once means each item moves to Done faster. Total elapsed time may be similar, but delivery happens in smaller, more frequent increments.
</details>

<details>
<summary>What happens when a work item is moved to a status that is not mapped to any column?</summary>
It disappears from the board (and from the Scrum backlog view). The work item still exists and can be found via search—it is not deleted.
</details>

<details>
<summary>What visual signal appears when a column exceeds its WIP max?</summary>
The column header highlights in red. Jira still allows the transition, but the team should treat it as a warning.
</details>

<details>
<summary>How do you create a swimlane for blocked work items?</summary>
In Board settings under Swimlanes, add a query swimlane with JQL such as labels = blocked, then set Group by to Queries on the board.
</details>

<details>
<summary>What WIP max does the lesson suggest for a five-person team?</summary>
Around three or four—less than the number of team members—to encourage pairing and reduce parallel bottlenecks.
</details>

## Related

- [Glossary](../reference/glossary.md)
- [Scrum vs Kanban](../reference/scrum-vs-kanban.md)
- [Working with Kanban: Managing Flow Over Time in Jira](04-kanban-managing-flow.md)
- [Understanding the Cumulative Flow Diagram for Kanban Teams](06-cumulative-flow-diagram.md)
- [Workflow States and Transitions: What You Can See and Do](../06-boards-and-workflows/02-workflow-states-and-transitions.md)

---

Previous: [Working with Kanban: Managing Flow Over Time in Jira](04-kanban-managing-flow.md) · Next: [Understanding the Cumulative Flow Diagram for Kanban Teams](06-cumulative-flow-diagram.md)
