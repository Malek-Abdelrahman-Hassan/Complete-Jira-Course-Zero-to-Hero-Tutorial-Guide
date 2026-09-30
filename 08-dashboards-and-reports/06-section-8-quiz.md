---
title: "Section 8 Quiz"
aliases:
  - "Section 8 Quiz"
type: quiz
section: 8
lesson: 6
duration: ""
status: done
tags:
  - jira
  - section/08
  - quiz
  - flashcards
---

# Section 8 Quiz

[Course home](../README.md) › [Section 8: Dashboards and Reports](README.md) › Quiz

> [!IMPORTANT]
> The official Udemy quiz questions are not reproduced here. The practice questions and flashcards below are original and cover the same topics.

## Topics covered

- [Creating Personal and Team Dashboards in Jira](01-personal-and-team-dashboards.md)
- [Useful Gadgets for Your Jira Dashboard: Filters, Charts, and More](02-useful-dashboard-gadgets.md)
- [Sharing and Cloning Dashboards with Stakeholders and Teams](03-sharing-and-cloning-dashboards.md)
- [Scrum Reports: Velocity, Burndown, and Sprint Report Explained](04-scrum-reports.md)
- [Kanban Reports: Control Chart and Cumulative Flow Diagram](05-kanban-reports.md)

## Practice questions

<details>
<summary>1. A stakeholder asks for a live list of all ABC release work items on one page, updated whenever they open it. Which dashboard building block do you need first?</summary>
A saved filter that returns the release work items. Gadgets such as Filter Results read from saved filters; the filter must exist and be shareable before the dashboard can show data.
</details>

<details>
<summary>2. You built a dashboard and typed a colleague's name as a viewer, but they still cannot see it. What step did you likely skip?</summary>
Clicking Add in the sharing dialog after entering their name. Names are not saved as viewers until you confirm each with Add.
</details>

<details>
<summary>3. On a burndown chart, the remaining-work line stays flat for three days while the gray guideline slopes downward. What does that pattern suggest?</summary>
Little or no progress toward completing sprint scope during those days—the team is not burning down planned work even though time is passing.
</details>

<details>
<summary>4. At sprint review, the Scrum Master opens the sprint report and sees several work items marked with an asterisk in the not-completed section. What should the team discuss?</summary>
Those items were added to the sprint after planning started—scope creep that may explain incomplete committed work and should inform future planning discipline.
</details>

<details>
<summary>5. On a velocity chart, the green completed bar is taller than the gray committed bar for the last four sprints. What planning adjustment might that suggest?</summary>
The team consistently finishes more than it commits—they may be under-planning and could take on slightly more work if capacity is stable.
</details>

<details>
<summary>6. A Kanban team's cumulative flow diagram shows the In progress band widening for two weeks while the Done band stays thin. What is the most likely interpretation?</summary>
Work is accumulating in In progress faster than it is finishing—a bottleneck or overload in that stage that warrants investigation (capacity, blockers, or WIP discipline).
</details>

<details>
<summary>7. The control chart average line is stable, but the shaded variation band suddenly widens. What should you do before changing team process?</summary>
Hover the outlier dots or clusters and inspect the completed work items—bulk closes of old backlog items or one-off exceptions often widen the band without reflecting everyday flow.
</details>

<details>
<summary>8. Filter Results and Pie Chart on the same dashboard both use the version 3.2 filter; Pie Chart is set to statistic type Status and Work item Statistics is also set to Status. Is this a good layout?</summary>
Probably not—you are showing the same breakdown twice in different visuals. Keep one status chart and use the other gadget for a different dimension (for example assignee) or remove the duplicate.
</details>

<details>
<summary>9. Where do you find burndown and velocity reports, and how is that different from a custom dashboard?</summary>
On the Scrum board under Reports—they are auto-generated from board sprint history. Custom dashboards are built from gadgets and saved filters you configure separately.
</details>

<details>
<summary>10. You want the same gadget layout for Version 3.3 that you used for Version 3.2, but with different filters. What is the safest approach?</summary>
Copy the Version 3.2 dashboard, rename it, and update each gadget to point at Version 3.3 filters—preserving the working 3.2 dashboard as a reference.
</details>

<details>
<summary>11. A wallboard in the team area shows some gadgets as blank boxes. What are two likely causes?</summary>
Those gadget types may not support wallboard mode, and/or viewers of the wallboard display lack permission to see the underlying saved filters even if the dashboard itself is shared.
</details>

<details>
<summary>12. On an epic report, the brown unestimated-issues line climbs while the blue completed area stays flat. What does that combination warn about?</summary>
New work is entering the epic without estimates while little is being completed—scope is growing without sizing, which undermines forecasting and progress tracking.
</details>

## Flashcards

What is a Jira dashboard?::A customizable page of gadgets that display live data, often from saved filters
What is a gadget?::A widget on a dashboard such as Filter Results, Pie Chart, or Created vs. Resolved Chart
What premade view does every board already have?::Summary—a built-in dashboard-style overview on the board
What do most reporting gadgets need as a data source?::A saved filter the viewer can access
What does Filter Results show?::A table of work items returned by a saved filter with chosen columns
What is the difference between Work item Statistics and Pie Chart?::Both aggregate a filter by one field; Work item Statistics uses bars, Pie Chart uses a pie
What does Created vs. Resolved Chart show?::How many work items were created versus resolved over a time period
What does Two Dimensional Filter Statistics show?::A table crossing two fields, for example assignee by status
Why are counts on filter gadgets clickable?::Each number links to a JQL search showing the work items in that segment
What must you click after typing a viewer name when sharing?::Add—otherwise the permission is not saved
What does Copy dashboard do?::Creates a new dashboard with the same gadgets and layout but new name and permissions
What is wallboard mode?::Fullscreen dashboard display with minimal Jira UI, often rotated on a timer
How do board reports differ from dashboards?::Reports are auto-generated per board; dashboards are custom gadget pages
Where do you open burndown and velocity charts?::Scrum board, Reports menu
What does the burndown gray guideline represent?::Ideal remaining work declining linearly from full scope to zero by sprint end
What does remaining work above the burndown guideline mean?::The sprint is likely off track—time is passing without enough completion
Which report is highlighted for sprint review?::Sprint report—completed, not completed, and mid-sprint additions
What does an asterisk on a sprint report item indicate?::The work item was added after sprint planning started
What does velocity chart gray vs green compare?::Committed (planned) story points vs completed story points per sprint
Green velocity bar consistently lower than gray?::Overcommitting—finishing less than planned each sprint
What does cycle time measure?::Time from starting active work until Done
What does a wide band on a control chart mean?::High variation—delivery timing is unpredictable
What does a widening CFD band indicate?::Work piling up in that status—likely a bottleneck
Which Kanban reports does the course prioritize?::Cumulative flow diagram and control chart

## Easy to confuse

| Concept A | Concept B | How to tell them apart |
|---|---|---|
| Dashboard | Board report | Dashboards are custom gadget pages you build. Board reports are auto-generated from one board's history under Reports. |
| Dashboard viewers | Filter viewers | Sharing a dashboard does not share its filters. Colleagues need permission on both or gadgets show empty. |
| Burndown chart | Burnup chart | Burndown tracks remaining work toward zero. Burnup tracks total scope and completed work on separate rising lines. |
| Velocity | Burndown | Velocity compares committed vs completed per sprint across history. Burndown tracks one sprint's remaining work over time. |
| Cycle time | Lead time | Cycle time starts when work actively begins. Lead time starts when the work item is created or requested. |
| Control chart | Cumulative flow diagram | Control chart plots how long finished items took. CFD shows how many items sit in each status over time. |
---

Previous: [Kanban Reports: Control Chart and Cumulative Flow Diagram](05-kanban-reports.md) · Next: [Section 9: Jira Automation](../09-automation/README.md)
