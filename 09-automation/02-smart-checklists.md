---
title: "Smart Checklists: Creating Reusable Checklists in Jira Issues"
aliases:
  - "Smart Checklists: Creating Reusable Checklists in Jira Issues"
type: lesson
section: 9
lesson: 2
duration: "5:29"
status: done
tags:
  - jira
  - section/09
  - topic/checklists
---

# Smart Checklists: Creating Reusable Checklists in Jira Issues

[Course home](../README.md) › [Section 9: Jira Automation](README.md) › Lesson 2 · 5:29

## TL;DR

**Smart Checklist for Jira** is a Marketplace app that adds reusable checklists inside work items (formerly *issues*). It is not installed by default; a Jira admin installs it from **Apps**. Once enabled for a space, you attach checklist templates — such as a **Definition of Done** — to stories and tick items off without creating subtasks. Templates can be reused across spaces, and automation rules can append a checklist when new work items match certain criteria.

## Key concepts

- **Marketplace app**: Software from the Atlassian Marketplace that extends Jira. Apps install at the site level and must be enabled per space before use.
- **Smart Checklist for Jira**: A third-party checklist app with free and paid tiers. The free tier on a Jira Cloud free site supports a limited number of global templates (five in the lesson demo).
- **Checklist template**: A saved list of steps — for example code review, tests passed, documentation updated — that you import into individual work items.
- **Definition of Done (DoD)**: A team agreement on what "done" means beyond writing code: tests, reviews, deployment, product-owner sign-off, and similar gates.
- **Global template**: A template stored at the app level and available in any space where Smart Checklist is enabled.
- **Checklist vs subtask**: A checklist keeps small verification steps inside one work item. Subtasks appear as separate cards on the board and add overhead when you only need a quick tick list.

## How to do it in Jira

### Install the app (Jira admin)

1. Open **Apps** in the top navigation (visible only if you are a Jira admin).
2. Select **Explore more apps** and search for *Smart Checklist*.
3. Choose **Smart Checklist for Jira** (Free or Pro depending on your plan) and select **Get it now**.
4. Complete the installation prompts and wait for the app to finish setting up.

### Enable the app for a space

1. Return to **Apps**, open Smart Checklist, and go to **Settings** (not just the getting-started guide).
2. Confirm Smart Checklist is **enabled** for the target space (for example the *Stamps and Points* space).

### Use a checklist on a work item

1. Open a work item from the backlog or board.
2. Scroll to the bottom of the fields panel on the right and expand **Smart Checklist**.
3. Open **Managed templates** to browse built-in and custom templates.
4. Select a template such as **Definition of Done** and choose **Import** to add it to this work item.
5. Tick items off as you complete each step.

### Create or edit a template (optional)

1. From the Smart Checklist panel, open template management.
2. Create a new global template or edit an existing one to match your team's DoD.
3. On the free tier, delete an unused template if you hit the five-template limit.

## Examples

### Definition of Done for a software story

Import the DoD template onto story `ABC-42` (*Add loyalty stamp counter*). The checklist might include:

- Unit tests pass
- Code review approved
- Documentation updated
- Deployed to staging
- Product owner verified

Each item is checked in place. No extra subtasks clutter the sprint board.

### HR onboarding story without subtask sprawl

An onboarding story could carry a checklist (*Create email account*, *Assign laptop*, *Schedule orientation*) instead of three subtasks that would each appear as board cards.

### Automation hook (mentioned in the lesson)

Combine Smart Checklist with a space automation rule: when a work item is created and matches your criteria, an action appends a chosen checklist template automatically. Build the rule in **Space settings > Automation** after the app is installed.

## Tips and pitfalls

- **Admin required for install.** Regular space admins can use checklists once the app is enabled, but only a Jira admin can install Marketplace apps.
- **Find the panel at the bottom.** Smart Checklist appears among the fields on the right side of the work item view, often below standard Jira fields.
- **Prefer checklists for lightweight steps.** Reserve subtasks for work that needs its own assignee, estimate, or board visibility.
- **Watch template limits on free tiers.** Plan which global templates matter most before creating new ones.

> [!NOTE]
> Your company site may not have Smart Checklist installed, or may use a different checklist app. The lesson uses Smart Checklist to show how Marketplace apps integrate into Jira; the same pattern applies to other apps.

## Review questions

<details>
<summary>Who can install Smart Checklist from the Marketplace?</summary>
A Jira admin. Space admins can enable and use the app in their spaces after installation, but they cannot install new apps site-wide.
</details>

<details>
<summary>Where do you find the Smart Checklist panel on a work item?</summary>
At the bottom of the fields on the right-hand side of the work item detail view.
</details>

<details>
<summary>Why might a team use a Definition of Done checklist instead of subtasks?</summary>
Checklists keep verification steps inside one work item without creating separate subtask cards that clutter the board and add tracking overhead.
</details>

<details>
<summary>How many global templates does the free Smart Checklist tier allow in the lesson demo?</summary>
Five global templates. Creating a sixth requires deleting or replacing an existing one.
</details>

## Related

- [Glossary](../reference/glossary.md)
- [What Can Be Automated in Jira by Non-Admins?](01-what-non-admins-can-automate.md)
- [Examples of Simple Automation Rules for Teams](03-simple-automation-rules.md)
- [Create Work Items: Epics, Stories & Subtasks](../02-jira-fundamentals/03-create-epics-stories-subtasks.md)

---

Previous: [What Can Be Automated in Jira by Non-Admins?](01-what-non-admins-can-automate.md) · Next: [Examples of Simple Automation Rules for Teams](03-simple-automation-rules.md)
