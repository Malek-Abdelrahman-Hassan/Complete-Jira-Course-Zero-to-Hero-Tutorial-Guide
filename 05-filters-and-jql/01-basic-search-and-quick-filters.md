---
title: "Using Basic Search and Quick Filters in Jira"
aliases:
  - "Using Basic Search and Quick Filters in Jira"
type: lesson
section: 5
lesson: 1
duration: "6:28"
status: done
tags:
  - jira
  - section/05
  - topic/search
  - topic/filters
---

# Using Basic Search and Quick Filters in Jira

[Course home](../README.md) › [Section 5: Filters and JQL](README.md) › Lesson 1 · 6:28

## TL;DR

Basic search lets you find work items (formerly *issues*) by filling in form fields instead of writing JQL. Open it from **Filters > All work items** or a space's list view, combine criteria such as space, assignee, work type, and status, then switch to JQL to see the query Jira built. Saved criteria from basic search can also become **quick filters** on a board.

## Key concepts

- **Basic search**: A point-and-click search form with dropdown fields. It covers common criteria but not everything JQL can do.
- **Filter**: Any search that returns a list of work items. Basic search and JQL both produce filters; only saved filters persist for reuse.
- **Quick filter**: A board-level toggle that narrows the board using JQL. Quick filters were introduced earlier in the course; this lesson shows how basic search feeds into them.
- **Project field in basic search**: Selects which space's work items to include or exclude. In JQL the same idea uses the `project` field even though the UI says *space* (the newer alias `space` may work too, but not yet on every site).

## How to do it in Jira

1. Open the work item search: select **Filters** in the sidebar, then **All work items** (older recordings show **View all issues**), or use **Search** in the top bar and choose the option to search Jira for work items. Inside a space, the **List** view (an **Issues** tab on some older spaces) offers similar filtering.
2. Review the default fields. Common ones include **Project** (space), **Assignee**, **Type** (work type), **Status**, and **Created** (often preset to the last 30 days). Open **More filters** to add fields such as story points, labels, or priority.
3. Set your criteria. Use **equals** to include a value or **not equals** to exclude it. Example for the *Stamps and Points* space: **Project** equals *Stamps and Points*, **Assignee** equals a team member, **Status** not equals *Done*.
4. Select **Search** or **Update** to refresh the results list.
5. Switch to JQL: select the **JQL** tab or button. Jira converts your form choices into a query you can copy, edit, or reuse.
6. Turn the query into a board quick filter: open the board, choose **Board settings** (or **Manage quick filters**), create a new quick filter, paste or type the JQL, and save. Enable quick filters on the board and toggle the new filter to test it.

## Examples

Filter open work for one person in the *Stamps and Points* loyalty app (space key `ABC`), excluding finished items:

```sql
project = ABC AND assignee = "John Smith" AND status != Done
```

Add a story-points condition for planning reviews:

```sql
project = ABC AND assignee = "John Smith" AND status != Done AND "Story Points" = 5
```

The last query might return a single story. Save it as a quick filter named something like *John — 5 pts open* so the team can highlight that slice of work on the board.

To see work from every space **except** *Stamps and Points*, set **Project** to **not equals** in basic search. Jira shows work items from both company-managed and team-managed spaces in one list — something basic search handles well before you need JQL.

## Tips and pitfalls

- **Basic search is enough for many tasks.** You do not have to learn JQL immediately. Build in basic search, then switch to JQL when you need more control.
- **Basic search finds work items, not people.** To locate a person or a saved filter by name, use the **Search** bar in the top bar and pick the right category.
- **Account IDs in generated JQL.** When you pick an assignee, Jira may show a long account ID in JQL instead of a display name. You can edit the query to use a readable name, or leave the ID — both work.
- **Interface labels move.** Menus and button names change between Jira releases. Look for *Filters*, *Search*, or *Issues* if the exact path differs from the lesson.

> [!TIP]
> Use basic search to prototype, then click **JQL** to learn the syntax Jira expects. That is the fastest bridge from clicking fields to writing queries by hand.

## Review questions

<details>
<summary>Where can you open basic search besides the Filters menu?</summary>
From a space's Issues tab or view, if your space navigation includes it. Exact labels vary by Jira version and space type.
</details>

<details>
<summary>What happens when you click the JQL button after building a basic search?</summary>
Jira converts your form selections into a JQL query showing the same results. You can copy, edit, or reuse that query.
</details>

<details>
<summary>Can basic search find people or spaces directly?</summary>
No. Basic search returns work items matching criteria such as assignee or project. To find people, spaces, or saved filters by name, use the Search bar in the top bar.
</details>

<details>
<summary>How do basic search criteria become a board quick filter?</summary>
Switch to JQL to get the query, open the board's quick filter settings, create a new quick filter with that JQL, and enable it on the board.
</details>

## Related

- [Glossary](../reference/glossary.md)
- [JQL Cheat Sheet](../reference/jql-cheat-sheet.md)
- [Navigate Jira: Menus, Spaces & Settings](../01-introduction/05-navigate-jira-menus-spaces-settings.md)
- [Understanding Jira Boards: Scrum, Kanban & Filters](../02-jira-fundamentals/05-boards-scrum-kanban-filters.md)
- [Creating and Saving Filters in Jira for Quick Access](02-creating-and-saving-filters.md)

---

Previous: [Section overview](README.md) · Next: [Creating and Saving Filters in Jira for Quick Access](02-creating-and-saving-filters.md)
