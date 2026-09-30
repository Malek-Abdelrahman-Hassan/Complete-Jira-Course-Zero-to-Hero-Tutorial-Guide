---
title: "Agile in Jira: Mastering Scrum and Kanban Workflows"
short_title: "Agile in Jira: Scrum and Kanban"
aliases:
  - "Section 3 — Agile in Jira: Mastering Scrum and Kanban Workflows"
  - "Section 03 overview"
type: section
section: 3
tags:
  - jira
  - section/03
---

# Section 3 — Agile in Jira: Mastering Scrum and Kanban Workflows

[Course home](../README.md) · Previous: [Section 2: Jira Fundamentals](../02-jira-fundamentals/README.md) · Next: [Section 4: Organizing Your Work](../04-organizing-work/README.md)

## What you will learn

By the end of this section you should be able to:

- Plan, start, and complete a sprint in a Scrum space.
- Estimate work with story points and with time tracking.
- Run a daily standup from the board.
- Manage continuous flow on a Kanban board.
- Use WIP limits and swimlanes to make work visible.
- Read a cumulative flow diagram.

## Lessons

<!-- BEGIN generated: lessons -->

| # | Lesson | Type | Duration | Notes |
|---:|---|---|---:|---|
| 1 | [Scrum Workflow in Jira: Sprints, Planning, and Execution](01-scrum-workflow-sprints.md) | Video | 12:06 | Done |
| 2 | [Estimating with Story Points and Time in Agile Projects](02-estimating-story-points-and-time.md) | Video | 10:04 | Done |
| 3 | [Running Daily Standups with Jira: Best Practices](03-daily-standups.md) | Video | 6:11 | Done |
| 4 | [Working with Kanban: Managing Flow Over Time in Jira](04-kanban-managing-flow.md) | Video | 5:38 | Done |
| 5 | [Visualizing Work with WIP Limits and Swimlanes in Jira](05-wip-limits-and-swimlanes.md) | Video | 10:31 | Done |
| 6 | [Understanding the Cumulative Flow Diagram for Kanban Teams](06-cumulative-flow-diagram.md) | Video | 4:46 | Done |
| 7 | [Section 3 Quiz](07-section-3-quiz.md) | Quiz | — | Done |

**Video time:** 49:16 · **Notes completed:** 7 / 7

<!-- END generated: lessons -->

## Key takeaways

- **Scrum in Jira** follows a repeating cycle: prepare and prioritize the backlog, plan a sprint with dates and a goal, start it, move work across the board daily, then complete the sprint and send unfinished items to the **top of backlog** for fresh planning.
- **Story points** estimate relative size on a Fibonacci scale (1, 2, 3, 5, 8, 13, 20). Jira totals points on the sprint, tracks gray/blue/green progress during the sprint, and builds **velocity** over time for capacity planning.
- **Daily standups** use board filters (assignee, epic, label, quick filters), swimlane grouping, the **Start standup** timer, and **Sprint insights** burndown to keep the team aligned and surface blockers within ~15 minutes.
- **Kanban** replaces sprints with **continuous flow**: work is prioritized in a backlog status and pulled into **To Do** as capacity allows. The same filtering and swimlane tools apply; planning happens on the board rather than in sprint buckets.
- **WIP limits** cap items per column and highlight overload in red. **Status mapping** is essential—unmapped statuses make work items disappear from both Kanban and Scrum board views.
- **Swimlanes and card layout** (by assignee, epic, or JQL query such as `labels = blocked`) make bottlenecks and blocked work visible. Keep workflows to roughly four or five statuses so the board stays maintainable.
- The **cumulative flow diagram** stacks status bands over time on each Kanban board. Steady band widths mean healthy flow; a widening band signals a bottleneck worth investigating.

## Hands-on practice

Suggested exercises for a free Jira Cloud site (these are not part of the official course material):

1. On your Scrum space, filter the epic panel to two or three epics, move high-priority stories to the top of the backlog, estimate them with story points, plan a two-week sprint with a sprint goal, and start it.
2. During the sprint, move work items across columns, complete at least one story, and check the gray/blue/green story point totals on the backlog view.
3. Run a mock standup: group the board by assignee, use **Start standup** with a two-minute timer, and open **Sprint insights** to read the burndown.
4. Complete the sprint with some items still in progress. Move incomplete work to the **top of backlog** (not the next sprint) and plan Sprint 2 from scratch.
5. Create or open a Kanban space, pull a few items from backlog to **To Do**, and set WIP max limits of 2–3 on **In Progress**.
6. Add a workflow status (for example, **Testing**), map it to a new board column, and confirm work items in that status stay visible.
7. Create a query swimlane for `labels = blocked`, add the `blocked` label to a test story, and verify it appears in its own row.
8. Open **Reports** > **Cumulative flow diagram** on the Kanban board, select a date range, and note which status band is widest.

## References

- [Glossary](../reference/glossary.md)
- [Scrum vs Kanban](../reference/scrum-vs-kanban.md)
- [Reports and metrics](../reference/reports-and-metrics.md)
