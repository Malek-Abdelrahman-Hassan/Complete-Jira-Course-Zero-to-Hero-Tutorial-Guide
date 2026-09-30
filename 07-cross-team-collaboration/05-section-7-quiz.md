---
title: "Section 7 Quiz"
aliases:
  - "Section 7 Quiz"
type: quiz
section: 7
lesson: 5
duration: ""
status: done
tags:
  - jira
  - section/07
  - quiz
  - flashcards
---

# Section 7 Quiz

[Course home](../README.md) › [Section 7: Cross-Team Collaboration](README.md) › Quiz

> [!IMPORTANT]
> The official Udemy quiz questions are not reproduced here. The practice questions and flashcards below are original and cover the same topics.

## Topics covered

- [Managing Cross-Team Work in Jira: Best Practices](01-managing-cross-team-work.md)
- [Creating and Using Shared Boards for Team Collaboration](02-shared-boards.md)
- [Roadmaps in Jira: Visualizing Plans and Dependencies](03-roadmaps-plans-and-dependencies.md)
- [What to Do When Statuses Don't Match Across Teams](04-mismatched-statuses-across-teams.md)

## Practice questions

<details>
<summary>1. The Stamps and Points team and the App Store team each have their own space. Why not move all App Store work items into the development space?</summary>
Each team has different workflows, ownership, and backlogs. App Store management handles many apps; development runs Scrum sprints. Separate spaces stay clean; coordination uses shared filters, boards, labels, and meetings instead of merging backlogs.
</details>

<details>
<summary>2. You need a board showing iOS release 3.2.0 work from space ABC (component iOS) and space XYZ (label SP app). What is the board source?</summary>
A saved JQL filter that ORs two scoped sub-queries, then a board created with the advanced filter-based option selecting that saved filter.
</details>

<details>
<summary>3. Both ABC and XYZ have a fix version named 3.2.0. Are they one shared version in Jira?</summary>
No. Fix versions belong to a space. Identical names are for human readability; Jira stores separate version records. A shared board may show both in the version panel.
</details>

<details>
<summary>4. After the App Store team moves items to In Review, they vanish from your shared Scrum board and backlog. What is the most likely cause?</summary>
In Review is unmapped on the board. Go to Board settings, Layout, Columns, and map unmapped statuses from foreign workflows to the correct columns.
</details>

<details>
<summary>5. Write JQL to find all actively worked release items from ABC (iOS, 3.2.0) and XYZ (SP app, 3.2.0) regardless of whether the status is called In Progress, In Review, or Ready for QA.</summary>
Wrap the OR filter in parentheses and add AND statusCategory = "In Progress". Example: ((project = ABC AND fixVersion = "3.2.0" AND component = iOS) OR (project = XYZ AND fixVersion = "3.2.0" AND labels = "SP app")) AND statusCategory = "In Progress"
</details>

<details>
<summary>6. Can you use Timeline on a board whose filter spans ABC and XYZ?</summary>
No, on any plan: Timeline only works with work items from one space. To plan across ABC and XYZ, use Plans, which needs Jira Premium or Enterprise. Practice Timeline on a single-space board; the dependency and sprint-planning concepts are the same.
</details>

<details>
<summary>7. On Timeline you drag a link from story ABC-12 onto ABC-36. What relationship does that create, and why does it matter?</summary>
A blocks link (unless you pick another link type). Dependencies show sequencing risk on the timeline, especially when date ranges overlap in the same sprint.
</details>

<details>
<summary>8. A teammate adds an App Store story to your active sprint from the shared board without asking the team. What is wrong with that?</summary>
It changes sprint scope without agreement. Cross-team items belong in the sprint only after shared planning; otherwise commitment and velocity lose meaning.
</details>

<details>
<summary>9. You want one filter to track every unreleased version for both teams instead of naming 3.2.0. What JQL function helps?</summary>
unreleasedVersions(), used as fixVersion in unreleasedVersions() inside each sub-query of the OR filter.
</details>

<details>
<summary>10. When saving the cross-team release filter, why share view access with the organization but restrict editors?</summary>
The organization needs to run the filter for the shared board. Restricting editors protects the JQL from accidental changes that would break the board for everyone.
</details>

<details>
<summary>11. Timeline is empty for an epic you know is in the backlog. The board uses Scrum scheduling. What should you check first?</summary>
Whether the epic's work items are in a sprint that has dates and appears on the timeline. Epics with no sprint placement may not show on a sprint-based timeline until scheduled.
</details>

<details>
<summary>12. You add a third space to an existing shared filter. The filter results look correct but the board shows fewer cards. What two places should you check?</summary>
Board settings, Layout, Columns for new unmapped statuses from the third workflow, and whether any new statuses need mapping every time a space joins the board.
</details>

## Flashcards

What is cross-team work in Jira?::Work that spans two or more teams or spaces where progress in one affects another
Why keep separate spaces for each team?::Different workflows, backlogs, and ownership; coordination layers sit on top
How does App Store space XYZ mark Stamps and Points work?::Label SP app on relevant work items
What pre-work scopes ABC items to iOS release 3.2.0?::Fix version 3.2.0 plus component iOS
What powers a shared cross-space board?::A saved JQL filter used as the board source
Are fix versions with the same name in two spaces the same object?::No — each space has its own version record
What JQL combines two spaces with different scoping rules?::Parenthesized sub-queries joined with OR
When should you share a cross-team filter with the organization?::When it powers a board or dashboard the team uses together
Why restrict filter editors to yourself?::To prevent accidental JQL changes that break shared views
What is an unmapped status?::A workflow status not assigned to any board column; cards in it may disappear
Where do you map statuses on a shared board?::Board settings, Layout, Columns
Can unmapped statuses hide items from the Scrum backlog?::Yes, not only from sprint columns
What is status category?::To Do, In Progress, or Done grouping that every status maps to
Why filter on statusCategory for cross-team dashboards?::Status names differ across workflows but categories align
What JQL finds all unreleased versions?::fixVersion in unreleasedVersions()
What is Timeline formerly called?::Roadmap in a space
What schedule mode suits Scrum teams on Timeline?::Sprint dates rather than start and due dates
Does Timeline work across several spaces?::No, on any plan; cross-space planning uses Plans (Premium and Enterprise)
How do you create a blocks link on Timeline?::Hover the link icon on one bar and drag to the blocked item
What happens if you add a story to a sprint from Timeline?::Sprint scope changes — treat it like backlog sprint assignment
When may App Store items join the development sprint?::Only after explicit shared planning with both teams

## Easy to confuse

| Concept A | Concept B | How to tell them apart |
|---|---|---|
| Shared board | Space default board | A shared board is built from a saved filter and can show work from multiple spaces. A space default board shows work from one space only. |
| Fix version name | Fix version record | Two spaces can both label a release 3.2.0, but each space stores its own version object. |
| Status | Status category | Status is the workflow step name (In Review). Category is the reporting bucket (In Progress) shared across workflows. |
| Timeline | Shared filter board | Timeline is the schedule view. A shared board is any filter-sourced board; Timeline only works when that filter covers one space. |
| Unmapped status | Filter mismatch | Unmapped statuses hide cards on a board whose filter still finds them in search. A filter problem changes search results too. |
| Component (ABC) | Label SP app (XYZ) | Both scope cross-team work, but components are space-defined fields; labels are free-text tags anyone with edit access can add. |

---

Previous: [What to Do When Statuses Don't Match Across Teams](04-mismatched-statuses-across-teams.md) · Next: [Section 8: Dashboards and Reports](../08-dashboards-and-reports/README.md)
