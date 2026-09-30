---
title: "Using Issue Labels and Priorities to Organize Work in Jira"
aliases:
  - "Using Issue Labels and Priorities to Organize Work in Jira"
type: lesson
section: 4
lesson: 1
duration: "7:10"
status: done
tags:
  - jira
  - section/04
  - topic/labels
  - topic/priorities
---

# Using Issue Labels and Priorities to Organize Work in Jira

[Course home](../README.md) › [Section 4: Organizing Your Work](README.md) › Lesson 1 · 7:10

## TL;DR

**Labels** are free-form tags anyone can add to a work item (formerly *issue*). They cut across epics, spaces, and work types, so they suit cross-cutting themes such as a wishlist or OKR tracking. **Priority** is a separate field with preset levels (Highest through Lowest). It does not change backlog order — drag-and-drop ranking does. Both labels and priority can drive **quick filters** on the board once you know the matching JQL.

## Key concepts

- **Label**: A user-created tag on a work item. Labels are created the first time someone types a new name and confirms it. The same label name is reused across the whole site.
- **Recent labels**: When you open the Labels field, Jira suggests labels you or others have used recently in that space.
- **Label filter**: Clicking a label on a work item opens a search for every work item with that label. The resulting JQL can be copied for saved filters or quick filters.
- **Priority**: A standard field (for example Highest, High, Medium, Low, Lowest). New work items usually default to Medium. Changing priority does not reorder the backlog.
- **Backlog rank**: The order of work items in the backlog, set by drag-and-drop. This is the primary way to prioritize what the team works on next.
- **Quick filter**: A one-click filter on the board, defined with JQL, that temporarily narrows the cards shown.

## Labels vs epics

| | Epic | Label |
|---|---|---|
| Scope | One parent epic per story, task, or bug | Many labels per work item |
| Best for | Large product themes with a clear owner | Lightweight tagging, OKRs, wishlists, cross-epic grouping |
| Who defines it | Created as a work item in the space | Anyone with edit access can invent a new label |

A work item can belong to only one epic at a time. If something should appear under two initiatives, labels are a common workaround.

## How to do it in Jira

### Add or create a label

1. Open a work item and find the **Labels** field (add it from **Configure fields** if it is hidden).
2. Click in **Labels** and start typing the label name (for example `wishlist`).
3. Select an existing label from the list, or press Enter to create a new one.
4. Repeat on other work items. Recent labels appear as suggestions.

### Filter by label from a work item

1. Open a work item that has the label.
2. Click the label text. Jira runs a search for all matching work items.
3. Copy the JQL from the search bar if you want to reuse it elsewhere.

### Add a label quick filter to the board

1. Open the space **Backlog** or **Board**.
2. Open **Quick filters** (or the board menu) and choose **Manage quick filters**.
3. Select **Create quick filter**, name it (for example `Wishlist`), and paste or type the JQL (for example `labels = wishlist`).
4. Save and return to the board. Enable **Show quick filters** and click the new filter to narrow the view.

### Show labels on backlog cards

1. From the board, open the board menu (**⋯**) and choose **Board settings**.
2. Go to **Layout** (or **Card layout**).
3. Under **Backlog** (and optionally **Active sprints**), choose **Add field** and select **Labels**.
4. Save and return to the board. Cards now show their labels; work items with none show an empty labels area.

### Set priority and filter by it

1. Open a work item and change **Priority** in the detail view (for example from Medium to High).
2. To filter the board, create another quick filter with JQL such as `priority = Highest`.

## Examples

On the *Stamps and Points* backlog, the team has no **Wishlist** status in the workflow. They add a `wishlist` label to stories that are ideas for later, such as *Social login* and *Gift cards*. Clicking the label shows both items; the same query becomes a **Wishlist** quick filter on the Scrum board.

For quarterly OKRs, a label like `okr-q3-retention` can tag every story tied to a retention objective, even when those stories sit under different epics.

JQL copied from a label click might look like:

```sql
labels = wishlist AND project = ABC ORDER BY Rank ASC
```

A priority quick filter for urgent bugs:

```sql
priority = Highest AND project = ABC
```

## Tips and pitfalls

- **Agree on label names with the team** before widespread use. Labels are easy to create and hard to clean up; typos (`whishlist` vs `wishlist`) often persist.
- **Do not rely on Priority for backlog order.** Reordering the backlog changes rank, not the priority field. Use priority as a secondary signal (for example flagging blockers), not as the main planning sort.
- **Card layout trade-off.** Showing labels on every card helps scanning, but empty label fields on most cards add visual noise if the team rarely uses labels.
- **Combine with epics, not instead of them.** Epics structure product themes; labels add flexible cross-cutting tags.

> [!TIP]
> If the team needs a "later" bucket without a workflow status, a shared label such as `wishlist` or `parking-lot` is a lightweight pattern the lesson demonstrates on the board.

## Review questions

<details>
<summary>How is a new label created in Jira?</summary>
Open the Labels field on a work item, type a name that does not exist yet, and confirm (Enter). The label is created and attached to that work item.
</details>

<details>
<summary>Why might a team use labels when epics already organize the backlog?</summary>
A work item can link to only one epic. Labels let the same item appear in multiple groupings, such as an OKR tag plus an epic, or a wishlist tag for work that is not ready for a sprint.
</details>

<details>
<summary>Does changing Priority move a work item up or down in the backlog?</summary>
No. Backlog order comes from rank (drag-and-drop). Priority is a separate field and does not reorder the list.
</details>

<details>
<summary>What happens when you click a label on a work item?</summary>
Jira opens a filter showing all work items with that label and displays the JQL query, which you can copy for quick filters or saved filters.
</details>

<details>
<summary>Where do you add Labels so they appear on backlog cards?</summary>
Board settings, then Layout or Card layout, then Add field under Backlog (and optionally Active sprints).
</details>

## Related

- [Glossary](../reference/glossary.md)
- [Create Work Items: Epics, Stories & Subtasks](../02-jira-fundamentals/03-create-epics-stories-subtasks.md)
- [Using Basic Search and Quick Filters in Jira](../05-filters-and-jql/01-basic-search-and-quick-filters.md)
- [Structuring Work with Components in Jira Projects](02-components.md)

---

Previous: [Section overview](README.md) · Next: [Structuring Work with Components in Jira Projects](02-components.md)
