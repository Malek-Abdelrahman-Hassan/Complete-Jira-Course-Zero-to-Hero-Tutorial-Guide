---
title: "Useful Gadgets for Your Jira Dashboard: Filters, Charts, and More"
aliases:
  - "Useful Gadgets for Your Jira Dashboard: Filters, Charts, and More"
type: lesson
section: 8
lesson: 2
duration: "6:31"
status: done
tags:
  - jira
  - section/08
  - topic/dashboards
---

# Useful Gadgets for Your Jira Dashboard: Filters, Charts, and More

[Course home](../README.md) › [Section 8: Dashboards and Reports](README.md) › Lesson 2 · 6:31

## TL;DR

The most practical dashboard gadgets share one pattern: attach a **saved filter**, choose how to slice the data, and let Jira keep the view current. **Filter Results** lists work items; **Work item Statistics** and **Pie Chart** break counts down by fields such as status or assignee; **Created vs. Resolved Chart** shows whether backlog pressure is rising or falling; **Two Dimensional Filter Statistics** crosses two fields in a table. Numbers on these gadgets link to the underlying JQL—click through to see exactly which work items (formerly *issues*) make up each total.

## Key concepts

- **Filter Results**: A table of work items returned by a saved filter. You choose which columns appear—trim fields you do not need so the gadget fits the layout.
- **Work item Statistics** (formerly *Issue Statistics*, the name used in the video): A bar-style breakdown of filter results by one field (status, assignee, priority, and others). Useful for quick percentage views.
- **Pie Chart**: The same data as Work item Statistics in pie form. Pick one representation; you rarely need both for the same filter and field.
- **Created vs. Resolved Chart**: A time-series chart of work items created versus resolved over a chosen period. Resolved work typically appears in green.
- **Two Dimensional Filter Statistics**: A table crossing two fields—for example assignee on one axis and status on the other—so you can spot workload imbalance.
- **Drill-down links**: Counts and segments on filter-based gadgets are clickable. Each link opens a search showing the work items behind that number, which is also a practical way to learn JQL.

## Gadget comparison

| Gadget | Best for | Key settings |
|---|---|---|
| **Filter Results** | A live work list | Saved filter, visible columns, result count |
| **Work item Statistics** | Percentages by one field | Filter, statistic type, sort direction, include resolved |
| **Pie Chart** | Visual share by one field | Filter, statistic type (status, assignee, etc.) |
| **Created vs. Resolved Chart** | Backlog growth vs shrinkage | Filter, period length, daily/weekly grouping |
| **Two Dimensional Filter Statistics** | Workload by person and stage | Filter, row field, column field |

## How to do it in Jira

1. Create or open a dashboard and add gadgets with **Add gadget**.
2. For **Filter Results**, select **Configure**, pick a saved filter (for example one scoped to a release or board), set **Number of results**, and choose columns. Remove low-value columns such as **Priority** if space is tight; add **Epic** or epic link when tracking epic progress.
3. For **Work item Statistics**, attach the same filter, choose a **Statistic Type** (often **Status** or **Assignee**), set sort to ascending, and decide whether to **Show resolved** items.
4. For **Pie Chart**, reuse the filter and pick a statistic type. Status and assignee are common choices when you want a different visual from Work item Statistics.
5. For **Created vs. Resolved Chart**, select the filter, set the interval (for example daily over the last five days), and save.
6. For **Two Dimensional Filter Statistics**, pick the filter, then set the two dimensions—for example **Assignee** by **Status**.
7. Adjust the dashboard **layout** if tables need width: a single wide column or a two-column layout with a large left pane often suits **Filter Results**.
8. Skip **Refresh every 15 minutes** unless you need a wall display. Dashboards refresh when loaded; per-gadget auto-refresh can slow heavy pages.

## Examples

The *Stamps and Points* release lead tracks version 3.2 across two spaces with one saved filter. Their dashboard places **Filter Results** on the left (columns: **Key**, **Summary**, **Status**, **Epic**), **Work item Statistics** by **Status** in the center, and **Pie Chart** by **Assignee** on the right. The pie chart reveals most work items are still unassigned—a signal to assign owners before the release date.

Clicking **3** under **In Progress** in **Two Dimensional Filter Statistics** opens a JQL search equivalent to the release filter plus an In Progress constraint—useful for verifying the count without rebuilding the query by hand.

## Tips and pitfalls

- **One filter, many gadgets.** Reusing the same saved filter keeps every chart aligned to the same scope (release, team, or space).
- **Do not duplicate chart types.** Work item Statistics and Pie Chart for the same field tell the same story; pick the format stakeholders prefer.
- **Watch column real estate.** Extra columns in **Filter Results** wrap or truncate on narrow layouts—show only fields decisions depend on.
- **Self-explanatory gadgets exist.** **Activity Stream** and **Assigned To Me** need little setup but are secondary to filter-driven reporting gadgets.

> [!NOTE]
> Gadget names follow the new terminology: *Issue Statistics* is now **Work item Statistics**, *Projects* is **Spaces**, and *Recently Created Issues* is **Recently Created Work items**. The Heat Map gadget is no longer in Atlassian's list, and older gadgets such as Road Map, Bubble Chart, and Labels may follow, so build dashboards around the filter-based charts above.

## Review questions

<details>
<summary>What do Filter Results and Pie Chart have in common?</summary>
Both need a saved filter as their data source. Filter Results lists work items; Pie Chart aggregates the same filter by a chosen field such as status or assignee.
</details>

<details>
<summary>When is Two Dimensional Filter Statistics more useful than Work item Statistics?</summary>
When you need to see two dimensions at once—for example how many items each assignee has in each status—not just a single-field breakdown.
</details>

<details>
<summary>What does a Created vs. Resolved Chart with mostly red and little green suggest?</summary>
More work items are being created than resolved in the selected period—the backlog is likely growing.
</details>

<details>
<summary>Why are the numbers on Work item Statistics clickable?</summary>
Each number links to a JQL search showing the work items counted in that segment, so you can verify or investigate the data.
</details>

<details>
<summary>Should you enable refresh every 15 minutes on every gadget?</summary>
Not by default. Dashboards update when you open them; forcing frequent refresh on many gadgets can slow the page without much benefit for day-to-day use.
</details>

## Related

- [Glossary](../reference/glossary.md)
- [Reports and Metrics](../reference/reports-and-metrics.md)
- [Creating Personal and Team Dashboards in Jira](01-personal-and-team-dashboards.md)
- [Creating and Saving Filters in Jira for Quick Access](../05-filters-and-jql/02-creating-and-saving-filters.md)
- [Sharing and Cloning Dashboards with Stakeholders and Teams](03-sharing-and-cloning-dashboards.md)

---

Previous: [Creating Personal and Team Dashboards in Jira](01-personal-and-team-dashboards.md) · Next: [Sharing and Cloning Dashboards with Stakeholders and Teams](03-sharing-and-cloning-dashboards.md)
