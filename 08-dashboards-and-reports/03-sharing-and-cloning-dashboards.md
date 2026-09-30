---
title: "Sharing and Cloning Dashboards with Stakeholders and Teams"
aliases:
  - "Sharing and Cloning Dashboards with Stakeholders and Teams"
type: lesson
section: 8
lesson: 3
duration: "2:51"
status: done
tags:
  - jira
  - section/08
  - topic/dashboards
---

# Sharing and Cloning Dashboards with Stakeholders and Teams

[Course home](../README.md) › [Section 8: Dashboards and Reports](README.md) › Lesson 3 · 2:51

## TL;DR

Dashboards are meant to be shared. Change **viewers** and **editors** anytime through **Rename or share**, refresh data manually or on a schedule, and **Copy** an existing dashboard when you want the same gadget layout for a different audience. **Wallboard** mode strips away Jira chrome for a fullscreen rotation—handy on an office display, though not every gadget supports it.

## Key concepts

- **Rename or share**: The dashboard action that updates title, description, viewers, and editors after creation.
- **Dashboard refresh**: Manual refresh reloads all gadgets; optional automatic refresh can apply to the whole dashboard instead of configuring each gadget separately.
- **Copy dashboard**: Creates a new dashboard from an existing one, including gadgets and layout. You set a new name and fresh sharing permissions.
- **Wallboard**: A fullscreen, minimal-UI view of one or more dashboards for display on a monitor. Gadgets may rotate on a timer; not all gadget types render in wallboard mode.

## How to do it in Jira

1. Open the dashboard and select **Rename or share** (wording may appear as **Share** or **⋯ > Share** depending on your Jira version).
2. Add **Viewers** (people, groups, or the whole organization) when a private dashboard should become a team or stakeholder view. Adjust **Editors** only for people who should change gadgets—not everyone who reads the page.
3. Select **Add** next to each person or group you enter in the sharing dialog. Skipping **Add** leaves them off the permission list even if you typed their name.
4. Save the dialog. Viewers can open the dashboard from **Dashboards** in the sidebar; they still need permission to see the underlying saved filters.
5. To refresh data, use the dashboard **Refresh** control. For automatic refresh, open dashboard settings and enable site-wide or dashboard-level auto-refresh if available—otherwise configure refresh on individual gadgets.
6. To duplicate, choose **Copy dashboard**, enter a new name, set viewers and editors, click **Add** for each permission entry, then confirm **Copy**.
7. For a display screen, open **View as wallboard**. Configure rotation interval and optionally cycle through multiple dashboards. Press **Esc** to exit wallboard mode.

## Examples

A Scrum Master shares **Sprint health – ABC** with the organization as viewers but keeps themselves as the only editor. Stakeholders see burndown and filter gadgets without rearranging the layout before demo day.

A program manager copies **Version 3.2 status** to **Version 3.3 status**, swaps the saved filters inside each gadget, and leaves the original dashboard untouched for historical comparison.

## Tips and pitfalls

- **Click Add in the sharing dialog.** Names typed into viewer or editor fields are not saved until you confirm each with **Add**—a common reason sharing appears to fail.
- **Filters need their own sharing.** A shared dashboard shows empty gadgets for anyone who cannot view the saved filters behind them.
- **Copy before big experiments.** Duplicate a working dashboard, then edit the copy so a proven layout stays available.
- **Wallboard limits.** Test wallboard mode before mounting a TV in the team area; unsupported gadgets may be hidden or simplified.

> [!IMPORTANT]
> Viewers and editors are separate from filter permissions. Share both the dashboard and its underlying filters (or use filters already visible to the organization).

## Review questions

<details>
<summary>How do you let colleagues view a dashboard you created as private?</summary>
Open Rename or share, add them (or a group or the organization) as viewers, click Add for each entry, and save.
</details>

<details>
<summary>Why might a copied dashboard show blank gadgets for some users?</summary>
The gadgets still point to saved filters those users cannot view. Share the filters or recreate them with broader visibility.
</details>

<details>
<summary>What is wallboard mode for?</summary>
A fullscreen display of dashboard gadgets with minimal Jira UI, often rotated on a timer for office monitors or status screens.
</details>

<details>
<summary>When is Copy dashboard better than editing the original?</summary>
When you want the same layout for a new release, team, or audience without losing the original dashboard configuration.
</details>

## Related

- [Glossary](../reference/glossary.md)
- [Reports and Metrics](../reference/reports-and-metrics.md)
- [Creating Personal and Team Dashboards in Jira](01-personal-and-team-dashboards.md)
- [Useful Gadgets for Your Jira Dashboard: Filters, Charts, and More](02-useful-dashboard-gadgets.md)
- [Creating and Saving Filters in Jira for Quick Access](../05-filters-and-jql/02-creating-and-saving-filters.md)

---

Previous: [Useful Gadgets for Your Jira Dashboard: Filters, Charts, and More](02-useful-dashboard-gadgets.md) · Next: [Scrum Reports: Velocity, Burndown, and Sprint Report Explained](04-scrum-reports.md)
