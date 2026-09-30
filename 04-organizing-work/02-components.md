---
title: "Structuring Work with Components in Jira Projects"
aliases:
  - "Structuring Work with Components in Jira Projects"
type: lesson
section: 4
lesson: 2
duration: "6:40"
status: done
tags:
  - jira
  - section/04
  - topic/components
---

# Structuring Work with Components in Jira Projects

[Course home](../README.md) › [Section 4: Organizing Your Work](README.md) › Lesson 2 · 6:40

## TL;DR

**Components** group work items (formerly *issues*) within a single space by subsystem or platform (for example iOS and Android). Unlike labels, they are defined by a space admin, stay inside that space, and can have a **component lead** and **default assignee**. A work item can have multiple components. Components work well when the team needs controlled vocabulary instead of everyone inventing labels.

## Key concepts

- **Component**: A space-level category for work items, often mapped to a part of the product (a platform, service, or feature area).
- **Component lead**: The person responsible for work in that component. Shown in space settings and available when filtering or reporting.
- **Default assignee**: Who gets new work items when that component is the first one selected at creation time. Options typically include component lead, project lead, or unassigned.
- **Compass components**: Atlassian's newer software-component catalog. The lesson uses classic **Jira components** instead; look for **Switch to Jira components** if Compass appears in space settings.
- **Space admin**: Only users with permission to open **Space settings** (formerly *project settings*) can create or edit components.

## Labels vs components

| | Labels | Components |
|---|---|---|
| Who creates them | Anyone editing a work item | Space admin in space settings |
| Scope | Whole Jira site; shared across spaces | One space only |
| Cleanup | Hard to remove; typos spread | Admin-controlled list |
| Extra metadata | None | Component lead, default assignee, description |
| Typical use | Flexible tags, OKRs, experiments | Platforms, modules, owned subsystems |

Both can power board quick filters and JQL searches.

## How to do it in Jira

### Create components (space admin)

1. In the sidebar, find the space (not the board). Open the space menu (**⋯**) and choose **Space settings** (may still say **Project settings** in some UIs).
2. Open **Components**. If you see Compass, choose **Switch to Jira components**.
3. Select **Create component**.
4. Enter a **Name** (for example `iOS`), optional **Description**, **Component lead**, and **Default assignee**, then save.
5. Repeat for other components (for example `Android` with a different lead).

### Assign a component to a work item

1. Open a work item and expand **More fields** if **Component** is not visible (location can vary if an admin customized the screen).
2. Click **Component** and select one or more components (for example `iOS` and `Android` if the work spans both).
3. Save. On a **new** work item, the first component selected may set **Assignee** from the component's default. On an **existing** unassigned item, adding a component later usually does not change assignee.

### Filter the board by component

1. Open **Manage quick filters** from the board.
2. Create a filter named for the component (for example `iOS`) with JQL such as `component = iOS`.
3. Return to the board, show quick filters, and click the filter to see only matching work items.

## Examples

For *Stamps and Points*, the mobile team creates **iOS** and **Android** components. A story *Redesign stamp card on phone* gets component **iOS**; a shared API change gets both **iOS** and **Android**.

JQL to find all Android work in the demo space:

```sql
component = Android AND project = ABC
```

Compare with a label-based query that could appear in any space:

```sql
labels = mobile-android
```

The lesson notes that labels remain available even in team-managed spaces, while components follow the admin-defined list for that company-managed space.

## Tips and pitfalls

- **Create components before assigning them.** The Component field shows no matches until an admin defines at least one component in space settings.
- **Pick labels or components deliberately.** Labels are fast and global but messy without discipline. Components add governance but only exist in one space and require an admin to change.
- **Default assignee applies at creation time.** Changing component on an already-created, unassigned work item does not automatically assign someone — only the initial selection during create typically does.
- **Compass vs Jira components.** New sites may prompt for Compass; switch to Jira components to match the classic workflow shown in the course.

> [!NOTE]
> Component availability and the exact settings path depend on space type (company-managed vs team-managed) and permissions. If **Components** is missing, an admin may need to enable the field or grant space settings access.

## Review questions

<details>
<summary>Who can create a new component?</summary>
A space admin with access to Space settings. Regular users can select existing components on work items but cannot add new component names from the work item form alone.
</details>

<details>
<summary>How do components differ from labels in scope?</summary>
Components belong to one space. Labels are shared across the whole Jira site and can be added from any space where the field is available.
</details>

<details>
<summary>Can one work item have more than one component?</summary>
Yes. You can select multiple components on the same work item, for example when a change affects both iOS and Android.
</details>

<details>
<summary>When does the default assignee for a component take effect?</summary>
Usually when the work item is first created and that component is the first one selected. Assigning a component later on an existing unassigned item typically does not change the assignee.
</details>

<details>
<summary>What are component lead and default assignee used for?</summary>
Component lead identifies the owner of that subsystem. Default assignee sets who receives new work items created with that component as the first selection.
</details>

## Related

- [Glossary](../reference/glossary.md)
- [Using Issue Labels and Priorities to Organize Work in Jira](01-labels-and-priorities.md)
- [Team-Managed vs Company-Managed Spaces](../02-jira-fundamentals/01-team-managed-vs-company-managed-spaces.md)
- [Planning and Releasing with Versions in Jira](03-versions-and-releases.md)

---

Previous: [Using Issue Labels and Priorities to Organize Work in Jira](01-labels-and-priorities.md) · Next: [Planning and Releasing with Versions in Jira](03-versions-and-releases.md)
