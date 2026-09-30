---
title: "Roadmaps in Jira: Visualizing Plans and Dependencies"
aliases:
  - "Roadmaps in Jira: Visualizing Plans and Dependencies"
type: lesson
section: 7
lesson: 3
duration: "6:25"
status: done
tags:
  - jira
  - section/07
  - topic/roadmaps
---

# Roadmaps in Jira: Visualizing Plans and Dependencies

[Course home](../README.md) › [Section 7: Cross-Team Collaboration](README.md) › Lesson 3 · 6:25

## TL;DR

Jira's **Timeline** view (formerly called *roadmap* in a space) lays epics and work items on a calendar so you can see sprint placement, date overlap, and **dependencies** such as "blocks." On a single-space Scrum board you open **Timeline**, review epics in the current and future sprints, and drag link handles to create blocking links between items. Timeline only works with work items from one space. Planning across several spaces needs **Plans** (formerly *Advanced Roadmaps*), which comes with Jira Premium and Enterprise; the Free plan still lets you practice the same skills on one space.

## Key concepts

- **Timeline**: The schedule view inside a space or board (menu label **Timeline**; older material may say *roadmap*). Shows epics and child work items across sprints or dates.
- **Schedule by sprints vs dates**: Under **Board settings > Timeline**, choose whether the timeline follows **sprint dates** or **start and due dates** on work items. Scrum teams usually keep sprint-based scheduling.
- **Dependency link**: A relationship such as *blocks* between two work items. On the timeline, overlapping dates on linked items highlight planning conflicts.
- **Scope change from the timeline**: Dragging a work item into a sprint from the timeline adds it to that sprint and changes sprint scope — only do this with team agreement.
- **One space per timeline**: Timeline only shows work items from the backlog of one space, on every plan. A board whose filter pulls in several spaces has to be narrowed to one space for Timeline to work.
- **Plans for cross-space planning**: **Plans** (formerly *Advanced Roadmaps*) combines boards, spaces, and filters into one schedule with cross-team dependencies and capacity. It is included in Jira Premium and Enterprise only. The lesson describes this as needing Premium for a multi-space timeline.

## How to do it in Jira

### Open and configure the timeline

1. Open the *Stamps and Points* Scrum board and select **Timeline** in the board navigation (exact placement may vary slightly by Jira version).
2. Use a board whose filter includes only one space; Timeline does not work with multi-space boards. For cross-space views on a Premium site, create a plan under **Plans** instead.
3. To change scheduling mode: **Board settings** > **Timeline** (or similar) > choose **Sprint dates** or **Start and due dates**. For Scrum, prefer **Sprint dates**.

### Read the view

1. Epics in the active sprint appear on the timeline; expand an epic to see its child stories.
2. Items planned for a later sprint sit outside the current sprint band until moved.
3. Dependency lines connect linked work items (for example *ABC-35 blocks ABC-9*). Click a link to open dependency details.
4. Change the time scale — **Today**, **Weeks**, **Months**, or **Quarters** — to zoom planning horizons. Months is a practical default for medium-range planning.

### Plan ahead with sprints

1. In the **Backlog**, create a future sprint (for example Sprint 5) and set **start and end dates** (the course uses a two-week sprint starting the Monday after Sprint 4 ends).
2. Return to **Timeline** — the new sprint appears as a column on the schedule.
3. Click inside that sprint band to assign an epic or story. Confirm in the backlog that the item moved into Sprint 5.

### Create dependencies on the timeline

1. Hover a work item bar until a **link** icon appears.
2. Drag from that icon to the work item it **blocks**.
3. Jira creates the link; the timeline shows the relationship and warns when dates overlap in problematic ways.

### Refine what you see

Use timeline display options to:

- **Remove completed work** from the chart
- **Expand** or **collapse** all epics
- Toggle **dependencies**, **progress**, and **warnings**
- Apply **quick filters** (same family as on the board)
- **Group by status category** — for example show only **In Progress** items

## Examples

On the *Stamps and Points* board, epic *User profile* spans Sprint 4 while story `ABC-34` is planned for a later sprint — the timeline makes that split visible without opening each epic.

Story `ABC-35` **blocks** `ABC-9`, and both sit in the same sprint. The dependency line plus overlapping bars signal a sequencing risk: if `ABC-35` slips, `ABC-9` may stall.

Planning Sprint 5: create the sprint with dates in the backlog, open Timeline, and place `ABC-30` in Sprint 5. The epic now spans two sprints, which is visible at a glance — useful for release planning but easy to overuse.

On a Premium site, a plan that includes both the development space and the release space shows the same kind of dependency across teams: a development story can block an App Store submission task, surfacing handoff order on one schedule.

## Tips and pitfalls

- **Avoid long-range waterfall planning.** Creating many future sprints and filling them far ahead fights Agile reprioritization. Use the timeline for the next few sprints, not a fixed multi-quarter commitment.
- **Timeline edits change sprint scope.** Adding an item to a sprint from the timeline is the same as adding it in the backlog — discuss with the team first.
- **Timeline vs Plans.** Practice Timeline on one space on any plan. For several spaces, Timeline is not the tool; Plans is, and it needs Premium or Enterprise.
- **Sprint dates need dates.** Future sprints only appear meaningfully on the timeline when start and end dates are set.

> [!WARNING]
> Dragging work into sprints from the timeline without team agreement silently expands sprint commitment. Treat it like any other scope change.

> [!TIP]
> Toggle **warnings** and **dependencies** together when reviewing a release — overlapping bars on a *blocks* link often mean the plan needs reordering.

## Review questions

<details>
<summary>What is the Timeline view called in older Jira material?</summary>
Roadmap. The feature is now labeled Timeline in the board navigation for a space.
</details>

<details>
<summary>Why might a cross-space shared board not show Timeline, and what is the alternative?</summary>
Timeline only works with work items from one space, on every plan, so a board whose filter pulls from several spaces cannot use it. Cross-space planning uses Plans, which is included in Jira Premium and Enterprise.
</details>

<details>
<summary>What is the recommended schedule mode for a Scrum team?</summary>
Schedule by sprint dates, configured under board settings for Timeline. Start and due dates suit teams that do not plan by sprint.
</details>

<details>
<summary>How do you create a blocks dependency from the timeline?</summary>
Hover a work item until the link icon appears, then drag from that icon to the work item being blocked. Jira saves the link and draws it on the timeline.
</details>

<details>
<summary>What happens if you assign a backlog story to a future sprint from the timeline?</summary>
The work item joins that sprint, which changes sprint scope the same way adding it from the backlog would. The team should agree before doing this.
</details>

## Related

- [Glossary](../reference/glossary.md)
- [Parent-Child Hierarchy vs Linked Work Items](../02-jira-fundamentals/04-parent-child-vs-linked-work-items.md)
- [Link-Based and Hierarchy JQL Queries for Advanced Filtering](../05-filters-and-jql/05-link-and-hierarchy-jql.md)
- [Scrum Workflow in Jira: Sprints, Planning, and Execution](../03-agile-scrum-and-kanban/01-scrum-workflow-sprints.md)
- [Creating and Using Shared Boards for Team Collaboration](02-shared-boards.md)

---

Previous: [Creating and Using Shared Boards for Team Collaboration](02-shared-boards.md) · Next: [What to Do When Statuses Don't Match Across Teams](04-mismatched-statuses-across-teams.md)
