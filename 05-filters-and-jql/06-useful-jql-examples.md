---
title: "Useful JQL Examples for Real Work: Practical Use Cases"
aliases:
  - "Useful JQL Examples for Real Work: Practical Use Cases"
type: lesson
section: 5
lesson: 6
duration: "7:56"
status: done
tags:
  - jira
  - section/05
  - topic/jql
---

# Useful JQL Examples for Real Work: Practical Use Cases

[Course home](../README.md) › [Section 5: Filters and JQL](README.md) › Lesson 6 · 7:56

## TL;DR

Build JQL by stating the goal in plain language first, then map each phrase to a clause. Use **AND** when every condition must match; use **OR** when any one condition is enough. The `~` operator searches text in fields such as `summary`. Save intermediate filters and reference them with `filter = "Name"` to stack conditions without repeating long queries — but keep nesting shallow for performance.

## Key concepts

- **AND vs OR**: `AND` narrows results (assignee and status and date). `OR` widens them (assignee A or assignee B). Parentheses group mixed logic when needed.
- **Text search (`~`)**: The *contains* operator for text fields. `summary ~ "points"` matches titles that include the word *points*, with stemming and wildcards supported.
- **Nested filter**: A saved filter referenced inside another query with `filter = "Filter Name"`. Jira expands it and adds quoting automatically — use autocomplete rather than typing quotes by hand.
- **Query planning**: Describe the outcome in one sentence before touching JQL. Each phrase becomes a field clause.

## How to do it in Jira

1. **State the goal** in plain language — for example "my open work created this week."
2. **Translate phrase by phrase**: assignee → `assignee = currentUser()`; not finished → `status != Done`; this week → `created >= -7d` or `created >= startOfWeek()`.
3. **Join with AND** when all phrases must be true at once.
4. **Add ORDER BY rank ASC** and run the query.
5. **Refine**: exclude epics with `issuetype != Epic`, add `project = ABC`, or search titles with `summary ~ "keyword"`.
6. **Save reusable pieces**: save a broad filter (for example all summaries containing *points*), share it if teammates need it, then start a new query with `filter = "contains points"` and add more AND clauses.
7. **Use autocomplete** when nesting filters so Jira inserts the correct name and quotes.

## Examples

New work assigned to you this week that is not done:

```sql
assignee = currentUser() AND status != Done AND created >= -7d ORDER BY rank ASC
```

Same query, excluding epics:

```sql
assignee = currentUser() AND status != Done AND created >= -7d AND issuetype != Epic ORDER BY rank ASC
```

Alternative "this week" boundary using a date function:

```sql
assignee = currentUser() AND status != Done AND created >= startOfWeek() ORDER BY rank ASC
```

Find titles mentioning *points* in the loyalty app space:

```sql
project = ABC AND summary ~ "points" ORDER BY rank ASC
```

Save the above (without the project clause) as a filter named *contains points*. Build on it for a personal view:

```sql
filter = "contains points" AND assignee = currentUser() ORDER BY rank ASC
```

Build on the same base for a specific teammate — let autocomplete format the filter name:

```sql
filter = "contains points" AND assignee = "John Smith" ORDER BY rank ASC
```

Open high-priority bugs across the site — combining several lesson topics:

```sql
type = Bug AND priority in (Highest, High) AND statusCategory != Done ORDER BY priority DESC, created ASC
```

## Tips and pitfalls

- **Say it before you write it.** "Assigned to me, not done, created this week" maps directly to three AND clauses.
- **Do not over-nest filters.** Each `filter = "..."` layer re-runs another saved search. Deep stacks slow dashboards and boards.
- **Let Jira format nested filter names.** Type `filter = con` and pick *contains points* from autocomplete. Manual quoting breaks easily.
- **JQL validates as you type.** Syntax errors highlight the problem clause — fix there before saving.
- **Keep a personal library.** Save queries you run weekly; star them in **Filters** for one-click access.

> [!TIP]
> The course provides a JQL cheat sheet PDF in local materials and a [JQL cheat sheet](../reference/jql-cheat-sheet.md) in the repo. Use either as a reference while building queries — do not copy copyrighted tables verbatim from the PDF.

> [!NOTE]
> Section 6 and beyond reuse JQL for boards, dashboards, and reports. Filters you save here become building blocks for gadgets and board sources later.

## Review questions

<details>
<summary>When should you use AND versus OR in JQL?</summary>
Use AND when every condition must match together. Use OR when matching any one condition is enough — for example assignee = "Alice" OR assignee = "Bob".
</details>

<details>
<summary>What does summary ~ "points" do?</summary>
It finds work items whose summary (title) contains the text points, using Jira's text search with stemming and wildcards.
</details>

<details>
<summary>How do you reuse a saved filter inside a new query?</summary>
Add filter = "Filter Name" as a clause, preferably through autocomplete so Jira quotes the name correctly, then AND additional conditions.
</details>

<details>
<summary>Why avoid stacking many nested filters?</summary>
Each nested filter executes a full search. Several layers slow results, especially on dashboards that refresh multiple gadgets at once.
</details>

<details>
<summary>Write JQL for: your open work created since the start of this week, excluding epics.</summary>
assignee = currentUser() AND status != Done AND created >= startOfWeek() AND issuetype != Epic ORDER BY rank ASC
</details>

## Related

- [Glossary](../reference/glossary.md)
- [JQL Cheat Sheet](../reference/jql-cheat-sheet.md)
- [JQL Basics: What is Jira Query Language and Why It Matters](03-jql-basics.md)
- [Creating and Saving Filters in Jira for Quick Access](02-creating-and-saving-filters.md)
- [Useful Gadgets for Your Jira Dashboard: Filters, Charts, and More](../08-dashboards-and-reports/02-useful-dashboard-gadgets.md)
- [Where's My Issue? Troubleshooting Visibility Problems in Jira](../10-best-practices/03-wheres-my-issue-troubleshooting.md)

---

Previous: [Link-Based and Hierarchy JQL Queries for Advanced Filtering](05-link-and-hierarchy-jql.md) · Next: [Section 5 Quiz](07-section-5-quiz.md)
