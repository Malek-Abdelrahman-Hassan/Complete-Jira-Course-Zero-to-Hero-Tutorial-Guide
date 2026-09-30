---
title: "Jira Fundamentals: Projects, Issues, Epics, and Boards"
short_title: "Jira Fundamentals"
aliases:
  - "Section 2 — Jira Fundamentals: Projects, Issues, Epics, and Boards"
  - "Section 02 overview"
type: section
section: 2
tags:
  - jira
  - section/02
---

# Section 2 — Jira Fundamentals: Projects, Issues, Epics, and Boards

[Course home](../README.md) · Previous: [Section 1: Introduction](../01-introduction/README.md) · Next: [Section 3: Agile in Jira: Scrum and Kanban](../03-agile-scrum-and-kanban/README.md)

## What you will learn

By the end of this section you should be able to:

- Compare team-managed and company-managed spaces and choose the right one.
- Explain Jira's work types and the default hierarchy (epic, then story/task/bug, then subtask).
- Create epics, stories, and subtasks.
- Tell the difference between a parent-child relationship and a work item link.
- Explain Scrum and Kanban boards and how a board uses a filter to decide what it shows.
- Describe how sites, spaces, boards, and work items fit together.

## Lessons

<!-- BEGIN generated: lessons -->

| # | Lesson | Type | Duration | Notes |
|---:|---|---|---:|---|
| 1 | [Team-Managed vs Company-Managed Spaces](01-team-managed-vs-company-managed-spaces.md) | Video | 5:15 | Done |
| 2 | [Understanding Jira Work Types & Hierarchy](02-work-types-and-hierarchy.md) | Video | 7:09 | Done |
| 3 | [Create Work Items: Epics, Stories & Subtasks](03-create-epics-stories-subtasks.md) | Video | 21:23 | Done |
| 4 | [Parent-Child Hierarchy vs Linked Work Items](04-parent-child-vs-linked-work-items.md) | Video | 7:52 | Done |
| 5 | [Understanding Jira Boards: Scrum, Kanban & Filters](05-boards-scrum-kanban-filters.md) | Video | 7:48 | Done |
| 6 | [How Jira Is Structured: Spaces, Boards & Work Items](06-how-jira-is-structured.md) | Video | 4:00 | Done |
| 7 | [Section 2 Quiz](07-section-2-quiz.md) | Quiz | — | Done |

**Video time:** 53:27 · **Notes completed:** 7 / 7

<!-- END generated: lessons -->

## Key takeaways

- A Jira **site** contains **spaces** (formerly *projects*); each space has a **key** that prefixes every work item, such as `SP-1`.
- **Team-managed** spaces give the team local control; **company-managed** spaces use shared configuration. The course demos use company-managed for consistency with larger organizations.
- Default **hierarchy** is epic → story/task/bug → subtask. One parent per child; epics live in the **Epics** panel, not the main backlog list.
- **Priority** and backlog **rank** are different: rank (drag-and-drop order) drives what the team pulls next; priority is an optional field.
- **Parent-child** organizes work within matching management types; **links** (blocks, relates to, duplicates) connect any work items across spaces and types.
- **Boards** are views, not containers—work items belong to spaces. Scrum boards use backlog and sprints; Kanban boards use columns and optional backlog configuration.
- Status changes on any board update the underlying work item everywhere it appears.

## Hands-on practice

Suggested exercises for a free Jira Cloud site (these are not part of the official course material):

1. Create a **company-managed** Scrum space named for a practice app (for example *Stamps and Points App*) with a short, memorable **key** such as `SP`.
2. In the backlog, enable the **Epics** panel and create three epics (for example *User account*, *Collecting points*, *Shop registration*). Color two for customer-facing work and one for vendor-facing work.
3. Add at least four **stories** with short summaries; put the full "As a user…" wording in each **description**. Assign each story to an epic using the parent picker or drag-and-drop.
4. Under one story, create three **subtasks** (for example requirements, design, testing). Confirm they nest under the parent and do not appear as top-level backlog cards.
5. Link two subtasks with **blocks / is blocked by** and verify the inverse link on the blocked item.
6. Create a second **Kanban** board for the same space using **Advanced** and a filter that includes only items from two of your epics (or all items if you have not learned filters yet).
7. Move one story to **In Progress** on the Kanban board and confirm the same status on the Scrum backlog.
8. Sketch your site structure: site → spaces → boards → epics → stories → subtasks, and note where links fit alongside hierarchy.

## References

- [Glossary](../reference/glossary.md)
- [Jira terminology changes](../reference/jira-terminology-changes.md)
- [Scrum vs Kanban](../reference/scrum-vs-kanban.md)
- [JQL cheat sheet](../reference/jql-cheat-sheet.md)
