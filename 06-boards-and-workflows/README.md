---
title: "Understanding Projects, Boards, Workflows, and Statuses"
short_title: "Projects, Boards, Workflows, and Statuses"
aliases:
  - "Section 6 — Understanding Projects, Boards, Workflows, and Statuses"
  - "Section 06 overview"
type: section
section: 6
tags:
  - jira
  - section/06
---

# Section 6 — Understanding Projects, Boards, Workflows, and Statuses

[Course home](../README.md) · Previous: [Section 5: Filters and JQL](../05-filters-and-jql/README.md) · Next: [Section 7: Cross-Team Collaboration](../07-cross-team-collaboration/README.md)

## What you will learn

By the end of this section you should be able to:

- Customize how a board looks for you without admin access.
- Explain statuses, status categories, and transitions.
- Find your way through complex workflows.

## Lessons

<!-- BEGIN generated: lessons -->

| # | Lesson | Type | Duration | Notes |
|---:|---|---|---:|---|
| 1 | [Customizing Your Jira Board View Without Admin Access](01-customizing-board-view.md) | Video | 10:00 | Done |
| 2 | [Workflow States and Transitions: What You Can See and Do](02-workflow-states-and-transitions.md) | Video | 8:06 | Done |
| 3 | [Navigating Complex Workflows Without Getting Lost in Jira](03-navigating-complex-workflows.md) | Video | 12:56 | Done |
| 4 | [Section 6 Quiz](04-section-6-quiz.md) | Quiz | — | Done |

**Video time:** 31:02 · **Notes completed:** 4 / 4

<!-- END generated: lessons -->

## Key takeaways

- **Board administrators** can reshape columns, swimlanes, card layout, quick filters, working days, and estimation on a board without Jira site admin rights.
- **Unmapped statuses** are the usual reason work items vanish from a board and Scrum backlog after a status change—map every active status to a column.
- **Board filters** define which work items a board shows; Kanban boards may add a **sub-filter** (for example unreleased versions) and a **completed-issues** time window.
- A **workflow** is statuses plus **transitions**; the status dropdown shows only moves allowed from the current step, not every status on the diagram.
- **Status categories** (To Do, In Progress, Done) drive reporting and progress bars; custom status names still belong to one category.
- **Resolution** records why finished work stopped and is usually permanent once set on a resolve transition.
- Complex workflows add **screens**, **conditions**, **validators**, and **post functions**—when behavior is unclear, open **View workflow** and involve an administrator.
- **Keep workflows simple** at first; add gates, screens, and automation gradually so everyday users are not overwhelmed.

## Hands-on practice

Suggested exercises for a free Jira Cloud site (these are not part of the official course material):

1. Open **Board settings** on your Scrum board: add yourself as a board administrator, review the board filter, and set working days plus story-point estimation.
2. In **Layout > Columns**, check for unmapped statuses. If none exist, add a custom **In Progress** status (for example **Review**) in workflow settings with admin help, then create a column and map it before moving any work there.
3. Set WIP max values on **To Do** and **In Progress**, enable **Days in column** on backlog and active sprint card layouts, and pick card colors by assignee.
4. Create two quick filters your team would use (for example `assignee = currentUser()` and a label you define on sample work items).
5. On a Kanban board, compare the sub-filter for unreleased versions with **Completed issues** set to two weeks vs show everything.
6. Open a work item, use **View workflow**, and list every transition available from its current status. Try changing status from the work item and by dragging on the board.
7. For each status on the diagram, note its **status category**. Move a sample story to **Done** and observe which resolution options appear.
8. If you have admin access on a practice site, clone the lesson's linear review workflow (To Do → In progress → In review → Ready for QA → In QA → Done with Reopened loop), assign it to a test space, publish, and walk one story through each transition including a resolve screen.

## References

- [Glossary](../reference/glossary.md)
- [Scrum vs Kanban](../reference/scrum-vs-kanban.md)
