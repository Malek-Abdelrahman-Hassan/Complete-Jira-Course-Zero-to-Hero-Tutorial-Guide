---
title: "Working Smart: Cross-Team Collaboration and Long-Term Projects"
short_title: "Cross-Team Collaboration"
aliases:
  - "Section 7 — Working Smart: Cross-Team Collaboration and Long-Term Projects"
  - "Section 07 overview"
type: section
section: 7
tags:
  - jira
  - section/07
---

# Section 7 — Working Smart: Cross-Team Collaboration and Long-Term Projects

[Course home](../README.md) · Previous: [Section 6: Projects, Boards, Workflows, and Statuses](../06-boards-and-workflows/README.md) · Next: [Section 8: Dashboards and Reports](../08-dashboards-and-reports/README.md)

## What you will learn

By the end of this section you should be able to:

- Apply good practices for work that spans several teams.
- Create shared boards that pull work from more than one space.
- Use roadmaps and timelines to visualize plans and dependencies.
- Handle teams whose workflows use different statuses.

## Lessons

<!-- BEGIN generated: lessons -->

| # | Lesson | Type | Duration | Notes |
|---:|---|---|---:|---|
| 1 | [Managing Cross-Team Work in Jira: Best Practices](01-managing-cross-team-work.md) | Video | 4:33 | Done |
| 2 | [Creating and Using Shared Boards for Team Collaboration](02-shared-boards.md) | Video | 7:35 | Done |
| 3 | [Roadmaps in Jira: Visualizing Plans and Dependencies](03-roadmaps-plans-and-dependencies.md) | Video | 6:25 | Done |
| 4 | [What to Do When Statuses Don't Match Across Teams](04-mismatched-statuses-across-teams.md) | Video | 5:32 | Done |
| 5 | [Section 7 Quiz](05-section-7-quiz.md) | Quiz | — | Done |

**Video time:** 24:05 · **Notes completed:** 5 / 5

<!-- END generated: lessons -->

## Key takeaways

- Cross-team coordination keeps each team in its own space and adds shared views — filters, boards, timelines, dashboards — instead of merging backlogs.
- Scope partner work with release versions, components, labels, or epics before writing JQL so filters stay precise (for example iOS component on ABC plus `SP app` label on XYZ).
- A shared board is created from a saved filter with OR sub-queries; share filter view access with the organization and restrict editors.
- Fix versions with the same name in different spaces are separate records; expect duplicate version names on cross-space views.
- Timeline (formerly *roadmap* in a space) shows sprint placement and dependencies; Timeline covers one space only, and planning across spaces uses Plans (Jira Premium and Enterprise), but single-space practice teaches the same skills.
- Creating dependencies on Timeline and assigning work to future sprints changes plan and scope — agree with the team before doing either.
- When workflows differ, unmapped statuses make cards disappear from shared boards and Scrum backlogs; map foreign statuses under **Board settings > Layout > Columns**.
- For cross-team searches and dashboards, use `statusCategory` so *In Progress*, *In Review*, and custom active statuses match regardless of workflow naming.
- Jira shows status; regular sync meetings and release handoffs still align goals between teams.

## Hands-on practice

Suggested exercises for a free Jira Cloud site (these are not part of the official course material):

1. Create two spaces (or use existing ones): a Scrum space `ABC` and a Kanban space `XYZ`. In `ABC`, add fix version `1.0.0`, an **iOS** component, and assign both to a few stories. In `XYZ`, create fix version `1.0.0` and label app-related items `SP app`.
2. Build and save a filter that ORs `(project = ABC AND fixVersion = "1.0.0" AND component = iOS)` with `(project = XYZ AND fixVersion = "1.0.0" AND labels = "SP app")`. Share view access with your organization; keep edit access private.
3. Create a Scrum or Kanban board from that filter using the advanced filter option. Confirm work items from both spaces appear.
4. In `XYZ`, transition a work item to a status that does not exist on `ABC`'s workflow (create one if needed, for example *In Review*). Observe it disappear from the shared board, then map the status under **Board settings > Layout > Columns**.
5. Extend the saved filter with `AND statusCategory = "In Progress"` wrapped around the OR block. Compare results to a filter that uses `status = "In Progress"` only.
6. On a single-space Scrum board, open **Timeline**, create a future sprint with start and end dates, and drag a *blocks* link between two stories. Note overlap warnings when both sit in the same sprint.

## References

- [Glossary](../reference/glossary.md)
- [Scrum vs Kanban](../reference/scrum-vs-kanban.md)
