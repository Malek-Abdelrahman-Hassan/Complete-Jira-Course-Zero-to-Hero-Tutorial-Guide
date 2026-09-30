---
title: "Estimating with Story Points and Time in Agile Projects"
aliases:
  - "Estimating with Story Points and Time in Agile Projects"
type: lesson
section: 3
lesson: 2
duration: "10:04"
status: done
tags:
  - jira
  - section/03
  - topic/estimation
---

# Estimating with Story Points and Time in Agile Projects

[Course home](../README.md) › [Section 3: Agile in Jira: Scrum and Kanban](README.md) › Lesson 2 · 10:04

## TL;DR

Story points estimate **relative size**—combining effort, complexity, and uncertainty—using a Fibonacci-style scale (1, 2, 3, 5, 8, 13, and sometimes 20). Jira totals story points on the sprint and backlog, tracks completed versus remaining work during an active sprint, and shows epic-level progress bars. Time-based **Original estimate** and **Time tracking** are also available, but the course favors story points for Agile planning.

## Key concepts

- **Story points**: A relative sizing tool for work items. Teams compare each item to a baseline story rather than guessing exact hours.
- **Fibonacci scale**: The common Agile sequence 1, 2, 3, 5, 8, 13, 20 (sometimes 40 and 100). Larger numbers reflect growing uncertainty—big items are harder to estimate precisely.
- **Baseline story**: A typical piece of work the team agrees is "medium"—for example, 5 points. Other items are sized as smaller or larger compared to that anchor.
- **Velocity**: The average story points a team completes per sprint. After several sprints, velocity helps plan how much work to commit to next time.
- **Sprint point totals**: On the backlog, gray shows remaining points, blue shows in-progress points, and green shows completed points for the active sprint.
- **Original estimate**: A time-based field where you enter expected duration using suffixes such as `h` (hours), `d` (days), or `w` (weeks).
- **Time tracking**: Logs time spent on a work item and calculates remaining time against the original estimate.

## How to do it in Jira

### Story points

1. Open a work item (for example, *Add a new user to the database*).
2. Scroll to **More fields** and locate **Story points**. Use **Pin field** so it stays visible at the top of the detail view.
3. Enter a value from the team's scale (1, 2, 3, 5, 8, 13, 20). Do not use numbers between scale steps (no 4, 9, or 10).
4. Repeat for other backlog items. Small gray boxes on backlog cards show each item's points.
5. Drag estimated items into a sprint. The sprint header shows the **total story points** committed (for example, 64).
6. After starting the sprint, return to the backlog view to see gray (to do), blue (in progress), and green (completed) point totals update as work moves.
7. Open the **Epics** panel to see progress bars per epic—green for done, blue for in progress, gray for not started—with percentage complete for estimated work.

### Time-based estimation (optional)

1. On a work item, open **More fields** and find **Original estimate**.
2. Enter a duration with a unit suffix, such as `75h` or `15d`. Jira converts to a readable format (for example, 75 hours becomes 1 week, 4 days, 3 hours based on configured working days).
3. Use **Time tracking** on the work item to log time spent (for example, `4d`). Jira shows logged time and remaining estimate on the work item.

> [!NOTE]
> Working days per week for time conversion are configured at site level—ask a Jira admin if the defaults do not match your team calendar.

## Examples

The team sets *Add a new user to the database* as the baseline at **5 points**. A much larger story gets **13**, a slightly larger one **8**, a smaller one **3**, and a very large item **20**. After estimating sprint candidates, the sprint total is **64 points**.

Once the sprint starts and one 8-point story is done while a 5-point story is in progress, the backlog shows **51** gray, **5** blue, and **8** green.

In the **User account** epic panel, one of eight stories is complete. Among estimated items, **61%** of estimated points are done and five stories still lack estimates.

Time-based example: entering `75h` on a work item displays as one week, four days, and three hours. Logging `4d` of work leaves a remaining estimate shown on the time tracking panel.

```sql
project = ABC AND "Story Points" is not EMPTY AND sprint in openSprints()
```

## Tips and pitfalls

- **Estimate relatively, not precisely.** Story points express size compared to other items; there is no exact science to choosing 8 over 5.
- **Keep the same baseline over time** so velocity trends become meaningful across sprints.
- **Unestimated work hides true scope.** Epic progress bars only reflect estimated items—estimate backlog candidates before relying on percentages.
- **Prefer story points for Agile teams.** Time tracking adds overhead and can encourage micromanagement; use it only when your context truly needs hour-level tracking.

> [!WARNING]
> Mixing re-estimation styles or changing the baseline every sprint makes velocity unreliable for planning.

## Review questions

<details>
<summary>Why do Agile teams use Fibonacci numbers instead of continuous values like 4 or 10?</summary>
Larger work items carry more uncertainty. The widening gaps in the scale reflect that precise sizing breaks down as items get bigger.
</details>

<details>
<summary>What do the gray, blue, and green story point totals on the backlog mean during an active sprint?</summary>
Gray is remaining (to do), blue is in progress, and green is completed. They sum to the sprint's committed scope.
</details>

<details>
<summary>How do you enter 75 hours in the Original estimate field?</summary>
Type 75h and press Enter. Jira converts it to weeks, days, and hours based on configured working days.
</details>

<details>
<summary>What is velocity used for once the team has several sprints of data?</summary>
Planning the next sprint's capacity—committing roughly the same number of story points the team reliably completes each iteration.
</details>

<details>
<summary>What does a green segment on an epic progress bar indicate?</summary>
Work items in that epic that have been completed.
</details>

## Related

- [Glossary](../reference/glossary.md)
- [Scrum vs Kanban](../reference/scrum-vs-kanban.md)
- [Scrum Workflow in Jira: Sprints, Planning, and Execution](01-scrum-workflow-sprints.md)
- [Running Daily Standups with Jira: Best Practices](03-daily-standups.md)
- [Scrum Reports: Velocity, Burndown, and Sprint Report Explained](../08-dashboards-and-reports/04-scrum-reports.md)

---

Previous: [Scrum Workflow in Jira: Sprints, Planning, and Execution](01-scrum-workflow-sprints.md) · Next: [Running Daily Standups with Jira: Best Practices](03-daily-standups.md)
