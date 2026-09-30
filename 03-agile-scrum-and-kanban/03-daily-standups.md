---
title: "Running Daily Standups with Jira: Best Practices"
aliases:
  - "Running Daily Standups with Jira: Best Practices"
type: lesson
section: 3
lesson: 3
duration: "6:11"
status: done
tags:
  - jira
  - section/03
  - topic/scrum
  - topic/standups
---

# Running Daily Standups with Jira: Best Practices

[Course home](../README.md) › [Section 3: Agile in Jira: Scrum and Kanban](README.md) › Lesson 3 · 6:11

## TL;DR

A daily standup is a short (~15 minute) Scrum ceremony where each teammate shares progress, plans, and blockers. Jira supports standups on the active sprint board through assignee and epic filters, quick filters, swimlane grouping, a built-in **Start standup** timer, and live **Sprint insights** including a story-point burndown. The goal is shared awareness and fast blocker resolution—not a status report to a manager.

## Key concepts

- **Daily standup**: A regular team check-in, usually 15 minutes, focused on what was done, what is in progress, and what is blocking progress.
- **Board-as-source-of-truth**: The active sprint board shows current work. Filters and swimlanes let the team walk through updates person by person or epic by epic.
- **Quick filters**: Saved one-click filters on the board. Every new board includes **Assigned to me** and **Recently updated**; teams can add custom filters (for example, a `blocked` label).
- **Start standup**: A board tool (under the **⋯** menu) that opens a timed panel for each participant, signaling when to wrap up and move on.
- **Sprint insights**: A live panel showing sprint health, story-point burndown, timeline progress, and completion by epic.

## How to do it in Jira

1. Open the **Scrum board** and make sure an **active sprint** is running.
2. **Filter by person**: click a teammate's avatar to show only their assigned work items. Clear the filter before selecting the next speaker.
3. **Check unassigned work**: include unassigned items so nothing is overlooked.
4. Use additional filters as needed:
   - **Epics** panel to focus on one epic at a time
   - **Work type** filter to show only stories or only subtasks
   - **Label** filter—for example, items labeled `blocked`
   - **Quick filters** such as **Assigned to me** or a custom blocked filter
5. **Group into swimlanes**: open **Sprint details** (or the board grouping menu) and choose **Group by** assignee, epic, or other options. Assignee grouping creates horizontal lanes—one per person plus unassigned at the bottom.
6. **Run a timed standup**: open **⋯** > **Start standup**. Select the current speaker, start the timer (for example, two minutes per person), and advance when time expires. An alert sounds if someone runs over.
7. **Monitor sprint health**: in **Sprint insights**, review the burndown chart (based on story points), overall progress percentage, and per-epic completion. Refresh after completing work to see the line move.

## Examples

During standup on the *Stamps and Points* board, the team groups by **Assignee**. Each developer filters to their lane and mentions a story moved to **In Progress** and a subtask still blocked—surfaced via the `blocked` label quick filter.

After one 8-point story is completed, **Sprint insights** shows roughly 4% of sprint story points done. The ideal burndown line slopes down steadily toward the sprint end date; a flat line suggests work is not finishing on pace.

To list blocked sprint items:

```sql
project = ABC AND sprint in openSprints() AND labels = blocked
```

## Tips and pitfalls

- **Clear filters between speakers.** Leaving an assignee filter active hides everyone else's cards.
- **Surface unassigned and blocked work.** Items with no owner or a `blocked` label need explicit attention—not only each person's assigned list.
- **Keep standups short.** The timer enforces timeboxing; deep problem-solving belongs after the standup with the relevant people.
- **Burndown needs story points.** Without estimates, the burndown chart in Sprint insights has little to measure against.

> [!TIP]
> Combine **Group by assignee** swimlanes with the **Start standup** timer so the board walks through each lane in order without manual filter switching.

## Review questions

<details>
<summary>What is the main purpose of a daily standup?</summary>
Keep every team member aligned on recent progress, current work, and blockers so problems are addressed quickly—not to report status upward.
</details>

<details>
<summary>How do you show only one person's work items during standup?</summary>
Click their avatar on the board filter bar. Deselect it before choosing the next person.
</details>

<details>
<summary>What does the Start standup feature add beyond manual filtering?</summary>
A timed panel that rotates through participants, alerts when time is up, and helps keep the meeting within its time box.
</details>

<details>
<summary>What metric drives the burndown line in Sprint insights?</summary>
Story points. Completing estimated work lowers the remaining-work line over the sprint timeline.
</details>

<details>
<summary>Why might you group the board by epic during standup?</summary>
To walk through progress epic by epic when stakeholders care about feature-area status, or when different epics have different owners.
</details>

## Related

- [Glossary](../reference/glossary.md)
- [Scrum vs Kanban](../reference/scrum-vs-kanban.md)
- [Scrum Workflow in Jira: Sprints, Planning, and Execution](01-scrum-workflow-sprints.md)
- [Estimating with Story Points and Time in Agile Projects](02-estimating-story-points-and-time.md)
- [Using Basic Search and Quick Filters in Jira](../05-filters-and-jql/01-basic-search-and-quick-filters.md)

---

Previous: [Estimating with Story Points and Time in Agile Projects](02-estimating-story-points-and-time.md) · Next: [Working with Kanban: Managing Flow Over Time in Jira](04-kanban-managing-flow.md)
