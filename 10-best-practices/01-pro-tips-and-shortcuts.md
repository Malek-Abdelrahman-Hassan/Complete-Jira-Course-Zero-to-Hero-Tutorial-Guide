---
title: "Pro Tips, Shortcuts, and Smart Habits for Jira Power Users"
aliases:
  - "Pro Tips, Shortcuts, and Smart Habits for Jira Power Users"
type: lesson
section: 10
lesson: 1
duration: "5:06"
status: done
tags:
  - jira
  - section/10
  - topic/shortcuts
  - topic/best-practices
---

# Pro Tips, Shortcuts, and Smart Habits for Jira Power Users

[Course home](../README.md) › [Section 10: Best Practices and Final Challenge](README.md) › Lesson 1 · 5:06

## TL;DR

Keyboard shortcuts cut down mouse travel for everyday actions such as creating work items, searching, and reordering the backlog. Bulk selection and the spreadsheet-style list view speed up multi-item edits. Power users also lean on quick filters, personal dashboards, and automation rules learned earlier in the course so daily work stays fast and predictable.

## Key concepts

- **Keyboard shortcut**: A key or key sequence that runs a Jira action without using the mouse. Shortcuts work on boards and work-item views, not inside the administration area.
- **Actions menu**: A compact menu of transitions and edits for the selected work item. Press `.` (period) to open it; some actions inside the menu have their own letter shortcuts.
- **Backlog reorder shortcuts**: `s` then `t` sends the selected backlog item to the top; `s` then `b` sends it to the bottom. Useful when the backlog is long and dragging cards is slow.
- **Bulk change**: Selecting multiple work items at once and applying the same update — move to sprint, reorder, or open the full bulk-edit dialog.
- **List view**: A tabular layout that shows work items like a spreadsheet, with configurable columns for fast inline editing.

## Shortcuts from this lesson

Press `?` in Jira anytime to see the full list for your site. Shortcuts do not fire while the cursor is in a text field.

| Keys | Action |
|---|---|
| `c` | Create a work item (pick the correct space and work type) |
| `/` | Focus the search box |
| `.` | Open the actions menu for the selected work item |
| `d` | Change status (from the actions menu) |
| `g` then `i` | Go to work item search (opens the filter / JQL view) |
| `s` then `t` | Send selected backlog item to the top |
| `s` then `b` | Send selected backlog item to the bottom |

Compared with [Keyboard shortcuts](../reference/keyboard-shortcuts.md), this lesson also demonstrates backlog reorder keys (`s` then `t`, `s` then `b`) and status change via `d` in the actions menu. The reference page lists additional global shortcuts such as `g` then `d` (dashboards) and `g` then `a` (boards) that are not shown in the video.

## How to do it in Jira

### Create and search with shortcuts

1. From a board or backlog (not **Settings**), press `c` to open **Create**.
2. Choose the correct space and work type, fill in the fields, and save.
3. Press `/` anywhere to jump to the top search box and type a query.

### Reorder the backlog quickly

1. Open the space **Backlog**.
2. Click a work item to select it.
3. Press `s` then `t` to move it to the top, or `s` then `b` to move it to the bottom.
4. Fine-tune order with drag-and-drop once the important items are grouped at the top.

### Use the actions menu on one work item

1. Select a work item on the board or in a list.
2. Press `.` to open the actions menu.
3. Press `d` (or choose **Status**) and pick the target status with the keyboard.

### Bulk-select and bulk-edit

1. On the backlog or board, **Shift**-click to select a range, or tick individual checkboxes.
2. Right-click the selection for quick moves — send to sprint, move to top or bottom of backlog, or open **Bulk change**.
3. In **Bulk change**, pick the fields to update and confirm.

### Edit many items in list view

1. Open the board and switch to **List** view (layout varies; look for a list or table toggle near the board header).
2. Use **Configure columns** to add fields you need or hide ones you do not.
3. Edit cells inline, similar to a spreadsheet, instead of opening each work item separately.

## Examples

On the *Stamps and Points* backlog, the product owner selects `ABC-29` and presses `s` then `t` so it jumps above dozens of older stories. After moving several priority items to the top the same way, they drag within that group to set sprint-ready order.

Before planning, they bulk-select five unestimated stories, right-click, and choose **Bulk change** to set **Story Points** in one step.

For a release sweep, they open **List** view, add **Fix version** and **Assignee** columns, and update ten work items without leaving the table.

## Tips and pitfalls

- **Group first, refine second.** Send everything that matters to the top with `s` then `t`, then drag to fine-tune. Trying to drag one card across a hundred-row backlog wastes time.
- **Confirm space and work type on `c`.** The create shortcut is fast; picking the wrong space creates cleanup work later.
- **Combine shortcuts with filters and dashboards.** Shortcuts move you quickly; saved quick filters and gadgets keep the right work visible once you arrive.

> [!TIP]
> Press `?` after Jira updates — Atlassian occasionally changes shortcut bindings, and your site may differ slightly from course recordings.

## Review questions

<details>
<summary>Which shortcut opens the create dialog from a board?</summary>
<code>c</code>, as long as you are not in the administration area.
</details>

<details>
<summary>What do the key sequences <code>s</code> then <code>t</code> and <code>s</code> then <code>b</code> do on the backlog?</summary>
The first sends the selected work item to the top of the backlog; the second sends it to the bottom.
</details>

<details>
<summary>How can you bulk-update story points on several work items at once?</summary>
Select them with checkboxes or Shift-click, then right-click and choose Bulk change, or use list view to edit the column inline.
</details>

<details>
<summary>What does <code>g</code> then <code>i</code> open?</summary>
The work item search view, where you can run basic or JQL searches across work items you can access.
</details>

## Related

- [Glossary](../reference/glossary.md)
- [Keyboard Shortcuts](../reference/keyboard-shortcuts.md)
- [Create Work Items: Epics, Stories & Subtasks](../02-jira-fundamentals/03-create-epics-stories-subtasks.md)
- [Customizing Your Jira Board View Without Admin Access](../06-boards-and-workflows/01-customizing-board-view.md)
- [Creating Personal and Team Dashboards in Jira](../08-dashboards-and-reports/01-personal-and-team-dashboards.md)

---

Previous: [Section overview](README.md) · Next: [Jira Etiquette: Do's and Don'ts for Real Teams](02-jira-etiquette.md)
