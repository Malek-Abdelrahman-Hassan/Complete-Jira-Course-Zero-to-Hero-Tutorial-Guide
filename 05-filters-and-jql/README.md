---
title: "Filters and JQL: Advanced Search for Better Visibility"
short_title: "Filters and JQL"
aliases:
  - "Section 5 — Filters and JQL: Advanced Search for Better Visibility"
  - "Section 05 overview"
type: section
section: 5
tags:
  - jira
  - section/05
---

# Section 5 — Filters and JQL: Advanced Search for Better Visibility

[Course home](../README.md) · Previous: [Section 4: Organizing Your Work](../04-organizing-work/README.md) · Next: [Section 6: Projects, Boards, Workflows, and Statuses](../06-boards-and-workflows/README.md)

## What you will learn

By the end of this section you should be able to:

- Find work quickly with basic search and quick filters.
- Create, save, share, and reuse filters.
- Write JQL queries using fields, operators, keywords, and functions.
- Query work by dates and time ranges.
- Query work by links and hierarchy.
- Apply practical JQL to everyday situations.

## Lessons

<!-- BEGIN generated: lessons -->

| # | Lesson | Type | Duration | Notes |
|---:|---|---|---:|---|
| 1 | [Using Basic Search and Quick Filters in Jira](01-basic-search-and-quick-filters.md) | Video | 6:28 | Done |
| 2 | [Creating and Saving Filters in Jira for Quick Access](02-creating-and-saving-filters.md) | Video | 10:31 | Done |
| 3 | [JQL Basics: What is Jira Query Language and Why It Matters](03-jql-basics.md) | Video | 10:47 | Done |
| 4 | [Time-Based JQL Queries: Finding Issues by Date and Time](04-time-based-jql.md) | Video | 7:50 | Done |
| 5 | [Link-Based and Hierarchy JQL Queries for Advanced Filtering](05-link-and-hierarchy-jql.md) | Video | 8:52 | Done |
| 6 | [Useful JQL Examples for Real Work: Practical Use Cases](06-useful-jql-examples.md) | Video | 7:56 | Done |
| 7 | [Section 5 Quiz](07-section-5-quiz.md) | Quiz | — | Done |

**Video time:** 52:24 · **Notes completed:** 7 / 7

<!-- END generated: lessons -->

## Key takeaways

- **Basic search** covers common criteria through form fields; switch to **JQL** to see and edit the query Jira generated.
- **Saved filters** persist searches for reuse on boards, dashboards, and bulk operations. Set **viewers** for sharing and restrict **editors** on fragile queries.
- JQL clauses follow **field → operator → value**, combined with **AND**, **OR**, and **ORDER BY**.
- Use **`currentUser()`**, **`is EMPTY`**, and **`OR`** carefully — `!=` does not include unassigned work items.
- End most queries with **`ORDER BY rank ASC`** so lists match board backlog order.
- **Time queries** use relative offsets (`-7d`), date functions (`startOfWeek()`), and fields such as `created`, `updated`, `due`, and `resolved`.
- **Hierarchy** uses `parent`; **links** use `issueLinkType` or `issue in linkedIssues(key, "link type")` — mind link direction.
- **Nested filters** (`filter = "Name"`) stack saved searches; keep nesting shallow for performance.
- **Bulk change** from filter results transitions status, clears fields, or exports to CSV — disable email notifications on large batches.

## Hands-on practice

Suggested exercises for a free Jira Cloud site (these are not part of the official course material):

1. In basic search, filter space `ABC` to your open assigned work, switch to JQL, and copy the generated query.
2. Save that query as a starred filter, share view access with your organization, and keep edit access private.
3. From the saved filter, bulk-transition two or three work items to another status, then bulk-transition them back. Leave **Send email** unchecked.
4. Write and run: `created >= -7d`, `updated >= startOfWeek()`, and `due > endOfWeek()` — add `project = ABC` if your site has many spaces.
5. Pick an epic with child stories. Run `parent = ABC-<key>` and refine with `AND issuetype in (Story, Task)`.
6. Create a blocks link between two work items. Write queries using both `"is blocked by"` and `"blocks"` until you can predict which key each returns.
7. Save `summary ~ "points"` as *contains points*, then build `filter = "contains points" AND assignee = currentUser()`.
8. Export filter fields to CSV from a saved filter and compare your five favorite queries with the [JQL cheat sheet](../reference/jql-cheat-sheet.md).

## References

- [Glossary](../reference/glossary.md)
- [JQL cheat sheet](../reference/jql-cheat-sheet.md)
- [Jira terminology changes](../reference/jira-terminology-changes.md)
