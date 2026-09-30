---
title: "Link-Based and Hierarchy JQL Queries for Advanced Filtering"
aliases:
  - "Link-Based and Hierarchy JQL Queries for Advanced Filtering"
type: lesson
section: 5
lesson: 5
duration: "8:52"
status: done
tags:
  - jira
  - section/05
  - topic/jql
  - topic/links
  - topic/hierarchy
---

# Link-Based and Hierarchy JQL Queries for Advanced Filtering

[Course home](../README.md) › [Section 5: Filters and JQL](README.md) › Lesson 5 · 8:52

## TL;DR

Hierarchy queries use the `parent` field to find children of an epic or other parent work item. Link queries use `issueLinkType` to filter by relationship type (blocks, clones, and so on) or `issue in linkedIssues()` to find everything connected to a specific work item. JQL can combine these clauses with AND and OR — combinations basic search cannot express.

## Key concepts

- **Parent/child hierarchy**: A parent (often an epic) has many children; each child has exactly one parent. Query with `parent = KEY` or `parent in (KEY-1, KEY-2)`, which return the direct children only.
- **`parentEpic`**: Returns an epic together with everything under it: the epic itself, its children, and their subtasks. Company-managed spaces only.
- **Epic Link (retired field)**: Filters written before 2024 used `"Epic Link" = ABC-1`. Atlassian retired it in February 2024 in favor of `parent`: existing saved filters that use it still run, but new filters must use `parent`.
- **Issue link**: A separate relationship between two work items (blocks, is blocked by, clones, relates to). Each link type has two directions.
- **`issueLinkType`**: Filters by link type name across the site — for example every item involved in a *blocks* relationship.
- **`linkedIssues()` function**: Returns work items linked to a given key. Optionally pass a link type as the second argument to filter direction.
- **New JQL names**: Atlassian's documentation now also lists `workItemLinkType` and `linkedWorkItems()` for the two items above. The names used in this lesson keep working everywhere; the new ones may not work on every site yet.

## How to do it in Jira

1. **Find children of one parent**: in JQL, type `parent = ABC-44` (replace with your parent key) and add `ORDER BY rank ASC`.
2. **Find children of several parents**: use `parent in (ABC-44, ABC-37)`.
3. **Find everything under an epic**: use `parentEpic = ABC-1`. It also returns the epic and the subtasks, so add `AND issuetype in (Story, Task)` when you only want the stories and tasks.
4. **Filter by link type**: use `issueLinkType = blocks` to see all work items on either side of blocking links.
5. **Find links from a specific work item**: use `issue in linkedIssues(ABC-9)` for every linked neighbor, or add a type: `issue in linkedIssues(ABC-9, "is blocked by")`.
6. **Pick the correct link direction**: if ABC-9 is blocked by ABC-35, search from ABC-9 with `"is blocked by"`. To see what ABC-35 blocks, search from ABC-35 with `"blocks"`.
7. Combine with other clauses — for example open blocked work: `issueLinkType = "is blocked by" AND statusCategory != Done`.

## Examples

All children of a sprint planning checklist parent in *Stamps and Points*:

```sql
parent = ABC-44 ORDER BY rank ASC
```

Children of two epics:

```sql
parent in (ABC-44, ABC-37) ORDER BY rank ASC
```

Retired epic field, as it appears in filters saved before 2024 (write new filters with `parent`):

```sql
"Epic Link" = ABC-1 ORDER BY rank ASC
```

Stories and tasks under an epic, without the epic row or subtasks:

```sql
parentEpic = ABC-1 AND issuetype in (Story, Task) ORDER BY rank ASC
```

Every work item involved in a *blocks* link (blocker or blocked):

```sql
issueLinkType = blocks ORDER BY rank ASC
```

Cloned work items (clone links are created automatically when you clone):

```sql
issueLinkType = clones ORDER BY rank ASC
```

Everything linked to ABC-9:

```sql
issue in linkedIssues(ABC-9) ORDER BY rank ASC
```

From ABC-9's perspective — items that block it:

```sql
issue in linkedIssues(ABC-9, "is blocked by") ORDER BY rank ASC
```

From ABC-35's perspective — items it blocks:

```sql
issue in linkedIssues(ABC-35, "blocks") ORDER BY rank ASC
```

## Tips and pitfalls

- **Link direction is easy to invert.** `"is blocked by"` and `"blocks"` describe the same relationship from opposite ends. Open both work items and read the link label if results look wrong.
- **`parentEpic` includes the epic itself.** Unlike `parent`, it also returns the epic and every subtask below it. Add an `issuetype` clause when you want only one level.
- **Quote multi-word fields and link types.** `"Story Points"` and `"is blocked by"` need double quotes.
- **`issueLinkType = blocks` is broad.** It returns blockers and blocked items together. Use `linkedIssues()` with a type when you need one side only.
- **Combine clauses for power.** Example: blocked and not done — `issueLinkType = "is blocked by" AND status != Done`.

> [!IMPORTANT]
> Basic search cannot chain hierarchy and link conditions the way JQL can. This is where switching to JQL pays off for dependency and epic breakdown views.

## Review questions

<details>
<summary>What is the difference between parent and issue links?</summary>
parent is a hierarchy: one parent, many children, each child has exactly one parent. Issue links are separate relationships (blocks, clones) between any two work items and do not define parent/child structure.
</details>

<details>
<summary>Why does parentEpic = ABC-1 return more rows than parent = ABC-1?</summary>
parent returns only the direct children of ABC-1. parentEpic returns the epic ABC-1 itself, its children, and their subtasks. Add an issuetype clause to parentEpic when you want only one level.
</details>

<details>
<summary>ABC-9 is blocked by ABC-35. Which query finds ABC-35 from ABC-9's side?</summary>
issue in linkedIssues(ABC-9, "is blocked by"). ABC-9 carries the "is blocked by" link toward ABC-35.
</details>

<details>
<summary>An old saved filter uses "Epic Link" = ABC-1. Does it still work, and what should a new filter use?</summary>
It still runs, because Atlassian kept existing filters working when it retired Epic Link in February 2024. A new filter must use parent = ABC-1 for the direct children, or parentEpic = ABC-1 for the epic and everything under it (company-managed spaces only).
</details>

<details>
<summary>What does issueLinkType = blocks return?</summary>
All work items that participate in any blocks relationship, whether they are doing the blocking or being blocked.
</details>

## Related

- [Glossary](../reference/glossary.md)
- [JQL Cheat Sheet](../reference/jql-cheat-sheet.md)
- [Jira Terminology Changes](../reference/jira-terminology-changes.md)
- [Parent-Child Hierarchy vs Linked Work Items](../02-jira-fundamentals/04-parent-child-vs-linked-work-items.md)
- [Time-Based JQL Queries: Finding Issues by Date and Time](04-time-based-jql.md)
- [Useful JQL Examples for Real Work: Practical Use Cases](06-useful-jql-examples.md)

---

Previous: [Time-Based JQL Queries: Finding Issues by Date and Time](04-time-based-jql.md) · Next: [Useful JQL Examples for Real Work: Practical Use Cases](06-useful-jql-examples.md)
