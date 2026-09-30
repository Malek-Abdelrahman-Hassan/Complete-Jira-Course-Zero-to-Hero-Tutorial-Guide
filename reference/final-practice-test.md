---
title: "Final Practice Test"
aliases:
  - "Final Practice Test"
type: reference
tags:
  - jira
  - reference
  - topic/review
---

# Final Practice Test

[Course home](../README.md) · Related: [Course Recap](course-recap.md)

Twenty-four scenario questions that mix all ten sections, in the style of problems that come up on real teams. Use the test after finishing the course, or as a quick check before starting, to see which sections need the most attention.

**How to take it**

1. Answer each question out loud or on paper before expanding the answer.
2. Give yourself one point for each answer that covers the main idea; small wording differences don't matter.
3. Score 20 or more out of 24 and the course material is solid. For each miss, open the lesson listed in *Where to review* at the end of this note.

> [!NOTE]
> These questions are original. They are not taken from the Udemy course quizzes, and they use the course's *Stamps and Points* example with the sample space keys `ABC` and `XYZ`.

## Part 1: Questions 1-12

<details>
<summary>1. An older guide says: "Create an issue in the project and set its issue type." How would you say that in current Jira terms, and does a saved query such as <code>project = ABC AND issuetype = Story</code> still work?</summary>
Create a work item in the space and set its work type. The query still works: the classic JQL names (project, issuetype, issue) keep working, while newer aliases such as space and workType are being rolled out and may not work everywhere yet.
Review: Section 1, Jira Has Changed: Products, Terminology & What You Need to Know.
</details>

<details>
<summary>2. A company is rolling Jira out to twelve teams that must follow one release workflow and report on the same fields. Which space type fits, and what does the choice mainly decide?</summary>
Company-managed spaces. Their workflows, work types, and fields are defined centrally by Jira admins and shared across many spaces, which keeps cross-team reporting consistent. The choice is mainly about governance: in team-managed spaces the team configures its own space; in company-managed spaces admins control shared configuration.
Review: Section 2, Team-Managed vs Company-Managed Spaces.
</details>

<details>
<summary>3. At the end of a sprint, three of eight stories are unfinished. What happens when you select Complete sprint, and where should the unfinished stories go?</summary>
Done items leave the board view but stay searchable, and Jira asks where to send the incomplete ones. Send them to the top of the backlog rather than straight into the next sprint, so the team re-plans them deliberately. Only completed stories count toward velocity.
Review: Section 3, Scrum Workflow in Jira: Sprints, Planning, and Execution.
</details>

<details>
<summary>4. The team wants to tag everything on a customer wishlist, spread across several epics and two spaces. Separately, a space admin wants every Payments work item to go to the payments lead automatically. Which Jira feature fits each need?</summary>
The wishlist needs a label: labels are free-form, anyone who can edit a work item can add them, and they work across epics and spaces. Payments needs a component: components are defined per space by admins and can have a component lead and a default assignee.
Review: Section 4, Using Issue Labels and Priorities to Organize Work in Jira, and Structuring Work with Components in Jira Projects.
</details>

<details>
<summary>5. A filter meant to show work in space ABC that is not assigned to you, <code>project = ABC AND assignee != currentUser()</code>, misses all the unassigned work items. Why, and how do you fix it?</summary>
The != operator does not match empty values, so work items with no assignee are skipped. Add an explicit check in parentheses: project = ABC AND (assignee != currentUser() OR assignee is EMPTY).
Review: Section 5, JQL Basics: What is Jira Query Language and Why It Matters.
</details>

<details>
<summary>6. An admin adds a new status, Ready for QA. As soon as a developer moves a story into it, the card disappears from the Scrum board and the backlog. What happened, and who can fix it?</summary>
The new status is not mapped to any board column, and unmapped statuses hide work items from both the board and the backlog. A board administrator (no Jira admin rights needed) opens Board settings, finds the status under Unmapped statuses on the columns page, and maps it to a column.
Review: Section 6, Customizing Your Jira Board View Without Admin Access.
</details>

<details>
<summary>7. For release 3.2.0, the development team works in space ABC (component iOS) and the app store team works in space XYZ (label SP app). How can both teams follow the release on one board without merging their backlogs?</summary>
Write one saved filter with an OR block per team and create a board from it: (project = ABC AND fixVersion = "3.2.0" AND component = iOS) OR (project = XYZ AND fixVersion = "3.2.0" AND labels = "SP app"). Each team keeps its own space and backlog; the shared board is only a view.
Review: Section 7, Creating and Using Shared Boards for Team Collaboration.
</details>

<details>
<summary>8. A team dashboard is shared with the whole organization, but colleagues see empty gadgets or errors. What is the most likely cause?</summary>
The gadgets read from saved filters that are still private. Sharing a dashboard does not share its filters. Share the filters with the same audience, or point the gadgets at filters the audience can already see.
Review: Section 8, Sharing and Cloning Dashboards with Stakeholders and Teams.
</details>

<details>
<summary>9. In a support space, closed tickets should reopen automatically when a customer adds a comment. Describe the automation rule.</summary>
Trigger: Work item commented. Condition: the status is Done. Action: Transition work item to the working status, such as In Progress. A space admin builds it under Space settings > Automation and tests it by commenting on a Done work item.
Review: Section 9, Examples of Simple Automation Rules for Teams.
</details>

<details>
<summary>10. A teammate says bug ABC-57 has vanished from the Kanban board, yet searching for the key opens it. In what order do you check, and what is the usual cause?</summary>
It is usually filtered out, not deleted. Check the active quick filters, then whether its status is mapped to a column, then the board's saved filter JQL, and on a Kanban board the sub-filter (often by fix version) and the timeframe that hides older completed work.
Review: Section 10, Where's My Issue? Troubleshooting Visibility Problems in Jira.
</details>

<details>
<summary>11. Someone deletes the team's old Kanban board by mistake. Is the team's work gone?</summary>
No. Boards are views over a saved filter; work items live in spaces. Deleting a board never deletes work items. Create a new board from the same filter to get the view back.
Review: Section 2, How Jira Is Structured: Spaces, Boards & Work Items.
</details>

<details>
<summary>12. A new teammate asks how many hours a 5-point story takes. How do you explain story points?</summary>
Story points measure relative size (effort, complexity, and uncertainty) compared with a baseline story the team agrees on; they are not hours. Over several sprints the team's velocity turns points into a forecast. Teams that prefer hours can switch the board's estimation setting to time.
Review: Section 3, Estimating with Story Points and Time in Agile Projects.
</details>

## Part 2: Questions 13-24

<details>
<summary>13. Write a query for bugs in space ABC created in the last seven days that are not done yet, listed in the same order as the board.</summary>
project = ABC AND issuetype = Bug AND created >= -7d AND statusCategory != Done ORDER BY rank ASC. Using statusCategory instead of a status name keeps the query correct even if the workflow's status names change.
Review: Section 5, Time-Based JQL Queries: Finding Issues by Date and Time.
</details>

<details>
<summary>14. A product manager sets five stories to Highest priority, but the team keeps starting other work first. Why?</summary>
Priority is only a field; it does not change backlog order. The team pulls from the top of the backlog, which follows rank (drag-and-drop order). Rank the urgent stories at the top, and use priority for filtering and reporting.
Review: Section 4, Using Issue Labels and Priorities to Organize Work in Jira.
</details>

<details>
<summary>15. A work item in To Do only offers In Progress in its status menu, but you want to close it directly. Why is Done missing, and what can you do?</summary>
The workflow allows only certain transitions from each status, and To Do has no direct transition to Done. Open View workflow from the status menu to see the path, move the work item through the allowed statuses, or ask a Jira admin to add a transition if the team really needs one. Regular users can view workflows but not edit them.
Review: Section 6, Workflow States and Transitions: What You Can See and Do.
</details>

<details>
<summary>16. Which Scrum report answers each question: (a) Are we on track in the middle of the sprint? (b) What was finished, not finished, added, or removed last sprint? (c) How much should we plan for next sprint?</summary>
(a) The burndown chart. (b) The sprint report. (c) The velocity chart, which shows committed and completed story points across recent sprints.
Review: Section 8, Scrum Reports: Velocity, Burndown, and Sprint Report Explained.
</details>

<details>
<summary>17. A shared board covers two spaces whose workflows use different names for work in progress (Doing and In development). How do you show and query that work consistently?</summary>
On the shared board, map both statuses into the same column. In JQL, query by status category instead of status names, and wrap the per-team OR block in parentheses before adding the category: (... OR ...) AND statusCategory = "In Progress".
Review: Section 7, What to Do When Statuses Don't Match Across Teams.
</details>

<details>
<summary>18. You are a space admin for one space and want a rule that emails the release manager whenever a Highest-priority work item is created in any of five spaces. What should you do?</summary>
Space admins can only automate their own space, so a multi-space rule needs a Jira admin. Prototype the rule in your own space, then send the admin a precise request: the trigger, conditions, actions, the spaces in scope, who is affected, and your test results. Announce the change to the affected teams.
Review: Section 9, When to Ask Admins for Help with Jira Automation.
</details>

<details>
<summary>19. On a Kanban board's cumulative flow diagram, the In review band gets wider every week while Done barely rises. What does that mean, and what are sensible first steps?</summary>
Work is entering review faster than it leaves, which is a bottleneck. Set or lower a WIP limit on the review column, have the team finish reviews before pulling new work, and check the control chart for work items stuck far longer than usual.
Review: Section 3, Understanding the Cumulative Flow Diagram for Kanban Teams.
</details>

<details>
<summary>20. Find every child of epic ABC-10 that is blocked by another work item. Then find everything linked to ABC-12, whatever the link type.</summary>
parent = ABC-10 AND issueLinkType = "is blocked by". Direction matters: "blocks" would instead return the items that block others. For everything linked to one work item: issue in linkedIssues(ABC-12).
Review: Section 5, Link-Based and Hierarchy JQL Queries for Advanced Filtering.
</details>

<details>
<summary>21. Every sprint the team repeats the same six-step planning checklist. Jira Cloud has no template library for work items. What is a practical pattern?</summary>
Create one master task with the checklist as subtasks (or in the description) and give it a template label. Each sprint, clone it, including subtasks, and work through the copy. A filter on labels = template finds the masters quickly.
Review: Section 4, Creating Templates and Reusable Tasks for Efficiency.
</details>

<details>
<summary>22. A manager wants to know whether the support backlog is growing or shrinking. Which gadget answers that, and how do you set it up?</summary>
The Created vs. Resolved Chart, pointed at a saved filter for the support space. If the created line stays above the resolved line, the backlog is growing. Click the numbers to see the work items behind each total.
Review: Section 8, Useful Gadgets for Your Jira Dashboard: Filters, Charts, and More.
</details>

<details>
<summary>23. You need a decision from a colleague about a work item they own. Where and how should you ask?</summary>
In a comment on the work item, with an @mention so they are notified and the decision stays in the work item's history. Avoid changing someone else's fields or status without agreement, and avoid moving the discussion to private chat where the context is lost.
Review: Section 10, Jira Etiquette: Do's and Don'ts for Real Teams.
</details>

<details>
<summary>24. On the Free plan, a lead wants to see epics from three spaces on one timeline with their dependencies. Is that possible?</summary>
Not with Timeline: it shows work items from one space only. Planning across spaces uses Plans (formerly Advanced Roadmaps), which comes with Jira Premium and Enterprise. On Free, use a shared board or dashboard across the spaces, and use each space's Timeline for its own dependencies.
Review: Section 7, Roadmaps in Jira: Visualizing Plans and Dependencies.
</details>

## Where to review

| Questions | Lesson |
|---|---|
| 1 | [Jira Has Changed: Products, Terminology & What You Need to Know](../01-introduction/03-jira-has-changed.md) |
| 2 | [Team-Managed vs Company-Managed Spaces](../02-jira-fundamentals/01-team-managed-vs-company-managed-spaces.md) |
| 11 | [How Jira Is Structured: Spaces, Boards & Work Items](../02-jira-fundamentals/06-how-jira-is-structured.md) |
| 3 | [Scrum Workflow in Jira: Sprints, Planning, and Execution](../03-agile-scrum-and-kanban/01-scrum-workflow-sprints.md) |
| 12 | [Estimating with Story Points and Time in Agile Projects](../03-agile-scrum-and-kanban/02-estimating-story-points-and-time.md) |
| 19 | [Understanding the Cumulative Flow Diagram for Kanban Teams](../03-agile-scrum-and-kanban/06-cumulative-flow-diagram.md) |
| 4, 14 | [Using Issue Labels and Priorities to Organize Work in Jira](../04-organizing-work/01-labels-and-priorities.md) |
| 4 | [Structuring Work with Components in Jira Projects](../04-organizing-work/02-components.md) |
| 21 | [Creating Templates and Reusable Tasks for Efficiency](../04-organizing-work/04-templates-and-reusable-tasks.md) |
| 5 | [JQL Basics: What is Jira Query Language and Why It Matters](../05-filters-and-jql/03-jql-basics.md) |
| 13 | [Time-Based JQL Queries: Finding Issues by Date and Time](../05-filters-and-jql/04-time-based-jql.md) |
| 20 | [Link-Based and Hierarchy JQL Queries for Advanced Filtering](../05-filters-and-jql/05-link-and-hierarchy-jql.md) |
| 6 | [Customizing Your Jira Board View Without Admin Access](../06-boards-and-workflows/01-customizing-board-view.md) |
| 15 | [Workflow States and Transitions: What You Can See and Do](../06-boards-and-workflows/02-workflow-states-and-transitions.md) |
| 7 | [Creating and Using Shared Boards for Team Collaboration](../07-cross-team-collaboration/02-shared-boards.md) |
| 24 | [Roadmaps in Jira: Visualizing Plans and Dependencies](../07-cross-team-collaboration/03-roadmaps-plans-and-dependencies.md) |
| 17 | [What to Do When Statuses Don't Match Across Teams](../07-cross-team-collaboration/04-mismatched-statuses-across-teams.md) |
| 22 | [Useful Gadgets for Your Jira Dashboard: Filters, Charts, and More](../08-dashboards-and-reports/02-useful-dashboard-gadgets.md) |
| 8 | [Sharing and Cloning Dashboards with Stakeholders and Teams](../08-dashboards-and-reports/03-sharing-and-cloning-dashboards.md) |
| 16 | [Scrum Reports: Velocity, Burndown, and Sprint Report Explained](../08-dashboards-and-reports/04-scrum-reports.md) |
| 9 | [Examples of Simple Automation Rules for Teams](../09-automation/03-simple-automation-rules.md) |
| 18 | [When to Ask Admins for Help with Jira Automation](../09-automation/04-when-to-ask-admins.md) |
| 23 | [Jira Etiquette: Do's and Don'ts for Real Teams](../10-best-practices/02-jira-etiquette.md) |
| 10 | [Where's My Issue? Troubleshooting Visibility Problems in Jira](../10-best-practices/03-wheres-my-issue-troubleshooting.md) |

For a broader refresh, reread the [Course Recap](course-recap.md) and redo the flashcards in each section's quiz note.
