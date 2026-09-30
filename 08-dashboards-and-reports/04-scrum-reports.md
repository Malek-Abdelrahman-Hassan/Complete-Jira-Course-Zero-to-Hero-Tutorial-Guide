---
title: "Scrum Reports: Velocity, Burndown, and Sprint Report Explained"
aliases:
  - "Scrum Reports: Velocity, Burndown, and Sprint Report Explained"
type: lesson
section: 8
lesson: 4
duration: "10:36"
status: done
tags:
  - jira
  - section/08
  - topic/reports
  - topic/scrum
---

# Scrum Reports: Velocity, Burndown, and Sprint Report Explained

[Course home](../README.md) › [Section 8: Dashboards and Reports](README.md) › Lesson 4 · 10:36

## TL;DR

**Board reports** differ from dashboards: Jira generates them automatically from a board's sprint history—you do not build them gadget by gadget. On a Scrum board, open **Reports** for burndown, sprint report, and velocity views. The **burndown chart** tracks remaining work against an ideal line during a sprint. The **sprint report** summarizes what finished, what did not, and what was added mid-sprint—ideal for sprint review. The **velocity chart** compares committed versus completed work across sprints to spot over- or under-planning.

## Key concepts

- **Board report**: An auto-generated chart or table tied to one board's data. Unlike a dashboard, you do not pick gadgets—Jira calculates the report from sprint and work-item history.
- **Burndown chart**: Plots remaining work in the selected sprint against time. A gray **guideline** slopes from full scope to zero; a colored line shows actual remaining work (story points, work-item count, or original time estimate).
- **Burnup chart**: Tracks total scope and completed work on separate lines. Less commonly used in the course demos but available on the same **Reports** page.
- **Sprint report**: Produced when a sprint completes (or in progress with partial data). Lists completed and incomplete work items, embeds a burndown, and flags items added after sprint start.
- **Velocity**: Story points (or count) completed per sprint. The **velocity chart** shows **committed** (planned) versus **completed** columns side by side for each sprint.
- **Scope creep**: Work items added to a sprint after planning. The sprint report marks them so the team can discuss planning discipline at review.
- **Epic report**: Shows total versus completed story points and issue counts for one epic, plus an **unestimated issues** line. Useful when epics span many sprints.

## How to read Scrum reports

| Report | What to look at | Healthy pattern | Warning pattern |
|---|---|---|---|
| **Burndown** | Remaining work line vs gray guideline | Line trends down toward zero near sprint end | Line stays flat (no progress) or sits above the guideline (time passes, little completion) |
| **Sprint report** | Completed vs not completed; mid-sprint additions | Most committed work finished; few or no late additions | Large incomplete slice; many items added after start (marked with an asterisk) |
| **Velocity chart** | Gray committed bar vs green completed bar | Similar height sprint after sprint | Green consistently lower (overcommitting) or higher (under-planning) |
| **Epic report** | Blue completed area filling gray total scope | Steady progress; unestimated line near zero | Scope grows without estimates; completed area flat |

## How to do it in Jira

1. Open the **Scrum board** for your space and select **Reports** in the board menu.
2. For **Burndown chart**, pick the **Sprint** and metric (**Story points**, **Issue count**, or **Original time estimate**). Read the guideline and remaining-work line; click data points to see which work items moved.
3. Open **Sprint report**, choose a **completed sprint** for a full picture (active sprints show partial data). Review completed work, not completed work, and any items added after sprint start.
4. Open **Velocity chart** and compare gray (committed) and green (completed) bars across recent sprints. Select a sprint bar to jump to that sprint's report.
5. Optionally explore **Epic report**—choose an epic and review scope versus completion, unestimated work, and the issue list below the chart.
6. Treat **Burnup chart**, **Epic burndown**, and **Release burndown** as secondary reports; read their titles and axes if your process needs them.

## Examples

On the *Stamps and Points* ABC board, Sprint 3 planned 64 story points but completed only 3. The burndown shows a tiny drop—the team opened and closed the sprint quickly with almost no delivery. The sprint report makes the gap obvious: one completed story and a large not-completed list.

Sprint 4's burndown looks noisy because a work item was completed, reopened, and completed again. That pattern inflates and resets remaining work—worth investigating in real teams, not a sign of healthy flow.

In a mature epic report, gray area shows total scope, blue area shows completed points climbing steadily, and the brown **unestimated issues** line stays near zero—evidence the epic is estimated and progressing.

## Tips and pitfalls

- **Use sprint report at review.** It is the report the course highlights for sprint review conversations about completion and scope change.
- **Velocity needs history.** One or two sprints produce thin charts; patterns emerge after several closed sprints.
- **Burndown above the guideline means trouble.** When remaining work stays high while time runs out, the team is not finishing planned scope.
- **Reopened work items distort burndown.** Completion followed by reopen jumps the remaining-work line back up.
- **Demo data looks odd.** Practice sites with little real activity produce flat or tiny charts—focus on how to read the axes and labels.

> [!TIP]
> Click any point or segment on burndown and velocity charts to drill into the work items behind the numbers—the same investigative habit as clicking dashboard gadget counts.

## Review questions

<details>
<summary>How do board reports differ from dashboards?</summary>
Board reports are auto-generated from a board's sprint and work history. Dashboards are custom pages of gadgets you configure with saved filters.
</details>

<details>
<summary>What does it mean when the burndown remaining-work line stays above the gray guideline?</summary>
Time is passing but remaining work is not dropping fast enough—the sprint is likely off track for finishing committed scope.
</details>

<details>
<summary>Which report should you open at sprint review, and why?</summary>
The sprint report. It lists completed and incomplete work and highlights items added after sprint start, which supports discussion of planning and scope change.
</details>

<details>
<summary>On the velocity chart, what does a green bar consistently shorter than the gray bar indicate?</summary>
The team completes less than it commits, a sign of overcommitting during sprint planning.
</details>

<details>
<summary>What does an asterisk on an item in the sprint report usually mean?</summary>
The work item was added to the sprint after sprint planning had already started—potential scope creep to discuss in review.
</details>

## Related

- [Glossary](../reference/glossary.md)
- [Reports and Metrics](../reference/reports-and-metrics.md)
- [Scrum vs Kanban](../reference/scrum-vs-kanban.md)
- [Scrum Workflow in Jira: Sprints, Planning, and Execution](../03-agile-scrum-and-kanban/01-scrum-workflow-sprints.md)
- [Estimating with Story Points and Time in Agile Projects](../03-agile-scrum-and-kanban/02-estimating-story-points-and-time.md)
- [Kanban Reports: Control Chart and Cumulative Flow Diagram](05-kanban-reports.md)

---

Previous: [Sharing and Cloning Dashboards with Stakeholders and Teams](03-sharing-and-cloning-dashboards.md) · Next: [Kanban Reports: Control Chart and Cumulative Flow Diagram](05-kanban-reports.md)
