---
title: "Creating and Using Shared Boards for Team Collaboration"
aliases:
  - "Creating and Using Shared Boards for Team Collaboration"
type: lesson
section: 7
lesson: 2
duration: "7:35"
status: done
tags:
  - jira
  - section/07
  - topic/boards
  - topic/collaboration
---

# Creating and Using Shared Boards for Team Collaboration

[Course home](../README.md) › [Section 7: Cross-Team Collaboration](README.md) › Lesson 2 · 7:35

## TL;DR

A **shared board** shows work items from more than one space on a single board, powered by a saved JQL filter. For the *Stamps and Points* iOS release `3.2.0`, the course builds a filter that combines development work (version + iOS component) with App Store work (same version name + `SP app` label), saves it, and creates a Scrum board from that filter. The same pattern works with Kanban boards, broader version lists, or unreleased versions.

## Key concepts

- **Shared board**: A board whose source is a saved filter, not a single space. Any work item matching the JQL can appear, regardless of which space it lives in.
- **Pre-work for cross-team filters**: Align on release version names, components, labels, or epics before writing JQL so each side can tag its relevant work items.
- **Fix version per space**: Version names can match across spaces (both `3.2.0`), but each space maintains its own version object. The board may show two separate `3.2.0` entries in the version panel — one per space.
- **OR across spaces**: Combine sub-queries with `OR` inside parentheses so one filter pulls from two (or more) spaces with different scoping rules.
- **Filter permissions**: Share view access with the organization when the board is for cross-team use; keep edit access restricted so nobody accidentally breaks the JQL.

## How to do it in Jira

### Prepare both spaces

1. In *Stamps and Points* (`ABC`), create or confirm fix version `3.2.0` and assign it to work items in the release. Tag iOS-only items with the **iOS** component.
2. In App Store management (`XYZ`), create fix version `3.2.0` (a separate version record) and add label **`SP app`** to every work item related to the loyalty app.

### Build and save the filter

1. Open **Filters** (or **Search work items**) and switch to JQL.
2. Write a query that ORs two scoped sub-queries:

```sql
(
  (project = ABC AND fixVersion = "3.2.0" AND component = iOS)
  OR
  (project = XYZ AND fixVersion = "3.2.0" AND labels = "SP app")
)
ORDER BY rank ASC
```

3. Adjust columns — add **Component**, **Labels**, and **Fix versions** if helpful — and confirm both spaces appear in the results.
4. **Save filter** with a descriptive name (for example *Release of version 3.2.0*). Set **Viewers** to your organization; keep **Editors** limited to yourself unless a teammate maintains the query.

### Create a board from the filter

1. In the *Stamps and Points* space, choose **Create board** (or **Boards** > **Create board**).
2. Pick **Scrum** or **Kanban** depending on how you want to track the release.
3. Choose the **advanced** option and select **Filter** as the source.
4. Pick the saved filter *Release of version 3.2.0* and finish setup.

The new board shows development and App Store work items together. Sprint columns reflect the Scrum board's active sprint; App Store items appear when they match the filter.

### Broaden or narrow the filter

- **Several versions**: use `fixVersion in ("3.2.0", "3.3.0")` inside each sub-query.
- **All unreleased versions**: replace the version clause with `fixVersion in unreleasedVersions()` (JQL function).
- **Kanban instead of Scrum**: same filter, but track flow by status columns rather than sprints — useful when one team does not use sprints.

## Examples

Release coordination board for iOS `3.2.0`:

```sql
(
  (project = ABC AND fixVersion = "3.2.0" AND component = iOS)
  OR
  (project = XYZ AND fixVersion = "3.2.0" AND labels = "SP app")
)
ORDER BY rank ASC
```

Track every unreleased version across both teams:

```sql
(
  (project = ABC AND fixVersion in unreleasedVersions() AND component = iOS)
  OR
  (project = XYZ AND fixVersion in unreleasedVersions() AND labels = "SP app")
)
ORDER BY rank ASC
```

During shared sprint planning, both teams can review this board and, by agreement, pull App Store work items into the development team's sprint. Without that agreement, leave App Store items on the shared view only — do not silently expand sprint scope.

## Tips and pitfalls

- **Same version name, different records.** `3.2.0` in `ABC` and `3.2.0` in `XYZ` are two fix versions. That is normal; the version panel on a shared board may list both.
- **Scrum vs Kanban for mixed teams.** Scrum fits when the development team runs sprints and you occasionally co-plan scope. Kanban fits when one side tracks continuous flow without sprints.
- **Filters are not the only option.** Dashboards (covered in a later section) can show the same JQL in gadgets for stakeholders who do not live on a board.
- **Process still required.** The board shows status; it does not replace release meetings or handoff agreements between teams.

> [!IMPORTANT]
> Only add another team's work items to your active sprint after explicit shared planning. Otherwise sprint commitment and velocity lose meaning.

> [!NOTE]
> When a shared board pulls from multiple spaces with different workflows, some statuses may not appear until you map them — see the lesson on mismatched statuses.

## Review questions

<details>
<summary>What makes a board "shared" in the sense of this lesson?</summary>
Its source is a saved JQL filter that matches work items from more than one space, not a single space's default board.
</details>

<details>
<summary>Why does the filter use component = iOS on ABC but labels = "SP app" on XYZ?</summary>
The development space has multiple platforms; the iOS component scopes release work to the platform the App Store team cares about. The App Store space is iOS-focused by default, so the SP app label identifies work for the Stamps and Points app among many apps.
</details>

<details>
<summary>Two spaces both have fix version 3.2.0. Are they the same Jira object?</summary>
No. Fix versions belong to a space. Identical names are convenient for humans but Jira stores separate version records per space.
</details>

<details>
<summary>When saving a cross-team filter, who should be viewers vs editors?</summary>
Share view access with the organization (or the relevant group) so the shared board works for everyone. Restrict edit access — usually to yourself — so the JQL is not changed accidentally.
</details>

<details>
<summary>What JQL function finds all unreleased versions instead of naming one?</summary>
<code>unreleasedVersions()</code>, used inside a <code>fixVersion in unreleasedVersions()</code> clause.
</details>

## Related

- [Glossary](../reference/glossary.md)
- [Scrum vs Kanban](../reference/scrum-vs-kanban.md)
- [Creating and Saving Filters in Jira for Quick Access](../05-filters-and-jql/02-creating-and-saving-filters.md)
- [Understanding Jira Boards: Scrum, Kanban & Filters](../02-jira-fundamentals/05-boards-scrum-kanban-filters.md)
- [What to Do When Statuses Don't Match Across Teams](04-mismatched-statuses-across-teams.md)

---

Previous: [Managing Cross-Team Work in Jira: Best Practices](01-managing-cross-team-work.md) · Next: [Roadmaps in Jira: Visualizing Plans and Dependencies](03-roadmaps-plans-and-dependencies.md)
