---
title: "Section 3 Quiz"
aliases:
  - "Section 3 Quiz"
type: quiz
section: 3
lesson: 7
duration: ""
status: done
tags:
  - jira
  - section/03
  - quiz
  - flashcards
---

# Section 3 Quiz

[Course home](../README.md) › [Section 3: Agile in Jira: Scrum and Kanban](README.md) › Quiz

> [!IMPORTANT]
> The official Udemy quiz questions are not reproduced here. The practice questions and flashcards below are original and cover the same topics.

## Topics covered

- [Scrum Workflow in Jira: Sprints, Planning, and Execution](01-scrum-workflow-sprints.md)
- [Estimating with Story Points and Time in Agile Projects](02-estimating-story-points-and-time.md)
- [Running Daily Standups with Jira: Best Practices](03-daily-standups.md)
- [Working with Kanban: Managing Flow Over Time in Jira](04-kanban-managing-flow.md)
- [Visualizing Work with WIP Limits and Swimlanes in Jira](05-wip-limits-and-swimlanes.md)
- [Understanding the Cumulative Flow Diagram for Kanban Teams](06-cumulative-flow-diagram.md)

## Practice questions

<details>
<summary>1. Sprint 3 ends with four stories still In Progress. Where should those stories go, and why?</summary>
Move them to the top of the backlog, not directly into Sprint 4. Fresh sprint planning lets the team re-evaluate priorities and recommit instead of automatically carrying unfinished work forward.
</details>

<details>
<summary>2. Your team sizes stories with a Fibonacci scale. A colleague wants to estimate a story at 9 points because it feels "between 8 and 13." What should the team do?</summary>
Pick either 8 or 13. The scale uses discrete steps (1, 2, 3, 5, 8, 13, 20)—not values in between—because larger items carry more uncertainty.
</details>

<details>
<summary>3. During standup, the facilitator clicks one avatar and leaves it selected while the next person speaks. What problem does this cause?</summary>
The board still filters to the previous person's work items, hiding everyone else's cards. Clear the assignee filter before selecting the next speaker.
</details>

<details>
<summary>4. A developer moves a story to a new Testing status, but it vanishes from both the Kanban board and the Scrum sprint view. What is the most likely cause?</summary>
The Testing status is not mapped to a column on the board. Map the status to a column in Board settings under Layout, then Columns.
</details>

<details>
<summary>5. On a five-person Kanban team, what WIP max for In Progress does the course recommend as a starting point?</summary>
Three or four—below the team size—so people collaborate and finish items before starting too many at once.
</details>

<details>
<summary>6. The active sprint backlog shows 51 gray, 5 blue, and 8 green story points. What do those numbers mean?</summary>
51 points remain to do, 5 are in progress, and 8 are completed in the current sprint.
</details>

<details>
<summary>7. A Kanban board with a separate backlog looks empty. Where is the work, and how do items reach the board?</summary>
Work items sit in the backlog status. Select items in the Backlog view and move them to To Do when the team is ready to pull them onto the board.
</details>

<details>
<summary>8. On a cumulative flow diagram, the In Progress band has been widening for two weeks while Done stays flat. What should the team investigate?</summary>
A bottleneck or stall in that status—blocked work, insufficient capacity, or statuses not being updated. Items are accumulating faster than they leave In Progress.
</details>

<details>
<summary>9. After three sprints, the team consistently completes about 50 story points per sprint. How should they use this for Sprint 4 planning?</summary>
Plan roughly 50 story points of work—their velocity—rather than over-committing far above what history shows they finish.
</details>

<details>
<summary>10. During standup, the team wants blocked items visible in their own row. What board configuration achieves this?</summary>
Create a query swimlane with JQL such as labels = blocked in Board settings under Swimlanes, then set Group by to Queries on the board.
</details>

<details>
<summary>11. A column WIP max is 2 and the team moves a third item into that column. Can they still do it, and what signal appears?</summary>
Yes—Jira allows the move. The column header turns red as a warning that WIP exceeds the agreed limit.
</details>

<details>
<summary>12. What is the difference between a sprint goal and the list of stories in a sprint?</summary>
The sprint goal states the single most important outcome (for example, launch MVP). The story list is the specific work items the team commits to during planning—they support the goal but are not the same thing.
</details>

## Flashcards

What is a sprint?::A time-boxed iteration, usually two weeks, in which a Scrum team commits to a set of backlog work items
What happens to Done items when you complete a sprint?::They leave the active board view but remain searchable in Jira
Where should incomplete sprint items go at sprint end?::Top of the backlog, not automatically into the next sprint
What is a sprint goal?::A short statement of the most important outcome the team aims to deliver in the sprint
What are story points?::A relative sizing estimate combining effort, complexity, and uncertainty
What Fibonacci values are commonly used for story points?::1, 2, 3, 5, 8, 13, and sometimes 20
What is velocity?::The average story points a team completes per sprint, used to plan future capacity
What do gray, blue, and green point totals on the backlog mean?::Gray = to do, blue = in progress, green = completed in the active sprint
What suffixes does Original estimate accept?::h for hours, d for days, w for weeks (for example 75h or 15d)
How long should a daily standup be?::About 15 minutes
What does Start standup add to the board?::A timed panel that rotates through participants and alerts when time is up
What metric drives the Sprint insights burndown?::Story points
What is Kanban's main focus vs Scrum?::Continuous flow and pull-based delivery instead of time-boxed sprints
How does a Kanban backlog differ from a Scrum backlog?::Kanban backlog is a status column; Scrum backlog uses sprint planning buckets
What is a WIP limit?::A maximum number of work items allowed in a column at once
What happens when WIP max is exceeded?::The column header turns red; Jira still allows the move
Why must workflow statuses map to board columns?::Unmapped statuses make work items disappear from the board view
What is a swimlane?::A horizontal row grouping board cards by assignee, epic, query, or other rules
What JQL might define a blocked swimlane?::labels = blocked
What does a widening band on a CFD indicate?::Work accumulating in that status—a likely bottleneck or stall
Is the CFD shared across all boards?::No—each Kanban board has its own CFD based on its columns

## Easy to confuse

| Concept A | Concept B | How to tell them apart |
|---|---|---|
| Sprint goal | Sprint backlog | The goal is one outcome statement (launch MVP). The backlog is the list of work items committed for the sprint. |
| Story points | Original estimate | Story points are relative size on a Fibonacci scale. Original estimate is absolute time (hours, days, weeks). |
| Velocity | WIP limit | Velocity measures completed points per sprint for planning. WIP limit caps items in a column to improve flow. |
| Scrum backlog | Kanban backlog | Scrum backlog feeds sprint buckets. Kanban backlog is a status—items are pulled to To Do when ready. |
| WIP limit exceeded (red column) | Blocked label | Red column means too many items in one status. Blocked label marks a specific impediment on a work item. |
| Cumulative flow diagram | Sprint burndown | CFD stacks status counts over time on a Kanban board. Burndown tracks remaining story points across a Scrum sprint timeline. |

---

Previous: [Understanding the Cumulative Flow Diagram for Kanban Teams](06-cumulative-flow-diagram.md) · Next: [Section 4: Organizing Your Work](../04-organizing-work/README.md)
