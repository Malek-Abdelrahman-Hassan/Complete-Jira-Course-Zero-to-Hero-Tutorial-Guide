---
title: "Course Recap"
aliases:
  - "Course Recap"
type: reference
tags:
  - jira
  - reference
  - review
---

# Course Recap

[Course home](../README.md) · Related: [Study Plan](../00-start-here/study-plan.md)

A one-page review of the whole course: the core ideas of each section, then the ten things most worth remembering. Each section heading links to its overview, which has the full takeaways and practice exercises.

> [!TIP]
> Try to recall each section's main ideas before reading its summary. Recalling works better than re-reading.

## Section 1: [Introduction](../01-introduction/README.md)

- Jira is Atlassian's work management tool, strongest with Agile teams but usable by almost any team.
- Jira Software and Jira Work Management are now one product, **Jira**. Jira Service Management and Jira Product Discovery are separate products.
- Projects are now **spaces**, issues are **work items**, and issue types are **work types**. JQL's old words (`project`, `issuetype`) still work, while new names such as `space` roll out.
- The interface changes often, so learn how things fit together rather than where each button sits.
- A free Jira Cloud site with a company-managed Scrum space is the safest place to practise.

## Section 2: [Jira Fundamentals](../02-jira-fundamentals/README.md)

- A **site** holds **spaces**, and each space key prefixes its work item keys (`ABC-1`).
- **Team-managed** spaces are configured by the team; **company-managed** spaces share configuration set by Jira admins.
- The default hierarchy is epic, then story, task, or bug, then subtask. Each child has one parent, and a parent-child chain can't mix the two space types.
- **Links** (blocks, relates to, duplicates, clones) connect any work items, across spaces and space types.
- **Boards are views, not containers.** They show whatever their filter returns, and a status change on one board updates the work item everywhere.

## Section 3: [Agile in Jira: Scrum and Kanban](../03-agile-scrum-and-kanban/README.md)

- A Scrum cycle in Jira: order the backlog, plan a sprint with dates and a goal, start it, update the board daily, then complete it and send unfinished work to the top of the backlog.
- **Story points** size work relative to a baseline story on the scale 1, 2, 3, 5, 8, 13, 20. Completed points per sprint become **velocity**.
- **Standups** run from the board, using quick filters, swimlanes, **Start standup**, and **Sprint insights**.
- **Kanban** replaces sprints with continuous flow. **WIP limits** flag overloaded columns in red, and every status must be mapped to a column.
- The **cumulative flow diagram** shows flow health: steady bands are good, and a widening band is a bottleneck.

## Section 4: [Organizing Your Work](../04-organizing-work/README.md)

- **Labels** are free-form and site-wide, so agree on names. **Components** are per space and managed by admins, with an optional lead and default assignee.
- **Priority** is a field; **backlog rank** (drag-and-drop order) decides what comes next.
- **Fix versions** plan releases. Releasing a version moves unfinished work on and can generate release notes.
- Epics group work by theme, and versions slice the same theme across releases.
- Jira Cloud has no template library: keep a labeled master work item with subtasks and clone it.

## Section 5: [Filters and JQL](../05-filters-and-jql/README.md)

- Build a search in **basic search**, then switch to **JQL** to see and edit the query.
- A clause is `field operator value`, combined with `AND` / `OR` and sorted with `ORDER BY rank ASC` to match the board.
- `!=` skips empty values, so add `OR assignee is EMPTY` when unassigned work matters.
- Time queries use relative dates (`-7d`) and date functions (`startOfWeek()`). Hierarchy uses `parent`, and links use `issueLinkType` or `linkedIssues()`, where direction matters.
- **Saved filters** power boards, dashboards, bulk changes, and other queries (`filter = "Name"`). Share viewers widely and keep editors few.

## Section 6: [Projects, Boards, Workflows, and Statuses](../06-boards-and-workflows/README.md)

- **Board administrators** can change columns, swimlanes, card layout, quick filters, and estimation without being Jira admins.
- **Unmapped statuses** are the usual reason work items vanish from a board and a Scrum backlog.
- A **workflow** is statuses plus **transitions**. The status dropdown offers only the moves allowed from the current status.
- **Status categories** (To Do, In Progress, Done) drive reports. **Resolution** records why work closed and normally stays once set.
- Complex workflows add screens, conditions, validators, and post functions; start simple and grow gradually.

## Section 7: [Cross-Team Collaboration](../07-cross-team-collaboration/README.md)

- Keep each team in its own space and share **views** (filters, boards, timelines, dashboards) instead of merging backlogs.
- Scope the partner work first with versions, components, labels, or epics, then write one filter with an `OR` per team.
- The **timeline** shows sprint placement and dependencies. Timeline covers one space; planning across spaces uses Plans (Jira Premium and Enterprise).
- When workflows differ, map the other team's statuses on the shared board and query with `statusCategory`.
- Tools show status; regular sync meetings still align the teams.

## Section 8: [Dashboards and Reports](../08-dashboards-and-reports/README.md)

- **Dashboards** combine gadgets, and most gadgets read from a saved filter. One filter behind several gadgets keeps them consistent.
- Workhorse gadgets: Filter Results, Work item Statistics, Pie Chart, Created vs. Resolved Chart, and Two Dimensional Filter Statistics.
- Share dashboards and their filters together, and select **Add** for every viewer or editor.
- Scrum reports: **burndown** for the current sprint, **sprint report** for review, and **velocity** for planning.
- Flow reports: the **control chart** shows cycle time and outliers, and the **CFD** shows where work piles up.

## Section 9: [Jira Automation](../09-automation/README.md)

- Space admins can automate their own space under **Space settings > Automation**.
- A rule is a **trigger**, optional **conditions**, and **actions**. **Smart values** such as `{{issue.key}}` insert live data.
- Good first rules: reopen done work when a comment arrives, and add a label based on keywords.
- Checklist apps keep a Definition of Done inside a work item instead of adding more subtasks.
- Prototype in your own space, then give a Jira admin a detailed request for global or multi-space rules, and announce changes to affected teams.

## Section 10: [Best Practices and Final Challenge](../10-best-practices/README.md)

- Shortcuts save time: `c`, `/`, `.`, `g` then `i`, and `s` then `t` / `s` then `b` on the backlog. Bulk selection and list view speed up multi-item edits.
- Good etiquette: clear summaries, full descriptions, honest statuses, comments with @mentions, and editing only work you own.
- A missing card is usually filtered out: check quick filters, column mapping, the board filter, and on Kanban boards the sub-filter and timeframe.
- The final challenge repeats the full workflow in a practice space on a theme of your choice.
- Lasting skill comes from small, regular improvements at work or in a sandbox.

## Top 10 things to remember

1. **Learn the logic, not the buttons.** The interface and the names change (space, work item, work type), but the concepts stay the same, and the classic JQL names `project` and `issue` keep working next to the new ones.
2. **Work items live in spaces; boards only show them.** When something is missing, check the board filter, quick filters, column mapping, and Kanban sub-filter before assuming it's gone.
3. **Structure before volume.** Use the hierarchy for breakdown, links for dependencies, and rank for order. Priority is only a field.
4. **Keep sprints honest.** Set a goal, commit to what fits based on story points and velocity, and send unfinished work back to the top of the backlog.
5. **Protect flow.** Set WIP limits below the team size, map every status to a column, keep the workflow to four or five statuses, and watch the CFD for widening bands.
6. **Organize with agreed conventions.** Consistent labels, components, and fix versions make every filter, board, and report work.
7. **Know the core of JQL.** `field operator value`, `currentUser()`, `is EMPTY`, relative dates, `statusCategory` across teams, and `ORDER BY rank ASC`.
8. **Save and share filters.** They power boards, dashboards, bulk changes, and other queries. Share viewers widely and keep editors few.
9. **Report from one scope and discuss, don't blame.** Put one filter behind related gadgets, and read burndown, velocity, and the control chart as prompts for team conversation.
10. **Automate small and communicate.** Build trigger, condition, and action rules in your own space, test them, and hand anything global to a Jira admin with a clear specification.

## Test yourself

Take the [final practice test](final-practice-test.md): 24 scenario questions that mix all ten sections, with a table that points each question to the lesson to review.
