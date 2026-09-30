---
title: "Create Work Items: Epics, Stories & Subtasks"
aliases:
  - "Create Work Items: Epics, Stories & Subtasks"
type: lesson
section: 2
lesson: 3
duration: "21:23"
status: done
tags:
  - jira
  - section/02
  - topic/work-items
  - topic/epics
---

# Create Work Items: Epics, Stories & Subtasks

[Course home](../README.md) › [Section 2: Jira Fundamentals](README.md) › Lesson 3 · 21:23

## TL;DR

Work items (formerly *issues*) are created from the top **Create** button or from **Create issue** in the backlog. Start with **epics** for large themes, then add **stories**, **tasks**, and **bugs**, and assign each to an epic as its parent. **Subtasks** break individual stories into smaller steps. Epics live in the **Epics** panel, not in the main backlog list, because they span multiple sprints. The work item detail view holds the summary, description, fields, comments, history, and subtasks.

## Key concepts

- **Create dialog**: The full form opened by **Create** in the top bar. You can pick the space, work type, and all fields. The inline **Create issue** row in the backlog creates in the current space with fewer clicks.
- **Summary**: The short title of a work item. Keep it concise; put the full user-story wording in the description.
- **Work item key**: A unique ID combining the space key and a sequence number, such as `SP-1`. Numbers increment in creation order and are never reused, even after deletion.
- **Epic panel**: A sidebar list of epics in the backlog view. Epics are hidden from the main backlog by default so they do not clutter sprint planning.
- **Parent assignment**: Linking a story, task, or bug to an epic. Each middle-level item has one epic parent.
- **Priority vs rank**: **Priority** is a field (High, Medium, Low, and so on). **Rank** is the order in the backlog, changed by drag-and-drop. A item can be high in the backlog but have medium priority.
- **Reporter**: The person who created the work item, set automatically to you unless changed.
- **Assignee**: Who is responsible for the work. Can follow space defaults (automatic, unassigned, or project lead) or be set manually.
- **Activity tabs**: **Comments** for discussion, **History** for every field and status change, **Work log** for time tracking if the team uses it.

## How to do it in Jira

### Create an epic

1. Open the space backlog. If the view opens on **Active sprints** and looks empty, switch to **Backlog**.
2. Open **Create** in the top bar (or use the epic shortcut in the Epics panel when available).
3. Set **Work type** to **Epic**.
4. Leave **Status** as **To Do** for new work. Leave **Sprint** empty; epics sit above sprints.
5. Enter a **Summary** (for example *User account*) and a **Description** with scope notes.
6. Set **Assignee** if needed, then select **Create**.
7. If epics do not appear, open the **Epics** panel from the backlog toolbar and enable it.

### Create stories and other middle-level work items

1. In the backlog, use **Create issue** with **Story** selected, or open the full **Create** dialog.
2. Type a short summary (for example *Create user account*).
3. Open the work item and add a description in user-story form: *As a new customer, I want to register an account so that I can start collecting rewards.*
4. Assign a **parent epic** in either of these ways:
   - Click the **parent** control on the card and pick an epic from the list.
   - Drag the story onto the epic in the Epics panel.

### Color-code epics (optional)

1. Open an epic from the Epics panel and select **View details**.
2. Click the epic **color** swatch and pick a color.
3. Use consistent colors to distinguish themes, such as blue for end-user features and red for shop or vendor features.

### Filter the backlog by epic

1. In the **Epics** panel, click one or more epics.
2. The backlog list shows only work items linked to the selected epics.

### Create subtasks

1. Open a story, task, or bug.
2. In the detail view, select **Add** (or the subtask section) and choose **Subtask**.
3. Enter summaries such as *Gather requirements*, *Create design*, *Development*, and *Testing*.
4. Assign subtasks to different people if needed. Each subtask has its own status and fields.

Subtasks do not appear as separate cards in the main backlog list. Expand a parent card or open the parent detail view to see them. A small subtask icon on the card indicates children exist.

## Examples

The *Stamps and Points* app demo builds epics around major product areas:

| Epic | Scope |
|---|---|
| User account | Registration, profile, account management for customers |
| Managing cards | Shop owners issuing and updating loyalty cards |
| Collecting points | How customers earn stamps and points |
| Rewards | Redeeming perks at shops and restaurants |
| User management | Admin actions on customer accounts |
| Shop registration | Business sign-up for the vendor side |
| Tracking and analytics | Customer lists and demographics for shops |

Sample stories under **User account**:

- *Create user account* — parent epic: User account
- *Edit information in my account* — parent epic: User account

Sample stories under other epics:

- *Add new user* → User management
- *Sign up for business account* → Shop registration
- *List of customers and demographics* → Tracking and analytics

Subtasks under *Create user account* might include gather requirements, create design, development, and testing.

```sql
project = ABC AND issuetype = Epic ORDER BY created ASC
```

```sql
project = ABC AND parent = ABC-5
```

## Tips and pitfalls

- **Start with epics, then stories.** Epics frame the backlog before detailed items accumulate.
- **Short summaries, rich descriptions.** Put the "As a user…" wording in the description, not the title.
- **Active sprints may look empty.** New spaces often open on the sprint board before any sprint exists. Switch to **Backlog** to see epics and stories.
- **Focus on backlog rank over priority.** Drag-and-drop order drives what the team pulls next; the priority field is optional and can disagree with rank.
- **Save description edits.** After typing in the description, confirm with **Save** so changes persist.
- **Parent drag-and-drop can be finicky.** If dropping onto an epic fails, use the parent picker on the card instead.

> [!IMPORTANT]
> Epics are intentionally kept out of the main backlog list. Use the Epics panel to view and manage them; do not expect epic cards among sprint-ready stories.

> [!TIP]
> Color-coding epics by audience (customer-facing versus vendor-facing) makes a large backlog easier to scan without extra fields or labels.

## Review questions

<details>
<summary>Why are epics shown in a separate Epics panel instead of the main backlog?</summary>
Epics span multiple sprints and are too large for sprint planning. Showing them in the main list would clutter prioritization of sprint-ready work.
</details>

<details>
<summary>What is the difference between priority and backlog rank?</summary>
Priority is a field such as High or Medium on the work item. Rank is the order in the backlog, controlled by drag-and-drop. They are independent.
</details>

<details>
<summary>How is a work item key formed?</summary>
Space key plus a sequence number, such as SP-1 for the first item in space SP. Numbers increase with each new item and are not reused.
</details>

<details>
<summary>What are two ways to assign a story to an epic?</summary>
Use the parent control on the backlog card and select an epic, or drag the story onto the epic in the Epics panel.
</details>

<details>
<summary>Where do subtasks appear in the backlog view?</summary>
They are nested under their parent work item. Expand the parent card or open the parent detail view; they do not appear as top-level backlog cards.
</details>

## Related

- [Glossary](../reference/glossary.md)
- [Understanding Jira Work Types & Hierarchy](02-work-types-and-hierarchy.md)
- [Parent-Child Hierarchy vs Linked Work Items](04-parent-child-vs-linked-work-items.md)
- [Using Issue Labels and Priorities to Organize Work in Jira](../04-organizing-work/01-labels-and-priorities.md)

---

Previous: [Understanding Jira Work Types & Hierarchy](02-work-types-and-hierarchy.md) · Next: [Parent-Child Hierarchy vs Linked Work Items](04-parent-child-vs-linked-work-items.md)
