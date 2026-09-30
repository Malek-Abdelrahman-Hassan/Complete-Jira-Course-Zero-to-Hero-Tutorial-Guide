---
title: "JQL Cheat Sheet"
aliases:
  - "JQL Cheat Sheet"
  - "Jira Query Language"
type: reference
tags:
  - jira
  - reference
  - topic/jql
---

# JQL Cheat Sheet

[Course home](../README.md) · Section: [Filters and JQL](../05-filters-and-jql/README.md)

JQL (Jira Query Language) finds work items using structured queries. Every filter, board, and dashboard gadget is powered by one.

> [!NOTE]
> This page uses the classic JQL names (`project`, `issuetype`, `linkedIssues()`), which work on every site and in every saved filter. Atlassian is adding new names such as `space`, `workType`, and `linkedWorkItems()`, which may not work everywhere yet. The full mapping is in [Jira terminology changes](jira-terminology-changes.md).

## Anatomy of a query

```sql
project = ABC AND status = "In Progress" AND assignee = currentUser() ORDER BY priority DESC, updated DESC
```

| Part | Example | Meaning |
|---|---|---|
| Field | `project`, `status`, `assignee` | What to look at |
| Operator | `=`, `!=`, `in`, `~`, `is` | How to compare |
| Value | `ABC`, `"In Progress"`, `EMPTY` | What to compare against. Quote values that contain spaces. |
| Function | `currentUser()`, `openSprints()` | A value that Jira calculates when the query runs |
| Keyword | `AND`, `OR`, `NOT`, `ORDER BY` | Combine clauses and sort results |

Use parentheses to make `AND` / `OR` precedence explicit:

```sql
project = ABC AND (priority = Highest OR labels = urgent)
```

## Common fields

| Field | Example |
|---|---|
| `project` | `project = ABC` or `project in (ABC, XYZ)` |
| `issuetype` (alias `type`) | `type = Bug` or `issuetype in (Story, Task)` |
| `status` | `status = "In Review"` |
| `statusCategory` | `statusCategory != Done` (values: `"To Do"`, `"In Progress"`, `Done`) |
| `assignee`, `reporter` | `assignee = currentUser()` or `reporter = "Jane Doe"` |
| `priority` | `priority in (Highest, High)` |
| `labels` | `labels = frontend` or `labels is EMPTY` |
| `component` | `component = API` |
| `fixVersion` | `fixVersion = "1.2.0"` or `fixVersion in unreleasedVersions()` |
| `sprint` | `sprint in openSprints()` |
| `parent` | `parent = ABC-42` |
| `parentEpic` | `parentEpic = ABC-1` (company-managed spaces) |
| `filter` | `filter = "My open work" AND priority = High` (reuses a saved filter) |
| `created`, `updated`, `resolved`, `due` | `created >= -7d` |
| `resolution` | `resolution = Unresolved` |
| `text`, `summary`, `description`, `comment` | `text ~ "login error"` |
| `watcher` | `watcher = currentUser()` |
| `issueLinkType` | `issueLinkType = "is blocked by"` |

## Operators

| Operator | Example | Notes |
|---|---|---|
| `=` / `!=` | `status = Done` | Exact match |
| `>` `>=` `<` `<=` | `created >= "2026-01-01"` | Dates, numbers, and ordered fields such as priority |
| `in` / `not in` | `status in ("To Do", "In Progress")` | Shorter than chaining `OR` |
| `~` / `!~` | `summary ~ "payment*"` | Text contains; supports wildcards and stemming |
| `is` / `is not` | `assignee is EMPTY` | Checks empty values (`EMPTY` or `NULL`) |
| `was` / `was in` / `was not` | `status was "In Progress"` | History: the value at some point in the past |
| `changed` | `status changed to Done after -7d` | History: the value changed |

History operators accept the predicates `after`, `before`, `on`, `during`, `by`, `from`, and `to`:

```sql
status changed from "In Progress" to "Done" by currentUser() during (startOfWeek(), now())
```

## Functions

| Function | Returns |
|---|---|
| `currentUser()` | The person running the query |
| `membersOf("group")` | Users in a group |
| `openSprints()`, `closedSprints()`, `futureSprints()` | Sprints by state |
| `unreleasedVersions()`, `releasedVersions()` | Versions by state (optionally for one space: `unreleasedVersions(ABC)`) |
| `earliestUnreleasedVersion(ABC)`, `latestReleasedVersion(ABC)` | A single version |
| `linkedIssues(ABC-1)`, `linkedIssues(ABC-1, "blocks")` | Work items linked to a given work item |
| `issueHistory()` | Work items you viewed recently |
| `watchedIssues()` | Work items you are watching |
| `now()` | The current date and time |
| `startOfDay()`, `endOfDay()` | Today's boundaries |
| `startOfWeek()`, `endOfWeek()` | This week's boundaries |
| `startOfMonth()`, `endOfMonth()` | This month's boundaries |
| `startOfYear()`, `endOfYear()` | This year's boundaries |

## Dates and time

- **Absolute dates:** `"2026-03-31"` or `"2026-03-31 14:00"`.
- **Relative dates:** `-1d`, `-2w`, `-4h`, `-30m`. For example `created >= -7d` means "in the last 7 days".
- **Offsets in date functions:** `startOfWeek(-1)` is the start of last week, and `startOfMonth(1)` is the start of next month.

| Goal | Query |
|---|---|
| Created in the last 7 days | `created >= -7d` |
| Updated today | `updated >= startOfDay()` |
| Resolved last week | `resolved >= startOfWeek(-1) AND resolved < startOfWeek()` |
| Due this week | `due >= startOfWeek() AND due <= endOfWeek()` |
| Overdue | `due < startOfDay() AND statusCategory != Done` |
| Not touched for two weeks | `updated <= -14d AND statusCategory != Done` |

## Links and hierarchy

| Goal | Query |
|---|---|
| Children of an epic | `parent = ABC-42` |
| Children of several parents | `parent in (ABC-42, ABC-43)` |
| An epic plus everything under it, subtasks included (company-managed spaces) | `parentEpic = ABC-42` |
| Work items blocked by something | `issueLinkType = "is blocked by" AND statusCategory != Done` |
| Everything linked to one work item | `issue in linkedIssues(ABC-1)` |
| Only subtasks | `issuetype in subTaskIssueTypes()` |
| Everything except subtasks | `issuetype in standardIssueTypes()` |

## Ready-to-use queries

**My open work, most important first**

```sql
assignee = currentUser() AND statusCategory != Done ORDER BY priority DESC, updated DESC
```

**Unassigned work in a space**

```sql
project = ABC AND assignee is EMPTY AND statusCategory != Done ORDER BY created ASC
```

**Current sprint**

```sql
project = ABC AND sprint in openSprints() ORDER BY rank
```

**Unfinished work from closed sprints**

```sql
project = ABC AND sprint in closedSprints() AND statusCategory != Done
```

**Open high-priority bugs**

```sql
type = Bug AND priority in (Highest, High) AND statusCategory != Done ORDER BY priority DESC, created ASC
```

**Work planned for the next release**

```sql
project = ABC AND fixVersion = earliestUnreleasedVersion(ABC)
```

**Work nobody has planned into a release**

```sql
project = ABC AND fixVersion is EMPTY AND statusCategory != Done
```

**Started this week**

```sql
status changed to "In Progress" during (startOfWeek(), now())
```

**Recently viewed**

```sql
issue in issueHistory() ORDER BY lastViewed DESC
```

## Tips

- Start with basic search, then switch to JQL to see the query Jira generated.
- Prefer `statusCategory` over lists of status names, because it keeps working when teams rename or add statuses.
- Put values with spaces in quotes: `status = "In Review"`. Single and double quotes both work.
- End filters with `ORDER BY rank ASC` when the results should match the board and backlog order.
- `!=` skips empty values. `assignee != currentUser()` misses unassigned work, so add `OR assignee is EMPTY`.
- `linkedIssues()` is a function, so it goes after `issue in`: write `issue in linkedIssues(ABC-1)`, not `linkedIssues = ABC-1`.
- Field and value names differ between sites. Story points may be `"Story Points"` or `"Story point estimate"`, and the subtask type may be `Sub-task` or `Subtask`. Let autocomplete pick the exact name.
- `"Epic Link"` was retired in February 2024. Filters saved before then still run, but new filters must use `parent` (direct children) or `parentEpic` (the epic and everything under it).
- Save useful queries as filters, star them, and reuse them in boards, dashboards, and other queries with `filter = "Name"`.

## Queries from the course

The queries shown in the lessons, grouped by lesson. They use the sample space keys `ABC` and `XYZ`.

### [Using Basic Search and Quick Filters in Jira](../05-filters-and-jql/01-basic-search-and-quick-filters.md)

| Goal | Query |
|---|---|
| One person's open work in a space | `project = ABC AND assignee = "John Smith" AND status != Done` |
| The same, only 5-point work items | `project = ABC AND assignee = "John Smith" AND status != Done AND "Story Points" = 5` |

### [Creating and Saving Filters in Jira for Quick Access](../05-filters-and-jql/02-creating-and-saving-filters.md)

| Goal | Query |
|---|---|
| All stories in a space, in board order | `project = ABC AND issuetype = Story ORDER BY rank ASC` |
| Stories that have left the Open status | `project = ABC AND issuetype = Story AND status != Open` |

### [JQL Basics: What is Jira Query Language and Why It Matters](../05-filters-and-jql/03-jql-basics.md)

| Goal | Query |
|---|---|
| My work | `assignee = currentUser()` |
| Unassigned work | `assignee is EMPTY` |
| Everything not assigned to me, unassigned included | `assignee != currentUser() OR assignee is EMPTY` |
| Stories and subtasks | `issuetype in (Story, Subtask) ORDER BY rank ASC` |
| Everything except stories and subtasks | `issuetype not in (Story, Subtask) ORDER BY rank ASC` |
| Estimated work | `"Story Points" is not EMPTY` |
| Unestimated work | `"Story Points" is EMPTY` |
| 5 points or more | `"Story Points" >= 5 ORDER BY rank ASC` |

### [Time-Based JQL Queries: Finding Issues by Date and Time](../05-filters-and-jql/04-time-based-jql.md)

| Goal | Query |
|---|---|
| Created in the last 7 days | `created >= -7d ORDER BY rank ASC` |
| Created between 5 and 3 days ago | `created >= -5d AND created <= -3d ORDER BY rank ASC` |
| Created since the start of this week | `created >= startOfWeek() ORDER BY rank ASC` |
| Due after this week | `due > endOfWeek() ORDER BY rank ASC` |
| Updated in the last 5 hours | `updated >= -5h ORDER BY rank ASC` |
| Created in the last 2 weeks | `created >= -2w ORDER BY rank ASC` |

### [Link-Based and Hierarchy JQL Queries for Advanced Filtering](../05-filters-and-jql/05-link-and-hierarchy-jql.md)

| Goal | Query |
|---|---|
| Children of one parent | `parent = ABC-44 ORDER BY rank ASC` |
| Children of several parents | `parent in (ABC-44, ABC-37) ORDER BY rank ASC` |
| Stories and tasks under an epic, without the epic or subtasks | `parentEpic = ABC-1 AND issuetype in (Story, Task) ORDER BY rank ASC` |
| Children of an epic, retired field (filters saved before 2024 only) | `"Epic Link" = ABC-1 ORDER BY rank ASC` |
| Every work item in a blocking link, on either side | `issueLinkType = blocks ORDER BY rank ASC` |
| Cloned work items | `issueLinkType = clones ORDER BY rank ASC` |
| Everything linked to one work item | `issue in linkedIssues(ABC-9) ORDER BY rank ASC` |
| What blocks ABC-9 | `issue in linkedIssues(ABC-9, "is blocked by") ORDER BY rank ASC` |
| What ABC-35 blocks | `issue in linkedIssues(ABC-35, "blocks") ORDER BY rank ASC` |

### [Useful JQL Examples for Real Work: Practical Use Cases](../05-filters-and-jql/06-useful-jql-examples.md)

| Goal | Query |
|---|---|
| My open work from the last 7 days, without epics | `assignee = currentUser() AND status != Done AND created >= -7d AND issuetype != Epic ORDER BY rank ASC` |
| My open work created this week | `assignee = currentUser() AND status != Done AND created >= startOfWeek() ORDER BY rank ASC` |
| Summary contains a word | `project = ABC AND summary ~ "points" ORDER BY rank ASC` |
| Reuse a saved filter, then narrow it | `filter = "contains points" AND assignee = currentUser() ORDER BY rank ASC` |
| Open high-priority bugs | `type = Bug AND priority in (Highest, High) AND statusCategory != Done ORDER BY priority DESC, created ASC` |

### Shared board for two teams

From [Creating and Using Shared Boards for Team Collaboration](../07-cross-team-collaboration/02-shared-boards.md): one team's iOS work plus the other team's work labeled for the app, in the upcoming releases.

```sql
(
  (project = ABC AND fixVersion in unreleasedVersions() AND component = iOS)
  OR
  (project = XYZ AND fixVersion in unreleasedVersions() AND labels = "SP app")
)
ORDER BY rank ASC
```

[What to Do When Statuses Don't Match Across Teams](../07-cross-team-collaboration/04-mismatched-statuses-across-teams.md) wraps the same scope in parentheses and adds `AND statusCategory in ("To Do", "In Progress")`. Status categories work across both workflows even when the status names differ.

### From other lessons

| Goal | Query | Lesson |
|---|---|---|
| Epics in a space | `project = ABC AND issuetype = Epic` | [Understanding Jira Work Types & Hierarchy](../02-jira-fundamentals/02-work-types-and-hierarchy.md) |
| Children of one epic | `project = ABC AND parent = ABC-5` | [Create Work Items: Epics, Stories & Subtasks](../02-jira-fundamentals/03-create-epics-stories-subtasks.md) |
| What ABC-15 blocks | `issue in linkedIssues("ABC-15", "blocks")` | [Parent-Child Hierarchy vs Linked Work Items](../02-jira-fundamentals/04-parent-child-vs-linked-work-items.md) |
| Open work across two spaces | `project in (ABC, XYZ) AND status != Done` | [Understanding Jira Boards: Scrum, Kanban & Filters](../02-jira-fundamentals/05-boards-scrum-kanban-filters.md) |
| Estimated work in the current sprint | `project = ABC AND "Story Points" is not EMPTY AND sprint in openSprints()` | [Estimating with Story Points and Time in Agile Projects](../03-agile-scrum-and-kanban/02-estimating-story-points-and-time.md) |
| Blocked work in the current sprint | `project = ABC AND sprint in openSprints() AND labels = blocked` | [Running Daily Standups with Jira: Best Practices](../03-agile-scrum-and-kanban/03-daily-standups.md) |
| Work with one label, in board order | `labels = wishlist AND project = ABC ORDER BY Rank ASC` | [Using Issue Labels and Priorities to Organize Work in Jira](../04-organizing-work/01-labels-and-priorities.md) |
| Work in one component | `component = Android AND project = ABC` | [Structuring Work with Components in Jira Projects](../04-organizing-work/02-components.md) |
| Unfinished work in a version | `fixVersion = "1.0" AND project = ABC AND status != Done` | [Planning and Releasing with Versions in Jira](../04-organizing-work/03-versions-and-releases.md) |
| Copies of a template, without the template itself | `summary ~ "planning checklist" AND project = ABC AND labels != template` | [Creating Templates and Reusable Tasks for Efficiency](../04-organizing-work/04-templates-and-reusable-tasks.md) |
| Work items that mention onboarding | `project = ABC AND (summary ~ onboarding OR description ~ onboarding)` | [Examples of Simple Automation Rules for Teams](../09-automation/03-simple-automation-rules.md) |
| Open work not updated for 5 days | `project = ABC AND status != Done AND updated <= -5d` | [Final Challenge: Apply What You've Learned in Jira](../10-best-practices/04-final-challenge.md) |
