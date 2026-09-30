---
title: "Working with Kanban: Managing Flow Over Time in Jira"
aliases:
  - "Working with Kanban: Managing Flow Over Time in Jira"
type: lesson
section: 3
lesson: 4
duration: "5:38"
status: done
tags:
  - jira
  - section/03
  - topic/kanban
---

# Working with Kanban: Managing Flow Over Time in Jira

[Course home](../README.md) › [Section 3: Agile in Jira: Scrum and Kanban](README.md) › Lesson 4 · 5:38

## TL;DR

Kanban emphasizes **continuous flow** instead of time-boxed sprints. Work is pulled from a prioritized **To Do** column through **In Progress** to **Done**, with ongoing monitoring and improvement. A Kanban board in Jira works much like a Scrum board for day-to-day moves, but the backlog is a status column rather than a sprint bucket. Teams choose which backlog items to pull onto the board when a separate backlog is enabled.

## Key concepts

- **Kanban**: An Agile approach focused on continuous delivery and flow rather than fixed iterations. Work is prioritized in a queue and pulled as capacity allows.
- **Flow**: The movement of work items through workflow statuses. Kanban teams watch for stalls, bottlenecks, and smooth throughput over time.
- **Kanban board**: A board whose columns represent workflow statuses. The framework name comes from the Japanese word for "signboard"—originally a physical board with cards moved left to right.
- **Backlog as status**: On a Kanban board with a backlog enabled, items sit in a backlog status until the team deliberately moves them to **To Do**. Without a backlog, all matching work items appear on the board immediately.
- **Board filter**: Kanban boards are built on a saved filter, so the board may show only a subset of a space's work items and epics.

## Scrum vs Kanban in Jira

| Aspect | Scrum board | Kanban board |
|---|---|---|
| Planning unit | Sprint (time-boxed) | Continuous pull from To Do |
| Backlog view | Sprint buckets + ordered backlog | Status-based queue |
| Primary focus | Sprint commitment and velocity | Flow and WIP control |
| Board interaction | Heavy backlog/sprint planning | More time on the board itself |

## How to do it in Jira

1. Open the **Kanban board** for your space.
2. If the board uses a **separate backlog**, open **Backlog** from the board menu. Select work items and move them to **To Do** when the team is ready to start them.
3. On the board, drag cards across columns (**To Do** → **In Progress** → **Done**, plus any mapped statuses).
4. Use the same filtering tools as on a Scrum board: **Epics** panel, **Labels**, assignee avatars, and **Quick filters**.
5. **Group into swimlanes** via the board menu (by assignee, epic, or other options). Set **Group by: None** for a flat view.
6. Adjust epic display: **⋯** > **Board settings** > **Layout** > **Columns**. Under epic display, choose **Display epics as cards on the board** or **Display in epic panel** (same pattern as the Scrum board).
7. Return to the board and toggle the **Epics** panel if you switched to panel mode.

## Examples

The *Stamps and Points* Kanban board includes a backlog. The team selects a handful of stories—*Create user account*, *Sign up with Google*, and *Manage business profile*—and moves them from backlog to **To Do**. As developers finish one item, they pull the next highest-priority card from **To Do**.

Because the board filter limits what appears, not every epic from the space shows in the epic panel—only epics tied to work items the filter includes.

```sql
project = ABC AND status = "To Do" ORDER BY rank ASC
```

## Tips and pitfalls

- **Pull deliberately from backlog.** Moving items to **To Do** should reflect team agreement on priority—not every open work item belongs on the board at once.
- **Scrum and Kanban boards share most controls.** Filtering, swimlanes, and epic panels work the same way; the main difference is sprint-based versus continuous planning.
- **Remember the board filter.** If an epic or work item seems missing, it may fall outside the board's saved filter scope.
- **Kanban needs ongoing board updates.** Flow metrics and WIP limits only help when statuses stay current.

> [!NOTE]
> The Kanban framework literally means "board." In Jira, the digital board replaces the physical card wall while keeping the same pull-based idea.

## Review questions

<details>
<summary>What is the main difference between Scrum and Kanban regarding time?</summary>
Scrum uses fixed-length sprints with planned commitments. Kanban uses continuous flow without sprint boundaries—work is pulled as capacity allows.
</details>

<details>
<summary>Why might a Kanban board look empty until you visit the backlog?</summary>
When a separate backlog is enabled, work items stay in the backlog status until the team moves them to To Do on the board.
</details>

<details>
<summary>How does the Kanban backlog differ from the Scrum backlog view?</summary>
The Kanban backlog is a workflow status column, not a sprint planning bucket. There are no sprint containers—items queue until pulled.
</details>

<details>
<summary>Where do you change whether epics appear as cards or in a side panel?</summary>
Board settings, under Layout, then Columns—look for the epic display option.
</details>

<details>
<summary>Why might fewer epics appear on a Kanban board than in the space overall?</summary>
The board is scoped by a saved filter, so only work items (and their epics) matching that filter are visible.
</details>

## Related

- [Glossary](../reference/glossary.md)
- [Scrum vs Kanban](../reference/scrum-vs-kanban.md)
- [Understanding Jira Boards: Scrum, Kanban & Filters](../02-jira-fundamentals/05-boards-scrum-kanban-filters.md)
- [Scrum Workflow in Jira: Sprints, Planning, and Execution](01-scrum-workflow-sprints.md)
- [Visualizing Work with WIP Limits and Swimlanes in Jira](05-wip-limits-and-swimlanes.md)

---

Previous: [Running Daily Standups with Jira: Best Practices](03-daily-standups.md) · Next: [Visualizing Work with WIP Limits and Swimlanes in Jira](05-wip-limits-and-swimlanes.md)
