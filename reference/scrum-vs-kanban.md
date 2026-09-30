---
title: "Scrum vs Kanban"
aliases:
  - "Scrum vs Kanban"
type: reference
tags:
  - jira
  - reference
  - topic/scrum
  - topic/kanban
---

# Scrum vs Kanban

[Course home](../README.md) · Section: [Agile in Jira: Scrum and Kanban](../03-agile-scrum-and-kanban/README.md)

## Side by side

| | Scrum | Kanban |
|---|---|---|
| **Cadence** | Fixed-length sprints, usually 1-4 weeks | Continuous flow, no iterations |
| **Planning** | Sprint planning at the start of each sprint | Just in time: pull new work when there is capacity |
| **Roles** | Product Owner, Scrum Master, Developers | No prescribed roles |
| **Changing scope** | Avoid changing the sprint once it starts | New work can arrive at any time, within WIP limits |
| **Main constraint** | What fits in the sprint (capacity) | WIP limits per column |
| **Key metrics** | Velocity, sprint burndown | Cycle time, lead time, throughput |
| **Jira board** | Shows the active sprint; planning happens in the backlog | Shows all work in the flow; the backlog is optional |
| **Jira reports** | Burndown chart, burnup chart, sprint report, velocity chart | Control chart, cumulative flow diagram |
| **Good fit** | Product work delivered in planned increments | Support, operations, maintenance, and unpredictable incoming work |

## Scrum in Jira

1. Build and order the **backlog**; estimate work items, for example in story points.
2. **Plan the sprint:** create a sprint, drag work into it, and set a sprint goal.
3. **Start the sprint** with a name, duration, and goal.
4. Run **daily standups** from the board and keep statuses up to date.
5. **Complete the sprint:** unfinished work moves to the backlog or to the next sprint.
6. Review the **sprint report** and **velocity chart** in the retrospective.

## Kanban in Jira

1. Map each **board column** to one or more workflow statuses.
2. Set **WIP limits** on columns to prevent overload.
3. Use **swimlanes** (for example for expedited work or by assignee) to make priorities visible.
4. **Pull** the next work item only when a column has capacity.
5. Watch the **cumulative flow diagram** and **control chart** to spot bottlenecks and improve flow.

> [!TIP]
> Many teams mix the two approaches, for example Kanban-style WIP limits inside Scrum sprints. Jira supports this: a Scrum board also has column limits, a cumulative flow diagram, and a control chart.

## Notes from the course

### Scrum

- **Sprints of about two weeks** with a one-line **sprint goal**, such as launching the app's first version. See [Scrum Workflow in Jira](../03-agile-scrum-and-kanban/01-scrum-workflow-sprints.md).
- **Unfinished work goes back to the top of the backlog** when a sprint completes, rather than straight into the next sprint, so the next planning session starts from a fresh decision.
- **Story points** use the scale 1, 2, 3, 5, 8, 13, 20, compared against a baseline story. During a sprint, the backlog shows point totals in gray (to do), blue (in progress), and green (done). See [Estimating with Story Points and Time in Agile Projects](../03-agile-scrum-and-kanban/02-estimating-story-points-and-time.md).
- **Standups run from the board.** Quick filters or swimlanes by assignee let each person walk through their work items, **Start standup** keeps time, and **Sprint insights** shows sprint health. See [Running Daily Standups with Jira](../03-agile-scrum-and-kanban/03-daily-standups.md).

### Kanban

- **No sprints; work flows continuously.** A Kanban board shows whatever its board filter returns, and the Kanban backlog is optional: it appears when a status is mapped to the backlog column. See [Working with Kanban](../03-agile-scrum-and-kanban/04-kanban-managing-flow.md).
- **WIP limits** are set per column in **Board settings > Columns**, and the value may need **Enter** to save. A column over its maximum turns red as a warning, but Jira still allows the move. A maximum below the team size (for example 3-4 for five people) encourages finishing over starting. See [Visualizing Work with WIP Limits and Swimlanes in Jira](../03-agile-scrum-and-kanban/05-wip-limits-and-swimlanes.md).
- **Map every status to a column.** A status that isn't mapped makes its work items disappear from the board.
- **Keep the workflow small.** Four or five statuses are usually enough; too many columns discourage updates.
- **Watch the cumulative flow diagram.** Bands that keep the same width mean steady flow, and a widening band points to a bottleneck. See [Understanding the Cumulative Flow Diagram for Kanban Teams](../03-agile-scrum-and-kanban/06-cumulative-flow-diagram.md).

### Both

- WIP limits, swimlanes, card layout, the cumulative flow diagram, and the control chart are available on Scrum boards too.
