---
title: "Time-Based JQL Queries: Finding Issues by Date and Time"
aliases:
  - "Time-Based JQL Queries: Finding Issues by Date and Time"
type: lesson
section: 5
lesson: 4
duration: "7:50"
status: done
tags:
  - jira
  - section/05
  - topic/jql
---

# Time-Based JQL Queries: Finding Issues by Date and Time

[Course home](../README.md) › [Section 5: Filters and JQL](README.md) › Lesson 4 · 7:50

## TL;DR

JQL time queries use date fields such as `created`, `updated`, `due`, and `resolved` with comparison operators and relative offsets like `-7d` or date functions like `startOfWeek()`. Think of time as a number line: negative offsets point into the past, bare positive offsets point into the future, and functions such as `endOfWeek()` mark boundaries tied to the moment the query runs.

## Key concepts

- **`created`**: When the work item was created. Set automatically; you cannot edit it.
- **`updated`**: When any field on the work item last changed.
- **`due`**: The due date you set manually. Often hidden on the work item screen until an admin or you adds it to the layout.
- **`resolved`**: When the work item was last resolved. Set when it moves to a done-type status; it may remain set even if the item is reopened, depending on workflow settings.
- **Relative date**: An offset from now — `-7d` (seven days ago), `-2w`, `-4h`, `-30m`. Use with `>=`, `<=`, `>`, or `<`.
- **Date function**: A boundary Jira calculates — `startOfDay()`, `startOfWeek()`, `endOfWeek()`, `startOfMonth()`, `endOfMonth()`, `startOfYear()`, `endOfYear()`. Pass an offset inside the parentheses for adjacent periods, for example `startOfWeek(-1)`.

## How to do it in Jira

1. Open the **JQL** tab in search.
2. Pick a date field: `created`, `updated`, `due`, or `resolved`.
3. Add an operator (`>=`, `<=`, `>`, `<`, or `=`).
4. Enter a relative offset (`-7d`), an absolute date (`"2026-04-08"`), or a function (`startOfWeek()`).
5. Combine clauses with **AND** to define a window — for example created after five days ago but before three days ago.
6. Add `ORDER BY rank ASC` and run the query.
7. To query **due** dates, ensure the **Due date** field is visible on work items (configure the screen or ask a space admin).

## Examples

Created in the last seven days:

```sql
created >= -7d ORDER BY rank ASC
```

Created in the last two days (tighter window):

```sql
created >= -2d ORDER BY rank ASC
```

Created during a specific past window — later than five days ago but no earlier than three days ago:

```sql
created >= -5d AND created <= -3d ORDER BY rank ASC
```

Created since the start of the current week:

```sql
created >= startOfWeek() ORDER BY rank ASC
```

Due after the end of this week (future deadlines):

```sql
due > endOfWeek() ORDER BY rank ASC
```

Use weeks or hours instead of days when it fits:

```sql
updated >= -5h ORDER BY rank ASC
```

```sql
created >= -2w ORDER BY rank ASC
```

For the *Stamps and Points* space, combine time with space scope:

```sql
project = ABC AND created >= -7d ORDER BY rank ASC
```

## Tips and pitfalls

- **Past vs future on the timeline.** Offsets like `-7d` anchor to *now* and look backward. Future due dates use the `due` field with comparisons toward later dates or `endOfWeek()`.
- **Closed ranges need two clauses.** One bound (`created >= -5d`) means "since then." To cap the range, add `AND created <= -3d`.
- **`resolved` can outlive reopening.** Moving a work item back to Open does not always clear `resolved` or `resolution`. Queries on `resolved` may still find reopened items.
- **Due date is optional in Agile teams.** Many Scrum teams rely on priority and sprints instead of due dates. Add the field only when your process uses it.
- **Functions may not autocomplete.** Type `startOfWeek()` and `endOfWeek()` manually even if the editor does not suggest them.

> [!NOTE]
> The lesson title says *issues*, which are now *work items*. The date fields used here (`created`, `updated`, `resolved`, `due`) were not renamed, so these queries work unchanged.

## Review questions

<details>
<summary>Which date field is set automatically when a work item is created and cannot be edited?</summary>
created. Jira stamps it at creation time and it does not change.
</details>

<details>
<summary>What does created >= -7d mean?</summary>
Work items created on or after the point seven days before now — effectively everything created in the last seven days.
</details>

<details>
<summary>How do you find work items created during a two-day window that ended three days ago?</summary>
Use two clauses: created >= -5d AND created <= -3d. The lower bound is five days back; the upper bound is three days back.
</details>

<details>
<summary>What is the difference between due > endOfWeek() and created >= startOfWeek()?</summary>
due > endOfWeek() finds work with due dates after this week ends — future deadlines. created >= startOfWeek() finds work created since this week began — recent arrivals.
</details>

<details>
<summary>Why might resolved still have a value after a work item is moved back to Open?</summary>
Workflow configuration can leave resolution and resolved date populated after reopening, so the item still shows when it was previously closed.
</details>

## Related

- [Glossary](../reference/glossary.md)
- [JQL Cheat Sheet](../reference/jql-cheat-sheet.md)
- [JQL Basics: What is Jira Query Language and Why It Matters](03-jql-basics.md)
- [Link-Based and Hierarchy JQL Queries for Advanced Filtering](05-link-and-hierarchy-jql.md)
- [Useful JQL Examples for Real Work: Practical Use Cases](06-useful-jql-examples.md)

---

Previous: [JQL Basics: What is Jira Query Language and Why It Matters](03-jql-basics.md) · Next: [Link-Based and Hierarchy JQL Queries for Advanced Filtering](05-link-and-hierarchy-jql.md)
