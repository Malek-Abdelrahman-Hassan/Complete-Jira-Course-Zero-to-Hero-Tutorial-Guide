---
title: "Organizing Your Work: Labels, Components, Versions, and Templates"
short_title: "Organizing Your Work"
aliases:
  - "Section 4 — Organizing Your Work: Labels, Components, Versions, and Templates"
  - "Section 04 overview"
type: section
section: 4
tags:
  - jira
  - section/04
---

# Section 4 — Organizing Your Work: Labels, Components, Versions, and Templates

[Course home](../README.md) · Previous: [Section 3: Agile in Jira: Scrum and Kanban](../03-agile-scrum-and-kanban/README.md) · Next: [Section 5: Filters and JQL](../05-filters-and-jql/README.md)

## What you will learn

By the end of this section you should be able to:

- Use labels and priorities consistently to organize work.
- Structure a space with components.
- Plan and ship work with versions (releases).
- Create templates and reusable tasks to avoid repetitive setup.

## Lessons

<!-- BEGIN generated: lessons -->

| # | Lesson | Type | Duration | Notes |
|---:|---|---|---:|---|
| 1 | [Using Issue Labels and Priorities to Organize Work in Jira](01-labels-and-priorities.md) | Video | 7:10 | Done |
| 2 | [Structuring Work with Components in Jira Projects](02-components.md) | Video | 6:40 | Done |
| 3 | [Planning and Releasing with Versions in Jira](03-versions-and-releases.md) | Video | 8:09 | Done |
| 4 | [Creating Templates and Reusable Tasks for Efficiency](04-templates-and-reusable-tasks.md) | Video | 6:04 | Done |
| 5 | [Section 4 Quiz](05-section-4-quiz.md) | Quiz | — | Done |

**Video time:** 28:03 · **Notes completed:** 5 / 5

<!-- END generated: lessons -->

## Key takeaways

- **Labels** are flexible, site-wide tags anyone can create. Agree on names with the team; they suit wishlists, OKRs, and cross-epic grouping when one epic parent is not enough.
- **Priority** is not backlog order. Drag-and-drop rank decides what is next; priority is an extra signal and works in quick filters and JQL.
- **Components** are space-specific, admin-controlled groupings (often platforms or modules) with optional component lead and default assignee.
- **Labels vs components**: labels are fast and global but hard to clean up; components add governance but require space settings access and stay in one space.
- **Fix versions** plan which release includes each work item. Use the Versions panel on the backlog like the Epics panel — filter, drag to assign, or set the field on the work item.
- **Releasing a version** marks it shipped, handles unresolved work, and can generate release notes. Progress toward a version appears in space settings.
- **Epics and versions complement each other**: epics group by theme; versions slice the same theme across releases over time.
- **Templates** are a clone-based pattern: one labeled master Task (often with subtasks), cloned each time a repeatable checklist is needed — Jira Cloud has no separate template store.

## Hands-on practice

Suggested exercises for a free Jira Cloud site (these are not part of the official course material):

1. On three backlog stories in *Stamps and Points*, add a shared label such as `wishlist`. Click the label, copy the JQL, and create a **Wishlist** quick filter on the board.
2. In **Space settings > Components**, create **iOS** and **Android** with different component leads. Assign components to several work items and add an **iOS** quick filter using `component = iOS`.
3. Open the **Versions** panel on the backlog. Create versions `1.0` and `2.0`, drag stories onto them, add **Fix versions** to card layout, then release `1.0` from space settings and move any open items to `2.0`.
4. Create a **Task** titled `Template — Sprint planning checklist` with label `template` and six subtasks. Clone it with subtasks included, rename the copy for your current sprint, assign it, and work through the checklist.
5. Compare **Priority = Highest** on one bug with backlog rank: reorder the backlog and confirm priority alone did not change position.

## References

- [Glossary](../reference/glossary.md)
