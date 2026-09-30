---
title: "Glossary"
aliases:
  - "Glossary"
  - "Jira glossary"
type: reference
tags:
  - jira
  - reference
---

# Glossary

[Course home](../README.md) · Related: [Jira Terminology Changes](jira-terminology-changes.md)

Jira and Agile terms used throughout the course, using current Jira Cloud names. Former names are shown in parentheses. Each entry links to the lesson where the term is covered.

## A

- **Action** (automation): The step a rule performs, such as assigning, commenting, editing a field, or transitioning the work item. See [What Can Be Automated in Jira by Non-Admins?](../09-automation/01-what-non-admins-can-automate.md)
- **Actions menu**: A compact menu of edits and transitions for the selected work item, opened with `.` (period). See [Pro Tips, Shortcuts, and Smart Habits for Jira Power Users](../10-best-practices/01-pro-tips-and-shortcuts.md)
- **Assignee**: The one person currently responsible for doing a work item. See [Create Work Items](../02-jira-fundamentals/03-create-epics-stories-subtasks.md)
- **Audit log** (automation): The history of a rule's runs, showing whether it fired and why it failed. The first place to look when a rule seems not to work. See [What Can Be Automated in Jira by Non-Admins?](../09-automation/01-what-non-admins-can-automate.md)
- **Automation rule**: A rule made of a *trigger* (what starts it), optional *conditions* (checks), and *actions* (what it does), which Jira runs automatically. Example: "when a work item is created, assign it to the reporter". See [What Can Be Automated in Jira by Non-Admins?](../09-automation/01-what-non-admins-can-automate.md)

## B

- **Backlog**: The ordered list of work that has not started yet. In Scrum, sprint planning moves work from the backlog into a sprint. See [Scrum Workflow in Jira](../03-agile-scrum-and-kanban/01-scrum-workflow-sprints.md)
- **Backlog rank**: The order of work items in the backlog, set by drag-and-drop. It is the main way to say what comes next and is separate from the *Priority* field. See [Using Issue Labels and Priorities to Organize Work in Jira](../04-organizing-work/01-labels-and-priorities.md)
- **Baseline story**: A typical work item the team agrees on as a reference size (for example 5 points). Other work is estimated as smaller or larger than it. See [Estimating with Story Points and Time in Agile Projects](../03-agile-scrum-and-kanban/02-estimating-story-points-and-time.md)
- **Basic search**: The point-and-click search form with field dropdowns. It covers common criteria, and switching to JQL shows the equivalent query. See [Using Basic Search and Quick Filters in Jira](../05-filters-and-jql/01-basic-search-and-quick-filters.md)
- **Board**: A visual view of work items in columns that represent workflow statuses. A board is a view, not a container: it shows whatever its board filter returns, and deleting it doesn't delete any work items. See [Understanding Jira Boards](../02-jira-fundamentals/05-boards-scrum-kanban-filters.md)
- **Board administrator**: Someone who can open **Board settings** for a specific board and change its columns, swimlanes, card layout, quick filters, and filter. Separate from Jira site administration. See [Customizing Your Jira Board View Without Admin Access](../06-boards-and-workflows/01-customizing-board-view.md)
- **Board filter**: The saved filter that decides which work items a board can show. It can span several spaces. See [Customizing Your Jira Board View Without Admin Access](../06-boards-and-workflows/01-customizing-board-view.md)
- **Board Summary**: A ready-made, non-customizable overview page for a board, with status breakdowns, epic progress, and recent activity. See [Creating Personal and Team Dashboards in Jira](../08-dashboards-and-reports/01-personal-and-team-dashboards.md)
- **Branch** (automation): A part of a rule that applies actions to related work items, such as every subtask of the trigger's work item. See [What Can Be Automated in Jira by Non-Admins?](../09-automation/01-what-non-admins-can-automate.md)
- **Bug**: A work type for a problem that stops something from working as intended. See [Understanding Jira Work Types & Hierarchy](../02-jira-fundamentals/02-work-types-and-hierarchy.md)
- **Bulk change**: Applying the same update (edit fields, transition, move, delete, watch) to many selected work items at once. Found under **More actions (⋯) > Bulk change work items** in search results. See [Creating and Saving Filters in Jira for Quick Access](../05-filters-and-jql/02-creating-and-saving-filters.md)
- **Burndown chart**: A Scrum report that plots the work remaining in a sprint against time, compared with a gray guideline. See [Scrum Reports](../08-dashboards-and-reports/04-scrum-reports.md)
- **Burnup chart**: A Scrum report that shows total scope and completed work as separate lines, so scope growth is visible. See [Scrum Reports](../08-dashboards-and-reports/04-scrum-reports.md)

## C

- **Card layout**: The board setting that chooses which extra fields (for example story points or days in column) appear on cards. See [Visualizing Work with WIP Limits and Swimlanes in Jira](../03-agile-scrum-and-kanban/05-wip-limits-and-swimlanes.md)
- **Checklist**: A list of items to tick off inside a single work item, such as a Definition of Done. Usually added through a Marketplace app. See [Smart Checklists](../09-automation/02-smart-checklists.md)
- **Checklist template**: A saved checklist (for example code review, tests passed, docs updated) that can be imported into any work item. See [Smart Checklists](../09-automation/02-smart-checklists.md)
- **Clone**: An action that copies a work item, optionally with its subtasks, into a new work item with a new key. See [Creating Templates and Reusable Tasks for Efficiency](../04-organizing-work/04-templates-and-reusable-tasks.md)
- **Company-managed space** (formerly *classic project*): A space whose configuration, such as workflows, fields, and screens, is controlled by Jira admins and can be shared by many spaces. See [Team-Managed vs Company-Managed Spaces](../02-jira-fundamentals/01-team-managed-vs-company-managed-spaces.md)
- **Completed issues** (Kanban board setting): How long done work items stay visible on a Kanban board, for example two weeks. Older done work disappears from the board but still exists. See [Customizing Your Jira Board View Without Admin Access](../06-boards-and-workflows/01-customizing-board-view.md)
- **Component**: A named subsection of a space (for example *iOS*, *Android*, *API*) used to group work items. Components are managed by space admins and can have a lead and a default assignee. Not to be confused with Compass components. See [Structuring Work with Components in Jira Projects](../04-organizing-work/02-components.md)
- **Component lead**: The person responsible for a component, who can also be its default assignee. See [Structuring Work with Components in Jira Projects](../04-organizing-work/02-components.md)
- **Condition** (automation): A check that must pass before a rule continues, such as "status equals Done". See [What Can Be Automated in Jira by Non-Admins?](../09-automation/01-what-non-admins-can-automate.md)
- **Condition** (workflow): A rule that decides whether a transition is offered at all, for example only to the assignee. See [Navigating Complex Workflows Without Getting Lost in Jira](../06-boards-and-workflows/03-navigating-complex-workflows.md)
- **Control chart**: A report of cycle time per work item, shown as dots with an average line and a variation band. It helps spot outliers and judge predictability. See [Kanban Reports](../08-dashboards-and-reports/05-kanban-reports.md)
- **Cumulative flow diagram (CFD)**: A stacked area chart of how many work items are in each status over time. A band that keeps widening points to a bottleneck. See [Understanding the Cumulative Flow Diagram for Kanban Teams](../03-agile-scrum-and-kanban/06-cumulative-flow-diagram.md)
- **Cycle time**: The time from when work actually starts to when it is done. Compare with *lead time*. See [Kanban Reports](../08-dashboards-and-reports/05-kanban-reports.md)

## D

- **Daily standup** (daily scrum): A short daily meeting in which the team syncs on progress and blockers, run from the board. See [Running Daily Standups with Jira](../03-agile-scrum-and-kanban/03-daily-standups.md)
- **Dashboard**: A page of gadgets that display information from filters, such as charts, lists, and statistics. It can be private or shared with viewers and editors. See [Creating Personal and Team Dashboards in Jira](../08-dashboards-and-reports/01-personal-and-team-dashboards.md)
- **Date function** (JQL): A calculated boundary such as `startOfWeek()` or `endOfMonth()`, optionally with an offset like `startOfWeek(-1)`. See [Time-Based JQL Queries](../05-filters-and-jql/04-time-based-jql.md)
- **Days in column**: A card-layout option that shows, as dots, how long a work item has stayed in its current column. See [Customizing Your Jira Board View Without Admin Access](../06-boards-and-workflows/01-customizing-board-view.md)
- **Default assignee**: Who new work items are assigned to automatically, for example the component lead when a component is selected. See [Structuring Work with Components in Jira Projects](../04-organizing-work/02-components.md)
- **Definition of Done (DoD)**: A shared list of conditions a work item must meet before it counts as done, often kept as a checklist template. See [Smart Checklists](../09-automation/02-smart-checklists.md)
- **Dependency link**: A link such as *blocks / is blocked by* between work items, shown on the timeline so conflicting dates stand out. See [Roadmaps in Jira](../07-cross-team-collaboration/03-roadmaps-plans-and-dependencies.md)

## E

- **Epic**: A large body of work that is broken down into smaller work items such as stories, tasks, and bugs. It sits above them in the hierarchy. See [Understanding Jira Work Types & Hierarchy](../02-jira-fundamentals/02-work-types-and-hierarchy.md)
- **Epic Link** (retired field): The older field that connected a work item to its epic. The *Parent* field replaced it, and JQL retired `"Epic Link"` in February 2024: filters saved before then still run, but new filters must use `parent`. See [Link-Based and Hierarchy JQL Queries for Advanced Filtering](../05-filters-and-jql/05-link-and-hierarchy-jql.md)
- **Epic panel**: The backlog side panel that lists epics and their progress. Epics don't appear in the main backlog list. See [Create Work Items](../02-jira-fundamentals/03-create-epics-stories-subtasks.md)
- **Epic report**: A report of one epic's total and completed scope over time, including a line for unestimated work items. See [Scrum Reports](../08-dashboards-and-reports/04-scrum-reports.md)
- **Estimate**: A forecast of effort, either in story points (relative size) or in time (original and remaining estimate). See [Estimating with Story Points and Time in Agile Projects](../03-agile-scrum-and-kanban/02-estimating-story-points-and-time.md)

## F

- **Fibonacci scale**: The Agile estimation scale 1, 2, 3, 5, 8, 13, 20 (sometimes 40 and 100), a simplified form of the Fibonacci sequence. The growing gaps reflect growing uncertainty in larger work. See [Estimating with Story Points and Time in Agile Projects](../03-agile-scrum-and-kanban/02-estimating-story-points-and-time.md)
- **Filter** (saved filter): A saved search, written in JQL. Filters power boards, dashboard gadgets, and subscriptions, and have their own viewers and editors. See [Creating and Saving Filters in Jira for Quick Access](../05-filters-and-jql/02-creating-and-saving-filters.md)
- **Fix version**: The version (release) in which a work item is planned to ship. See [Planning and Releasing with Versions in Jira](../04-organizing-work/03-versions-and-releases.md)
- **Flow**: How smoothly work moves from start to done. Kanban aims to keep it steady and predictable. See [Working with Kanban](../03-agile-scrum-and-kanban/04-kanban-managing-flow.md)
- **Function** (JQL): A named calculation that returns values, such as `currentUser()`, `startOfWeek()`, or `linkedIssues()`. See [JQL Basics](../05-filters-and-jql/03-jql-basics.md)

## G

- **Gadget**: A widget on a dashboard, for example *Filter Results*, *Work item Statistics* (formerly *Issue Statistics*), *Pie Chart*, *Created vs. Resolved Chart*, or *Two Dimensional Filter Statistics*. See [Useful Gadgets for Your Jira Dashboard](../08-dashboards-and-reports/02-useful-dashboard-gadgets.md)
- **Global automation**: Site-wide automation managed by Jira admins, for rules that span several spaces. See [When to Ask Admins for Help with Jira Automation](../09-automation/04-when-to-ask-admins.md)
- **Global transition**: A workflow transition from any status (shown as "Any") to one target status. See [Workflow States and Transitions](../06-boards-and-workflows/02-workflow-states-and-transitions.md)

## I

- **`issueLinkType`** (JQL field): Finds work items that have a given kind of link, for example `issueLinkType = blocks`. Atlassian's newer name for it is `workItemLinkType`. See [Link-Based and Hierarchy JQL Queries for Advanced Filtering](../05-filters-and-jql/05-link-and-hierarchy-jql.md)

## J

- **Jira admin**: A site-level administrator who manages global settings, schemes, users, and global automation. Compare with *space admin*. See [What Can Be Automated in Jira by Non-Admins?](../09-automation/01-what-non-admins-can-automate.md)
- **Jira Automation**: Jira's built-in, no-code rule engine. See [What Can Be Automated in Jira by Non-Admins?](../09-automation/01-what-non-admins-can-automate.md)
- **Jira Cloud**: The version of Jira hosted by Atlassian, and the one the course uses. It gets new features first. See [Jira Has Changed](../01-introduction/03-jira-has-changed.md)
- **Jira Data Center**: The self-managed version of Jira that runs on a company's own servers. New customers could no longer buy it after March 30, 2026, and it reaches end of life on March 28, 2029. See [Jira Has Changed](../01-introduction/03-jira-has-changed.md)
- **JQL (Jira Query Language)**: The structured language for searching work items. A clause has the form `field operator value`; clauses are combined with `AND` / `OR` and sorted with `ORDER BY`. See [JQL Basics](../05-filters-and-jql/03-jql-basics.md) and the [JQL Cheat Sheet](jql-cheat-sheet.md)

## K

- **Kanban**: An Agile method built around continuous flow: visualize the work, limit work in progress, and improve flow, with no fixed-length iterations. See [Working with Kanban](../03-agile-scrum-and-kanban/04-kanban-managing-flow.md)
- **Kanban backlog**: An optional backlog view on a Kanban board, made by mapping a status to the backlog column instead of to the board. See [Understanding Jira Boards](../02-jira-fundamentals/05-boards-scrum-kanban-filters.md)
- **Kanban sub-filter**: An extra JQL clause on a Kanban board, commonly used to hide work items from released versions. See [Customizing Your Jira Board View Without Admin Access](../06-boards-and-workflows/01-customizing-board-view.md)
- **Keyboard shortcut**: A key or key sequence that runs an action without the mouse, such as `c` (create) or `/` (search). Press `?` for the full list. See [Keyboard Shortcuts](keyboard-shortcuts.md)

## L

- **Label**: A free-form tag that anyone who can edit a work item can add. Labels are shared across the whole site and are useful for grouping across spaces. See [Using Issue Labels and Priorities to Organize Work in Jira](../04-organizing-work/01-labels-and-priorities.md)
- **Lead time**: The time from when a work item is created (requested) to when it is done.
- **Link** (work item link): A relationship between two work items that are not parent and child, such as *blocks / is blocked by*, *relates to*, *duplicates*, or *clones*. Links work across spaces of either management type. See [Parent-Child Hierarchy vs Linked Work Items](../02-jira-fundamentals/04-parent-child-vs-linked-work-items.md)
- **`linkedIssues()`** (JQL function): Returns the work items linked to a given key, optionally only for one link type, for example `issue in linkedIssues(ABC-9, "is blocked by")`. See [Link-Based and Hierarchy JQL Queries for Advanced Filtering](../05-filters-and-jql/05-link-and-hierarchy-jql.md)
- **List view**: A spreadsheet-like layout of work items with configurable columns and inline editing. See [Pro Tips, Shortcuts, and Smart Habits for Jira Power Users](../10-best-practices/01-pro-tips-and-shortcuts.md)

## M

- **Marketplace app**: An add-on from the Atlassian Marketplace that extends Jira, such as a checklist app. Installing apps usually needs a Jira admin. See [Smart Checklists](../09-automation/02-smart-checklists.md)

## N

- **Nested filter**: A saved filter reused inside another query with `filter = "Filter name"`. See [Useful JQL Examples for Real Work](../05-filters-and-jql/06-useful-jql-examples.md)
- **Notification scheme**: The admin-managed setting that decides which events email which people. See [Jira Etiquette](../10-best-practices/02-jira-etiquette.md)

## O

- **Operator** (JQL): The comparison in a clause, such as `=`, `!=`, `>=`, `in`, `is EMPTY`, or `~`. See [JQL Basics](../05-filters-and-jql/03-jql-basics.md)
- **Original estimate**: The time-based estimate of a work item, entered with units such as `4h`, `2d`, or `1w`. See [Estimating with Story Points and Time in Agile Projects](../03-agile-scrum-and-kanban/02-estimating-story-points-and-time.md)

## P

- **Parent**: The work item directly above another in the hierarchy: an epic is the parent of a story, and a story is the parent of a subtask. The *Parent* field replaced the older *Epic Link* and *Parent Link* fields. A parent-child chain can cross spaces only when both spaces have the same management type. See [Parent-Child Hierarchy vs Linked Work Items](../02-jira-fundamentals/04-parent-child-vs-linked-work-items.md)
- **Plans** (formerly *Advanced Roadmaps*): A feature in Jira Premium and Enterprise for planning across several teams and spaces, with cross-team dependencies and capacity. The course mentions it only as the Premium option for multi-space timelines. See [Roadmaps in Jira](../07-cross-team-collaboration/03-roadmaps-plans-and-dependencies.md)
- **Post function**: An action Jira runs automatically after a transition, such as setting a field or sending a notification. See [Navigating Complex Workflows Without Getting Lost in Jira](../06-boards-and-workflows/03-navigating-complex-workflows.md)
- **Priority**: How urgent a work item is compared with others. The default levels are Highest, High, Medium, Low, and Lowest. Priority doesn't change backlog order. See [Using Issue Labels and Priorities to Organize Work in Jira](../04-organizing-work/01-labels-and-priorities.md)

## Q

- **Query swimlane**: A swimlane defined by a JQL query, such as `labels = blocked`, that gives matching cards their own row. See [Visualizing Work with WIP Limits and Swimlanes in Jira](../03-agile-scrum-and-kanban/05-wip-limits-and-swimlanes.md)
- **Quick filter**: A one-click JQL filter on a board, such as *Only my work items* or *Recently updated*, that narrows down what the board shows. See [Using Basic Search and Quick Filters in Jira](../05-filters-and-jql/01-basic-search-and-quick-filters.md)

## R

- **Rank**: The hidden ordering field behind backlog order. Adding `ORDER BY rank ASC` makes a filter list work items in board order. See [JQL Basics](../05-filters-and-jql/03-jql-basics.md)
- **Relative date** (JQL): An offset from now, such as `-7d`, `-2w`, or `-5h`, used with date fields like `created` and `updated`. See [Time-Based JQL Queries](../05-filters-and-jql/04-time-based-jql.md)
- **Release**: Shipping a version. Releasing a version in Jira marks it as released on a date and can move unfinished work to another version. See [Planning and Releasing with Versions in Jira](../04-organizing-work/03-versions-and-releases.md)
- **Release notes**: A generated summary of the work items in a version, which can be edited before sharing. See [Planning and Releasing with Versions in Jira](../04-organizing-work/03-versions-and-releases.md)
- **Reopened status**: A status for work that came back after being done or rejected in review, kept separate from new *To Do* work. See [Navigating Complex Workflows Without Getting Lost in Jira](../06-boards-and-workflows/03-navigating-complex-workflows.md)
- **Reporter**: The person who created or reported the work item. See [Create Work Items](../02-jira-fundamentals/03-create-epics-stories-subtasks.md)
- **Resolution**: A field that records *how* a work item was closed, for example *Done*, *Won't Do*, or *Duplicate*. It is set when the work item reaches a done status. In the course demo it stays even after the work item is reopened, so choose it carefully; only an admin-configured transition can clear it. Many reports and queries such as `resolution = Unresolved` depend on it. See [Workflow States and Transitions](../06-boards-and-workflows/02-workflow-states-and-transitions.md)
- **Roadmap**: See *Timeline* and *Plans*.
- **Rovo**: Atlassian's AI assistant, used for search, chat, and agents. Useful for asking why a setting or action is missing. Included in the paid plans (Standard, Premium, Enterprise) and their trials, not in the Free plan. See [Jira Has Changed](../01-introduction/03-jira-has-changed.md)
- **Rule owner**: The person responsible for an automation rule, who is notified when it fails. See [What Can Be Automated in Jira by Non-Admins?](../09-automation/01-what-non-admins-can-automate.md)
- **Rule scope**: Where an automation rule applies: one space, several spaces, or the whole site. Anything beyond one space needs a Jira admin. See [When to Ask Admins for Help with Jira Automation](../09-automation/04-when-to-ask-admins.md)
- **Rule template**: A ready-made automation rule to start from instead of building one from scratch. See [What Can Be Automated in Jira by Non-Admins?](../09-automation/01-what-non-admins-can-automate.md)

## S

- **Scope creep**: Work added to a sprint after it started. The sprint report marks such work items with an asterisk. See [Scrum Reports](../08-dashboards-and-reports/04-scrum-reports.md)
- **Scrum**: An Agile framework that delivers work in fixed-length iterations called sprints. Its events are sprint planning, the daily scrum, sprint review, and retrospective. See [Scrum Workflow in Jira](../03-agile-scrum-and-kanban/01-scrum-workflow-sprints.md)
- **Scrum board**: A board built around a backlog and sprints. See [Understanding Jira Boards](../02-jira-fundamentals/05-boards-scrum-kanban-filters.md)
- **Shared board**: A board built on a saved filter that pulls work from several spaces, often with an `OR` between each team's scope. See [Creating and Using Shared Boards for Team Collaboration](../07-cross-team-collaboration/02-shared-boards.md)
- **Site**: A Jira Cloud instance such as `your-team.atlassian.net`. It contains all spaces, users, and settings. See [Set Up Your Free Jira Cloud Site (Optional Hands-On Setup)](../01-introduction/04-set-up-free-jira-cloud-site.md)
- **Smart Checklist for Jira**: The Marketplace checklist app used in the course. Its free tier limits the number of templates. See [Smart Checklists](../09-automation/02-smart-checklists.md)
- **Smart value**: A placeholder in an automation rule, such as `{{issue.key}}`, that is filled with live data when the rule runs. See [What Can Be Automated in Jira by Non-Admins?](../09-automation/01-what-non-admins-can-automate.md)
- **Space** (formerly *project*): A container for work items with its own settings, boards, and permissions. See [How Jira Is Structured](../02-jira-fundamentals/06-how-jira-is-structured.md)
- **Space admin**: Someone who manages one space's settings, such as components, versions, and space automation. Compare with *Jira admin*. See [What Can Be Automated in Jira by Non-Admins?](../09-automation/01-what-non-admins-can-automate.md)
- **Space key**: The short code chosen when a space is created (for example `ABC`). It prefixes every work item key in that space. It can be changed later under **Space settings > Details**, but filters and gadgets that name the old key must then be updated. See [Team-Managed vs Company-Managed Spaces](../02-jira-fundamentals/01-team-managed-vs-company-managed-spaces.md)
- **Sprint**: A fixed timebox, usually 1-4 weeks, in which a Scrum team completes a planned set of work. See [Scrum Workflow in Jira](../03-agile-scrum-and-kanban/01-scrum-workflow-sprints.md)
- **Sprint goal**: A short statement of the most important outcome of a sprint, set when the sprint starts. See [Scrum Workflow in Jira](../03-agile-scrum-and-kanban/01-scrum-workflow-sprints.md)
- **Sprint insights**: A board panel that shows sprint progress, such as work by status and by epic. Useful during standups. See [Running Daily Standups with Jira](../03-agile-scrum-and-kanban/03-daily-standups.md)
- **Sprint report**: A report listing the work completed, not completed, and added or removed during a sprint. See [Scrum Reports](../08-dashboards-and-reports/04-scrum-reports.md)
- **Start standup**: A board option that runs a timed standup, moving through team members one by one. See [Running Daily Standups with Jira](../03-agile-scrum-and-kanban/03-daily-standups.md)
- **Status**: The current state of a work item in its workflow, such as *To Do*, *In Progress*, *In Review*, or *Done*. See [Workflow States and Transitions](../06-boards-and-workflows/02-workflow-states-and-transitions.md)
- **Status category**: The group a status belongs to: *To Do* (gray), *In Progress* (blue), or *Done* (green). Reports and the JQL field `statusCategory` rely on it, which makes it useful when teams use different status names. See [Workflow States and Transitions](../06-boards-and-workflows/02-workflow-states-and-transitions.md)
- **Status mapping**: Assigning each workflow status to a board column in **Board settings > Columns**. See *Unmapped status*. See [Visualizing Work with WIP Limits and Swimlanes in Jira](../03-agile-scrum-and-kanban/05-wip-limits-and-swimlanes.md)
- **Story**: A work type that describes functionality from the user's point of view, often written as "As a ..., I want ..., so that ...". See [Understanding Jira Work Types & Hierarchy](../02-jira-fundamentals/02-work-types-and-hierarchy.md)
- **Story points**: A relative unit for estimating the effort and complexity of work, used instead of hours. See [Estimating with Story Points and Time in Agile Projects](../03-agile-scrum-and-kanban/02-estimating-story-points-and-time.md)
- **Subtask** (formerly *sub-task*): A work item that splits a story, task, or bug into smaller steps. It is the lowest level of the default hierarchy. See [Understanding Jira Work Types & Hierarchy](../02-jira-fundamentals/02-work-types-and-hierarchy.md)
- **Summary**: The short title of a work item, shown on cards and in search results. See [Jira Etiquette](../10-best-practices/02-jira-etiquette.md)
- **Swimlane**: A horizontal row on a board that groups cards, for example by assignee, by epic, or by a query. See [Visualizing Work with WIP Limits and Swimlanes in Jira](../03-agile-scrum-and-kanban/05-wip-limits-and-swimlanes.md)

## T

- **Task**: A work type for a piece of work that needs doing and isn't necessarily user-facing. See [Understanding Jira Work Types & Hierarchy](../02-jira-fundamentals/02-work-types-and-hierarchy.md)
- **Team-managed space** (formerly *next-gen project*): A space configured by its own space admins, with settings that don't affect other spaces. See [Team-Managed vs Company-Managed Spaces](../02-jira-fundamentals/01-team-managed-vs-company-managed-spaces.md)
- **Template work item**: A labeled "master" work item that holds a standard description and subtasks, cloned whenever the process repeats. See [Creating Templates and Reusable Tasks for Efficiency](../04-organizing-work/04-templates-and-reusable-tasks.md)
- **Text search** (`~`): The JQL "contains" operator for text fields, for example `summary ~ "points"`. See [Useful JQL Examples for Real Work](../05-filters-and-jql/06-useful-jql-examples.md)
- **Time tracking**: Logging time spent on a work item and comparing it with the original estimate. See [Estimating with Story Points and Time in Agile Projects](../03-agile-scrum-and-kanban/02-estimating-story-points-and-time.md)
- **Timeline** (formerly *roadmap* in a space): The view for planning epics and their child work items over time, including dependencies. It shows work from one space only; planning across spaces uses *Plans*. See [Roadmaps in Jira](../07-cross-team-collaboration/03-roadmaps-plans-and-dependencies.md)
- **Transition**: A move from one status to another. The workflow defines which transitions are allowed, so the status dropdown only offers the moves available from the current status. See [Workflow States and Transitions](../06-boards-and-workflows/02-workflow-states-and-transitions.md)
- **Transition screen**: A form that appears during a transition, for example to choose a resolution or add a comment. See [Navigating Complex Workflows Without Getting Lost in Jira](../06-boards-and-workflows/03-navigating-complex-workflows.md)
- **Trigger** (automation): The event that starts a rule, such as *Work item created* or *Work item commented*. See [What Can Be Automated in Jira by Non-Admins?](../09-automation/01-what-non-admins-can-automate.md)

## U

- **Unmapped status**: A workflow status that isn't assigned to any board column. Work items in it disappear from the board, and on Scrum boards from the backlog too, even though search still finds them. See [What to Do When Statuses Don't Match Across Teams](../07-cross-team-collaboration/04-mismatched-statuses-across-teams.md)

## V

- **Validator**: A workflow check that runs during a transition and blocks it if the input is invalid, such as a missing comment. See [Navigating Complex Workflows Without Getting Lost in Jira](../06-boards-and-workflows/03-navigating-complex-workflows.md)
- **Velocity**: The amount of work, usually in story points, that a Scrum team completes per sprint. The velocity chart compares committed (gray) and completed (green) work and is used for forecasting. See [Scrum Reports](../08-dashboards-and-reports/04-scrum-reports.md)
- **Version**: A planned release that groups work items through the *Fix versions* field. See [Planning and Releasing with Versions in Jira](../04-organizing-work/03-versions-and-releases.md)

## W

- **Wallboard**: A full-screen display of a dashboard for a team monitor. See [Sharing and Cloning Dashboards with Stakeholders and Teams](../08-dashboards-and-reports/03-sharing-and-cloning-dashboards.md)
- **Watcher**: Someone who gets notifications about changes to a work item without being its assignee. See [Jira Etiquette](../10-best-practices/02-jira-etiquette.md)
- **WIP limit** (work-in-progress limit): The maximum number of work items allowed in a board column at the same time. Going over it turns the column red as a warning; Jira doesn't block the move. See [Visualizing Work with WIP Limits and Swimlanes in Jira](../03-agile-scrum-and-kanban/05-wip-limits-and-swimlanes.md)
- **Work item** (formerly *issue*): Any unit of work tracked in Jira, such as an epic, story, task, bug, or subtask. See [Jira Has Changed](../01-introduction/03-jira-has-changed.md)
- **Work item key**: The unique ID of a work item, made of the space key and a number, such as `ABC-123`. Numbers are never reused. See [Create Work Items](../02-jira-fundamentals/03-create-epics-stories-subtasks.md)
- **Work type** (formerly *issue type*): The kind of work item: Epic, Story, Task, Bug, Subtask, or a custom type. See [Understanding Jira Work Types & Hierarchy](../02-jira-fundamentals/02-work-types-and-hierarchy.md)
- **Workflow**: The set of statuses and transitions a work item moves through from creation to completion. See [Workflow States and Transitions](../06-boards-and-workflows/02-workflow-states-and-transitions.md)
- **Workflow scheme**: The admin setting that assigns workflows to a space's work types. See [Navigating Complex Workflows Without Getting Lost in Jira](../06-boards-and-workflows/03-navigating-complex-workflows.md)
