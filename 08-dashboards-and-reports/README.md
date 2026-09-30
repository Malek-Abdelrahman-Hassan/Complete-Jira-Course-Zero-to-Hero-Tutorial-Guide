---
title: "Dashboards and Reports: Tracking Progress and Performance"
short_title: "Dashboards and Reports"
aliases:
  - "Section 8 — Dashboards and Reports: Tracking Progress and Performance"
  - "Section 08 overview"
type: section
section: 8
tags:
  - jira
  - section/08
---

# Section 8 — Dashboards and Reports: Tracking Progress and Performance

[Course home](../README.md) · Previous: [Section 7: Cross-Team Collaboration](../07-cross-team-collaboration/README.md) · Next: [Section 9: Jira Automation](../09-automation/README.md)

## What you will learn

By the end of this section you should be able to:

- Create personal and team dashboards.
- Choose useful gadgets: filter results, charts, and more.
- Share and copy dashboards for stakeholders and teams.
- Interpret Scrum reports: velocity chart, burndown chart, and sprint report.
- Interpret Kanban reports: control chart and cumulative flow diagram.

## Lessons

<!-- BEGIN generated: lessons -->

| # | Lesson | Type | Duration | Notes |
|---:|---|---|---:|---|
| 1 | [Creating Personal and Team Dashboards in Jira](01-personal-and-team-dashboards.md) | Video | 4:37 | Done |
| 2 | [Useful Gadgets for Your Jira Dashboard: Filters, Charts, and More](02-useful-dashboard-gadgets.md) | Video | 6:31 | Done |
| 3 | [Sharing and Cloning Dashboards with Stakeholders and Teams](03-sharing-and-cloning-dashboards.md) | Video | 2:51 | Done |
| 4 | [Scrum Reports: Velocity, Burndown, and Sprint Report Explained](04-scrum-reports.md) | Video | 10:36 | Done |
| 5 | [Kanban Reports: Control Chart and Cumulative Flow Diagram](05-kanban-reports.md) | Video | 6:45 | Done |
| 6 | [Section 8 Quiz](06-section-8-quiz.md) | Quiz | — | Done |

**Video time:** 31:20 · **Notes completed:** 6 / 6

<!-- END generated: lessons -->

## Key takeaways

- **Dashboards** combine **gadgets** on a layout you choose; most reporting gadgets need a **saved filter** as their data source.
- Every board already has a **Summary** view; custom dashboards let you mix filters, charts, and lists for a specific audience.
- **Filter Results**, **Work item Statistics**, **Pie Chart**, **Created vs. Resolved Chart**, and **Two Dimensional Filter Statistics** are the workhorse gadgets—click counts to drill into JQL.
- Share **dashboards and filters** together; set **viewers** and **editors** separately, and click **Add** when granting access. **Copy dashboard** to reuse a layout for a new release or team.
- **Board reports** (under **Reports** on a board) are auto-generated—burndown, sprint report, and velocity for Scrum; control chart and CFD for flow.
- **Burndown** compares remaining work to an ideal line during one sprint; **sprint report** supports review with completed, incomplete, and mid-sprint additions.
- **Velocity chart** compares committed versus completed work across sprints to spot over- or under-planning.
- **Control chart** tracks **cycle time** and variation; investigate outlier dots before changing process. **CFD** shows bottlenecks by widening status bands.

## Hands-on practice

Suggested exercises for a free Jira Cloud site (these are not part of the official course material):

1. Save a filter for your ABC space (for example all open stories), then create a three-column dashboard with **Filter Results**, **Work item Statistics** by status, and **Pie Chart** by assignee—all using that filter.
2. Share the dashboard with your organization as viewers but keep yourself as the only editor. Confirm a colleague can open it only after the filter is shared too.
3. Copy the dashboard, rename it for a second filter, and swap gadget configurations without touching the original.
4. Complete at least two sprints on a Scrum board, then open **Burndown**, **Sprint report**, and **Velocity chart**. Write one sentence each on what the charts say about planning accuracy.
5. On a Kanban board, open **Control chart** and **Cumulative flow diagram** for the past two weeks. Note one widening CFD band and the control chart average cycle time.

## References

- [Glossary](../reference/glossary.md)
- [Reports and metrics](../reference/reports-and-metrics.md)
- [Scrum vs Kanban](../reference/scrum-vs-kanban.md)
