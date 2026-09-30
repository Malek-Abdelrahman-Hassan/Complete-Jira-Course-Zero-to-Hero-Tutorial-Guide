---
title: "Understanding the Cumulative Flow Diagram for Kanban Teams"
aliases:
  - "Understanding the Cumulative Flow Diagram for Kanban Teams"
type: lesson
section: 3
lesson: 6
duration: "4:46"
status: done
tags:
  - jira
  - section/03
  - topic/kanban
  - topic/reports
---

# Understanding the Cumulative Flow Diagram for Kanban Teams

[Course home](../README.md) › [Section 3: Agile in Jira: Scrum and Kanban](README.md) › Lesson 6 · 4:46

## TL;DR

The **cumulative flow diagram (CFD)** is a Kanban board report that stacks colored bands showing how many work items sat in each status over time. Ideally, bands rise together while keeping roughly the same width—steady flow. A band that keeps widening signals a bottleneck or stalled work. Each board has its own CFD, shaped by that board's columns and mapped statuses.

## Key concepts

- **Cumulative flow diagram (CFD)**: A stacked area chart where each band represents a board column/status. The vertical height at any date shows how many work items were in that status on that day.
- **Board-specific report**: The CFD reflects one Kanban board's column configuration. Two boards in the same space can show different diagrams.
- **Steady band width**: When throughput matches arrival rate, each status band stays about the same thickness over time—all bands climb in parallel.
- **Widening band**: A band that grows thicker over a period means work items are accumulating in that status—often a bottleneck, capacity gap, or period of inactivity.
- **Control chart**: Another useful Kanban report (covered later in the course) that analyzes cycle time for completed items.

## How to do it in Jira

1. Open the **Kanban board** and click **Reports** in the board menu.
2. Select **Cumulative flow diagram**. Other reports on the same page may be Scrum-specific or Kanban-specific depending on board type.
3. Set the **date range** to the period you want to analyze.
4. Refine the view with filters for **columns**, **swimlanes**, and **quick filters**. Include all columns and swimlanes for a full picture.
5. Read the chart:
   - Each color corresponds to a column/status (for example, backlog, selected for development, in progress, done).
   - The total height at any point is all work items on the board at that moment.
   - Bands should rise over time as new work enters the system, but each band's **thickness** shows how many items are stuck in that stage.
6. Investigate any band that widens for an extended period—check for blockers, missing capacity, or statuses that are not being updated.

## Examples

On a fresh *Stamps and Points* board with little history, most items sit in **To Do** (one large band) with tiny slivers for **In Progress**, **Testing**, and **Done**—reflecting demo activity rather than steady production flow.

In a mature example with columns **Backlog**, **Selected for development**, **In progress**, and **Done**, the **In progress** band widens sharply over two weeks while no items reach **Done** and no new items are created. That flat plateau suggests work stalled—possibly a bottleneck, holiday, or team blocked on dependencies.

After adding a **Testing** status, the CFD gains a new band. Most items remain in **To Do** with a few in **Testing**, showing where work accumulates.

## Tips and pitfalls

- **Need history for meaningful charts.** A brand-new board produces a sparse or confusing CFD until enough status transitions accumulate.
- **Widening does not always mean failure.** Confirm context—a widening **In progress** band during a known freeze explains the pattern. Sustained widening without explanation deserves investigation.
- **Filter deliberately.** Excluding columns or swimlanes hides part of the flow and can mask bottlenecks.
- **Pair CFD with WIP limits.** Limits surface overload on the board; the CFD shows whether overload is a one-day spike or a weeks-long trend.

> [!TIP]
> Check the CFD regularly during Kanban operation—not only when something feels wrong—so widening bands are caught early.

## Review questions

<details>
<summary>What does each colored band on a cumulative flow diagram represent?</summary>
The count of work items in one board column (mapped status) at a given point in time. Bands stack to show total work in the system.
</details>

<details>
<summary>What does an ideally healthy CFD look like over time?</summary>
All bands trend upward as work enters the system, but each band stays roughly the same width—work flows through without accumulating in one status.
</details>

<details>
<summary>What does a band that keeps getting wider indicate?</summary>
Work items are piling up in that status—a likely bottleneck, insufficient capacity, or lack of status updates moving items forward.
</details>

<details>
<summary>Is the CFD shared across all boards in a space?</summary>
No. Each Kanban board has its own CFD based on that board's columns and configuration.
</details>

<details>
<summary>Which other Kanban report does the course mention as highly useful?</summary>
The control chart, covered in a later section—it analyzes how long completed items take to flow through the board.
</details>

## Related

- [Glossary](../reference/glossary.md)
- [Scrum vs Kanban](../reference/scrum-vs-kanban.md)
- [Reports and Metrics](../reference/reports-and-metrics.md)
- [Visualizing Work with WIP Limits and Swimlanes in Jira](05-wip-limits-and-swimlanes.md)
- [Kanban Reports: Control Chart and Cumulative Flow Diagram](../08-dashboards-and-reports/05-kanban-reports.md)

---

Previous: [Visualizing Work with WIP Limits and Swimlanes in Jira](05-wip-limits-and-swimlanes.md) · Next: [Section 3 Quiz](07-section-3-quiz.md)
