---
title: "JQL Basics: What is Jira Query Language and Why It Matters"
aliases:
  - "JQL Basics: What is Jira Query Language and Why It Matters"
type: lesson
section: 5
lesson: 3
duration: "10:47"
status: done
tags:
  - jira
  - section/05
  - topic/jql
---

# JQL Basics: What is Jira Query Language and Why It Matters

[Course home](../README.md) › [Section 5: Filters and JQL](README.md) › Lesson 3 · 10:47

## TL;DR

JQL (Jira Query Language) finds work items using **field**, **operator**, and **value** clauses combined with **AND**, **OR**, and **ORDER BY**. It powers every saved filter, board, and dashboard gadget. Start from the **JQL** tab in search, use autocomplete for field names, and end queries with `ORDER BY rank ASC` so result order matches your boards.

## Key concepts

- **JQL**: A structured query language for work items. It is not a programming language, but it uses precise syntax similar to database queries.
- **Field**: Any attribute on a work item — built-in fields such as `assignee` and `status`, or custom fields your organization adds. If it appears on the work item screen, it can usually be queried.
- **Operator**: How the field is compared to a value. Common operators include `=`, `!=`, `in`, `not in`, `is`, `is not`, and numeric comparisons (`>`, `>=`, `<`, `<=`).
- **Function**: A dynamic value Jira calculates at query time, such as `currentUser()` for whoever is running the search.
- **Keyword**: Words that combine or sort clauses: `AND`, `OR`, `NOT`, and `ORDER BY`.
- **Rank**: A hidden global ordering field. Boards use rank for backlog order; adding `ORDER BY rank ASC` keeps filter results aligned with board order.

## JQL operators at a glance

| Operator | Example | Use when |
|---|---|---|
| `=` / `!=` | `assignee = currentUser()` | Exact match or exclusion |
| `is` / `is not` | `"Story Points" is EMPTY` | Only for empty vs not-empty checks |
| `in` / `not in` | `issuetype in (Story, Subtask)` | Match any value in a list |
| `>`, `>=`, `<`, `<=` | `"Story Points" >= 5` | Numbers, dates, ordered fields |

## How to do it in Jira

1. Open **Filters** and switch to the **JQL** tab (or open **Advanced search**).
2. Type a **field** name; autocomplete suggests matches. Select one and press Enter.
3. Press Space to see **operators** valid for that field. Pick one.
4. Enter a **value** — a name, status, number, `EMPTY`, or a function such as `currentUser()`.
5. Add more clauses with **AND** (all must match) or **OR** (either can match).
6. Finish with **ORDER BY rank ASC** (or another sort field).
7. Press Enter or select **Search**. Fix syntax errors using Jira's inline hints.

## Examples

Work assigned to whoever runs the query:

```sql
assignee = currentUser()
```

Unassigned work:

```sql
assignee is EMPTY
```

Everything assigned to someone else **or** unassigned — `!=` alone misses unassigned items:

```sql
assignee != currentUser() OR assignee is EMPTY
```

Stories and subtasks only, in board order:

```sql
issuetype in (Story, Subtask) ORDER BY rank ASC
```

Work types other than stories and subtasks. Use the exact subtask name your space defines (`Subtask` on current sites; older sites may still use `Sub-task` with a hyphen):

```sql
issuetype not in (Story, Subtask) ORDER BY rank ASC
```

Story points populated vs empty:

```sql
"Story Points" is not EMPTY
```

```sql
"Story Points" is EMPTY
```

Numeric filtering on story points:

```sql
"Story Points" >= 5 ORDER BY rank ASC
```

Five or higher. Strictly greater than five excludes exactly five:

```sql
"Story Points" > 5 ORDER BY rank ASC
```

## Tips and pitfalls

- **`!=` excludes empty values.** To mean "not me, including unassigned," combine `assignee != currentUser() OR assignee is EMPTY`.
- **`is` / `is not` only pair with EMPTY.** Use them to test whether a field has any value, not for other comparisons.
- **Quote names with spaces.** Custom fields such as `"Story Points"` and status names such as `"In Progress"` need double quotes.
- **Match work type spelling exactly.** `Sub-task` and `Subtask` are different strings; a mismatch silently skews results.
- **Make `ORDER BY rank ASC` a habit.** It keeps filter lists, boards, and exports in the same order.

> [!TIP]
> Open any work item and scan its fields — each label is a potential JQL field. Custom fields appear with the name your admin configured.

## Review questions

<details>
<summary>What three parts make up a basic JQL clause?</summary>
Field, operator, and value — for example assignee = currentUser().
</details>

<details>
<summary>Why does assignee != currentUser() not return unassigned work items?</summary>
Unassigned work items have no assignee value, so they fail both equality and inequality checks. Add OR assignee is EMPTY to include them.
</details>

<details>
<summary>When should you use is or is not instead of = or !=?</summary>
When checking whether a field is empty or has any value — for example "Story Points" is EMPTY. The is/is not operators only work with EMPTY.
</details>

<details>
<summary>Why add ORDER BY rank ASC to most queries?</summary>
Rank is Jira's global backlog ordering. Sorting by rank ASC aligns filter results with the order work items appear on boards.
</details>

<details>
<summary>What does currentUser() do in a saved filter shared with teammates?</summary>
It resolves to whoever runs the query. The same filter shows each person their own assigned work without rewriting the JQL.
</details>

## Related

- [Glossary](../reference/glossary.md)
- [JQL Cheat Sheet](../reference/jql-cheat-sheet.md)
- [Using Basic Search and Quick Filters in Jira](01-basic-search-and-quick-filters.md)
- [Creating and Saving Filters in Jira for Quick Access](02-creating-and-saving-filters.md)
- [Time-Based JQL Queries: Finding Issues by Date and Time](04-time-based-jql.md)

---

Previous: [Creating and Saving Filters in Jira for Quick Access](02-creating-and-saving-filters.md) · Next: [Time-Based JQL Queries: Finding Issues by Date and Time](04-time-based-jql.md)
