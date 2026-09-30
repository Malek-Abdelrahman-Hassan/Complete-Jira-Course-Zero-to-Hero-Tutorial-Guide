---
title: "Kanban Reports: Control Chart and Cumulative Flow Diagram"
aliases:
  - "Kanban Reports: Control Chart and Cumulative Flow Diagram"
type: lesson
section: 8
lesson: 5
duration: "6:45"
status: done
tags:
  - jira
  - section/08
  - topic/reports
  - topic/kanban
---

# Kanban Reports: Control Chart and Cumulative Flow Diagram

[Course home](../README.md) › [Section 8: Dashboards and Reports](README.md) › Lesson 5 · 6:45

## TL;DR

Kanban boards expose the same **Reports** menu as Scrum boards, but **control chart** and **cumulative flow diagram (CFD)** matter most for flow-based work. The control chart plots **cycle time**—how long completed work items took from start to finish—with an average line and a band showing variation. Lower averages and tighter bands mean faster, more predictable delivery. The CFD (introduced earlier in the course) shows where work piles up by status over time. Use both together: CFD for bottlenecks, control chart for timing predictability.

## Key concepts

- **Control chart**: A scatter-style report of **cycle time** for completed work items. Each dot is one item (or a cluster of items closed on the same day). A line shows the rolling average; a shaded band shows spread around that average.
- **Cycle time**: Elapsed time from when work starts (for example entering **In progress**) until it is **Done**. Shorter cycle time means faster value delivery and quicker feedback.
- **Variation (spread)**: How much individual cycle times differ from the average. A tight band means predictable delivery; a wide band means some items finish in days and others in weeks.
- **Board columns vs statuses**: Control chart filters use **board columns** (the Kanban board configuration), not every workflow status in the space.
- **Cumulative flow diagram (CFD)**: Stacked bands by status over time. Widening bands signal bottlenecks; parallel bands signal steady flow. Covered in depth in [Section 3](../03-agile-scrum-and-kanban/06-cumulative-flow-diagram.md); still available on Kanban **Reports**.
- **Outliers**: Dots far above the average often come from old backlog items closed in bulk, long-idle work, or one-off exceptions—not necessarily today's process.

## How to read the control chart

| Element | Meaning | What you want |
|---|---|---|
| **Dots** | Cycle time of completed work items (clusters = several closed same day) | Mostly low, near the average line |
| **Average line** | Rolling mean cycle time for the selected period | Trend flat or downward over time |
| **Shaded band** | Range of cycle times around the average | Narrow—predictable delivery |
| **Spikes upward** | Periods when completions took much longer | Investigate linked work items before changing process |

## How to do it in Jira

1. Open the **Kanban board** and select **Reports**.
2. Open **Control chart**. Read the on-screen tips Jira provides for your site version.
3. Set the **timeframe** at the bottom (for example past week or past month). Short windows react quickly; longer windows smooth noise.
4. Filter by **columns** (board columns included in the calculation), **swimlanes**, and **quick filters**. Include everything for a team-wide view; exclude lanes only when certain work types should not affect delivery metrics.
5. Hover over dots or clusters to see which work items completed and their cycle times. Open suspicious items to learn whether outliers are real process problems or cleanup.
6. Open **Cumulative flow diagram** on the same page when you also need to see where work accumulates by status.
7. Revisit after the board has enough completed history—empty or sparse charts on new boards are normal.

## Examples

On a mature Kanban board, the control chart shows an average cycle time around seven to eight days with a band that widens sharply mid-chart—average jumps toward sixteen days. Hovering the cluster reveals a batch of ancient backlog items closed without development, which explains the spike without implying the whole team slowed down.

For *Stamps and Points* support-style flow, a CFD with a widening **In progress** band plus a rising control-chart average suggests work is entering development faster than it leaves—pair with WIP limits and stand-up conversation before blaming individuals.

## Tips and pitfalls

- **Investigate dots, do not panic at spikes.** Bulk closes and reopened-then-finished items distort averages; read the underlying work items.
- **Exclude deliberate exceptions.** Use swimlanes or quick filters to omit work types that should not define team delivery time (for example "won't fix" closures).
- **Pair CFD and control chart.** CFD shows where work stalls; control chart shows how long finished work took end to end.
- **Same reports on Scrum boards.** Kanban-focused lessons apply to Scrum boards too—the **Reports** catalog overlaps.
- **Needs completed work.** Until items flow to Done, the control chart has little to plot.

> [!TIP]
> Shorter cycle time and tighter variation support Kanban goals: finish work in progress before starting more, and make delivery dates believable.

## Review questions

<details>
<summary>What does cycle time measure on a control chart?</summary>
How long a completed work item took from starting active work (for example In progress) through Done—not time spent sitting in the backlog before work began.
</details>

<details>
<summary>What does a wide shaded band around the average line indicate?</summary>
High variation: some items finish quickly and others take much longer, so delivery is less predictable.
</details>

<details>
<summary>Why filter control chart columns by board column rather than workflow status alone?</summary>
The report respects the Kanban board column mapping you configured; columns determine which stages count toward cycle time for that board view.
</details>

<details>
<summary>When should you exclude swimlanes or quick filters from the control chart?</summary>
When certain work types (old backlog cleanup, spikes, non-team work) would skew cycle time and are not representative of normal delivery.
</details>

<details>
<summary>How does the cumulative flow diagram complement the control chart?</summary>
The CFD shows where work accumulates by status over time (bottlenecks). The control chart shows how long completed items took and how predictable that timing is.
</details>

## Related

- [Glossary](../reference/glossary.md)
- [Reports and Metrics](../reference/reports-and-metrics.md)
- [Scrum vs Kanban](../reference/scrum-vs-kanban.md)
- [Understanding the Cumulative Flow Diagram for Kanban Teams](../03-agile-scrum-and-kanban/06-cumulative-flow-diagram.md)
- [Working with Kanban: Managing Flow Over Time in Jira](../03-agile-scrum-and-kanban/04-kanban-managing-flow.md)
- [Scrum Reports: Velocity, Burndown, and Sprint Report Explained](04-scrum-reports.md)

---

Previous: [Scrum Reports: Velocity, Burndown, and Sprint Report Explained](04-scrum-reports.md) · Next: [Section 8 Quiz](06-section-8-quiz.md)
