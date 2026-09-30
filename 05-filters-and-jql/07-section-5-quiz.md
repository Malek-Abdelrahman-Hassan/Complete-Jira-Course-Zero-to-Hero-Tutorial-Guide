---
title: "Section 5 Quiz"
aliases:
  - "Section 5 Quiz"
type: quiz
section: 5
lesson: 7
duration: ""
status: done
tags:
  - jira
  - section/05
  - quiz
  - flashcards
---

# Section 5 Quiz

[Course home](../README.md) › [Section 5: Filters and JQL](README.md) › Quiz

> [!IMPORTANT]
> The official Udemy quiz questions are not reproduced here. The practice questions and flashcards below are original and cover the same topics.

## Topics covered

- [Using Basic Search and Quick Filters in Jira](01-basic-search-and-quick-filters.md)
- [Creating and Saving Filters in Jira for Quick Access](02-creating-and-saving-filters.md)
- [JQL Basics: What is Jira Query Language and Why It Matters](03-jql-basics.md)
- [Time-Based JQL Queries: Finding Issues by Date and Time](04-time-based-jql.md)
- [Link-Based and Hierarchy JQL Queries for Advanced Filtering](05-link-and-hierarchy-jql.md)
- [Useful JQL Examples for Real Work: Practical Use Cases](06-useful-jql-examples.md)

## Practice questions

<details>
<summary>1. What is the fastest way to learn JQL syntax if you prefer clicking fields over typing queries?</summary>
Build the search in basic search, then switch to the JQL tab. Jira shows the equivalent query for the criteria you selected.
</details>

<details>
<summary>2. You saved a filter for a team dashboard but teammates see an error. What sharing setting did you likely forget?</summary>
View access — the filter must be shared with the organization or a group that includes teammates, not kept private.
</details>

<details>
<summary>3. Write JQL to list unassigned open work in space ABC, in the same order as the board.</summary>
project = ABC AND assignee is EMPTY AND statusCategory != Done ORDER BY rank ASC
</details>

<details>
<summary>4. Why does assignee != currentUser() miss unassigned work items?</summary>
Unassigned items have no assignee value, so they fail both equality and inequality tests. Add OR assignee is EMPTY to include them.
</details>

<details>
<summary>5. Write JQL for work items created between five and three days ago (inclusive window).</summary>
created >= -5d AND created <= -3d ORDER BY rank ASC
</details>

<details>
<summary>6. Work item ABC-9 is blocked by ABC-35. Write JQL to find ABC-35 when starting from ABC-9.</summary>
issue in linkedIssues(ABC-9, "is blocked by") ORDER BY rank ASC
</details>

<details>
<summary>7. What is the difference between issueLinkType = blocks and issue in linkedIssues(ABC-35, "blocks")?</summary>
issueLinkType = blocks returns every work item on either side of any blocks link site-wide. linkedIssues(ABC-35, "blocks") returns only work items that ABC-35 blocks.
</details>

<details>
<summary>8. Write JQL for summaries containing the word login in space ABC.</summary>
project = ABC AND summary ~ "login" ORDER BY rank ASC
</details>

<details>
<summary>9. You saved a filter named High priority bugs. Write JQL that finds your open assigned work on top of that filter.</summary>
filter = "High priority bugs" AND assignee = currentUser() AND statusCategory != Done ORDER BY rank ASC
</details>

<details>
<summary>10. When bulk-transitioning 40 work items, what checkbox should you usually turn off?</summary>
Send email (or notify watchers). Each transition can email every watcher per work item.
</details>

<details>
<summary>11. Using parentEpic, write JQL for the stories and tasks under epic ABC-1, without the epic itself or any subtasks.</summary>
parentEpic = ABC-1 AND issuetype in (Story, Task) ORDER BY rank ASC. Without the issuetype clause, parentEpic also returns the epic and every subtask below it.
</details>

<details>
<summary>12. Exporting filter results for Excel cleanup — which export option keeps the file smaller?</summary>
Export filter fields (only visible columns), not all fields.
</details>

## Flashcards

What is basic search?::A point-and-click search form with dropdown fields for common work item criteria
How do you see the JQL for a basic search?::Switch to the JQL tab after building criteria in basic search
What is a saved filter?::A named, reusable search stored for quick access, sharing, boards, and dashboards
Filter viewers vs editors?::Viewers run the filter; editors can change its JQL
What bulk operation changes workflow status?::Transition
What bulk operation clears labels or components?::Edit with Clear field on the chosen fields
What three parts form a JQL clause?::Field, operator, value
What does currentUser() return?::Whoever is running the query right now
When use is/is not?::Only to test EMPTY vs not empty — for example assignee is EMPTY
What does != miss for assignee?::Unassigned work items — add OR assignee is EMPTY
What does in / not in do?::Matches any value inside parentheses — issuetype in (Story, Task)
Why ORDER BY rank ASC?::Aligns filter order with board backlog ranking
Relative date example for last 7 days?::created >= -7d
Date function for since Monday?::created >= startOfWeek()
Two-clause past window example?::created >= -5d AND created <= -3d
Which field is user-set for deadlines?::due
Which date field is automatic at creation?::created
parent = ABC-1 vs parentEpic = ABC-1?::parent returns direct children only; parentEpic also returns the epic itself and all subtasks below it
Legacy epic field in JQL?::"Epic Link" = KEY; retired in 2024, it works only in existing filters, so new filters use parent
issueLinkType vs linkedIssues()?::Link type filters by relationship name globally; linkedIssues finds neighbors of one key
Text contains operator?::~ — for example summary ~ "points"
AND vs OR?::AND requires all clauses; OR matches any one clause
Nested filter syntax?::filter = "Saved Filter Name" as a clause in a larger query
JQL space field name?::project — even though the UI says space

## Easy to confuse

| Concept A | Concept B | How to tell them apart |
|---|---|---|
| Basic search | JQL | Basic search uses form fields; JQL is typed query syntax. Switch to JQL to see how they connect. |
| Quick filter | Saved filter | Quick filters are board toggles with JQL. Saved filters live under Filters and can source entire boards. |
| `assignee != X` | `assignee is EMPTY` | Not equal excludes empty values. Unassigned work needs is EMPTY explicitly or combined with OR. |
| `parent` | `issueLinkType` | parent is hierarchy (one parent per child). issueLinkType is a non-hierarchical link such as blocks or clones. |
| `"is blocked by"` | `"blocks"` | Two directions of the same link. Query from the blocked item with "is blocked by"; from the blocker with "blocks". |
| `created >= -7d` | `created >= startOfWeek()` | -7d is rolling seven days from now. startOfWeek() is calendar week boundary — different windows. |
---

Previous: [Useful JQL Examples for Real Work: Practical Use Cases](06-useful-jql-examples.md) · Next: [Section 6: Projects, Boards, Workflows, and Statuses](../06-boards-and-workflows/README.md)
