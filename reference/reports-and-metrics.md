---
title: "Reports and Metrics"
aliases:
  - "Reports and Metrics"
  - "Jira reports"
type: reference
tags:
  - jira
  - reference
  - topic/reports
---

# Reports and Metrics

[Course home](../README.md) · Section: [Dashboards and Reports](../08-dashboards-and-reports/README.md)

## Board reports

| Report | Board | Question it answers | How to read it |
|---|---|---|---|
| **Burndown chart** | Scrum | Is the sprint on track? | Remaining work against an ideal guideline. A flat line means no progress; an upward step means scope was added. |
| **Burnup chart** | Scrum | How does completed work compare with total scope? | Two lines, *scope* and *completed*. The gap between them is the work left. |
| **Sprint report** | Scrum | What was completed, what wasn't, and what changed mid-sprint? | Lists of completed and not-completed work, plus work added after the sprint started. |
| **Velocity chart** | Scrum | How much work does the team finish per sprint? | Commitment vs completed per sprint. Use the recent average for forecasting. |
| **Cumulative flow diagram** | Kanban and Scrum | Where is work piling up? | One band per status. A widening band shows a bottleneck; a flat top band shows nothing is being finished. |
| **Control chart** | Kanban and Scrum | How long does work take, and how predictable is it? | Each dot is a work item's cycle time, with average and rolling average lines. A tighter spread means more predictable delivery. |

> [!NOTE]
> The available reports depend on the board type and on whether the space is team-managed or company-managed. Company-managed spaces offer extra reports such as the epic report and version report.

## Dashboard gadgets for reporting

| Gadget | Useful for |
|---|---|
| Filter Results | A live list of work items from a saved filter |
| Pie Chart | Breaking work down by status, assignee, priority, and so on |
| Created vs. Resolved Chart | Whether the backlog is growing or shrinking |
| Two Dimensional Filter Statistics | A table of one field against another, for example status by assignee |
| Sprint Health / Sprint Burndown | Sprint progress on a dashboard |

## Key metrics

| Metric | Definition |
|---|---|
| **Velocity** | Work (usually story points) completed per sprint |
| **Cycle time** | Time from starting work to finishing it |
| **Lead time** | Time from the request (creation) to finishing it |
| **Throughput** | Number of work items finished per period |
| **Work in progress (WIP)** | Number of work items started but not finished |

## Notes from the course

### Scrum reports

From [Scrum Reports: Velocity, Burndown, and Sprint Report Explained](../08-dashboards-and-reports/04-scrum-reports.md). All of them are under **Reports** on the board.

| Report | What to look at | Warning sign |
|---|---|---|
| **Burndown chart** | The remaining-work line against the gray guideline, measured in story points, work item count, or original time estimate | The line stays flat or above the guideline; upward steps mean work was added or reopened |
| **Burnup chart** | Scope and completed lines | Scope keeps rising while completed stays flat |
| **Sprint report** | Completed and not-completed lists | Many work items marked with an asterisk, meaning they were added after the sprint started |
| **Velocity chart** | Gray (committed) vs green (completed) bars per sprint | Green consistently lower than gray (overcommitting) or higher (underplanning) |
| **Epic report** | Blue completed area inside the gray total scope, plus the brown unestimated line | Scope grows, the unestimated line climbs, and completion stays flat |

### Kanban reports

From [Kanban Reports: Control Chart and Cumulative Flow Diagram](../08-dashboards-and-reports/05-kanban-reports.md) and [Understanding the Cumulative Flow Diagram for Kanban Teams](../03-agile-scrum-and-kanban/06-cumulative-flow-diagram.md).

- **Control chart**: each dot is a work item's cycle time, with an average line and a band for variation. Narrow the view by timeframe, columns, swimlanes, or quick filters. Hover over outliers before drawing conclusions; a batch of old work items closed at once can make the average jump.
- **Cumulative flow diagram**: read band width, not height. A band that keeps widening shows work piling up in that status.
- **Use them together.** The CFD shows where work accumulates, and the control chart shows how long it takes.

### Dashboards

From [Creating Personal and Team Dashboards in Jira](../08-dashboards-and-reports/01-personal-and-team-dashboards.md), [Useful Gadgets for Your Jira Dashboard](../08-dashboards-and-reports/02-useful-dashboard-gadgets.md), and [Sharing and Cloning Dashboards with Stakeholders and Teams](../08-dashboards-and-reports/03-sharing-and-cloning-dashboards.md).

- **One saved filter behind several gadgets** keeps every chart on the same scope, such as one release across two spaces.
- **Workhorse gadgets**: Filter Results, Work item Statistics, Pie Chart, Created vs. Resolved Chart, and Two Dimensional Filter Statistics. Numbers in the statistics gadgets are clickable and open the matching work items.
- **Pick one format per question.** Work item Statistics and Pie Chart on the same field tell the same story.
- **Sharing**: set viewers and editors, and select **Add** for each person or group, or the permission isn't saved. Keep editors limited so a team dashboard isn't changed by accident.
- **Board Summary** gives a ready-made overview for each board without building a dashboard.
- **Copy dashboard** to reuse a layout with new permissions; use a wallboard for a team monitor.
