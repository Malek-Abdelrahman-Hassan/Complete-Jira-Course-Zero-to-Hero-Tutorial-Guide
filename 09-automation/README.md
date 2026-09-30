---
title: "Jira Automation: Save Time Without Admin Rights"
short_title: "Jira Automation"
aliases:
  - "Section 9 — Jira Automation: Save Time Without Admin Rights"
  - "Section 09 overview"
type: section
section: 9
tags:
  - jira
  - section/09
---

# Section 9 — Jira Automation: Save Time Without Admin Rights

[Course home](../README.md) · Previous: [Section 8: Dashboards and Reports](../08-dashboards-and-reports/README.md) · Next: [Section 10: Best Practices and Final Challenge](../10-best-practices/README.md)

## What you will learn

By the end of this section you should be able to:

- Identify what can be automated without Jira admin rights.
- Create reusable checklists inside work items.
- Build simple automation rules from a trigger, conditions, and actions.
- Recognize when a request needs a Jira admin.

## Lessons

<!-- BEGIN generated: lessons -->

| # | Lesson | Type | Duration | Notes |
|---:|---|---|---:|---|
| 1 | [What Can Be Automated in Jira by Non-Admins?](01-what-non-admins-can-automate.md) | Video | 10:17 | Done |
| 2 | [Smart Checklists: Creating Reusable Checklists in Jira Issues](02-smart-checklists.md) | Video | 5:29 | Done |
| 3 | [Examples of Simple Automation Rules for Teams](03-simple-automation-rules.md) | Video | 5:24 | Done |
| 4 | [When to Ask Admins for Help with Jira Automation](04-when-to-ask-admins.md) | Video | 4:26 | Done |
| 5 | [Section 9 Quiz](05-section-9-quiz.md) | Quiz | — | Done |

**Video time:** 25:36 · **Notes completed:** 5 / 5

<!-- END generated: lessons -->

## Key takeaways

- **Space admins automate locally.** If you administer a space, you can build rules under **Space settings > Automation** without Jira admin rights.
- **Rules have three layers.** Every rule needs a **trigger** (when), optional **conditions** (if), and **actions** (then). Branches apply actions to sets such as all subtasks.
- **Smart values personalize actions.** Placeholders like `{{issue.key}}` and `{{assignee.displayName}}` insert live work item data into emails and other actions.
- **Small rules solve real problems.** Reopen on comment, auto-label by keyword, and assignee email notifications are practical starting points.
- **Checklists reduce subtask clutter.** Marketplace apps such as Smart Checklist add reusable Definition of Done lists inside a work item instead of extra board cards.
- **Prototype before you escalate.** Build and test a rule in your space, then hand a detailed specification to a Jira admin for global or multi-space rollout.
- **Global automation is admin territory.** Cross-space parent/child status sync and site-wide rules require a Jira admin and careful communication with affected teams.
- **Impact beats intent.** Auto-closing related work items can surprise teammates. Enable aggressive templates only when the team understands automation and you have announced the change.

## Hands-on practice

Suggested exercises for a free Jira Cloud site (these are not part of the official course material):

1. Open **Space settings > Automation** in a space you administer. Browse **Templates** and **Rules**, and note the monthly **Usage** counter for your plan.
2. Create a rule: when a work item is assigned and the assignee is not the current user, send an email to the assignee with smart values for the work item key and summary.
3. Add a JQL condition (`assignee != currentUser()`), test self-assignment vs assigning to another user, and confirm results in the **Audit log**.
4. Build a *Reopen when commented* rule: trigger *Work item commented*, condition status = Done, action *Transition work item* to Open. Close a test work item, comment on it, and verify the reopen.
5. Build an auto-label rule: when a work item is created and the summary contains a keyword your team uses, add a matching label automatically.
6. If you have Jira admin access on a practice site, install **Smart Checklist for Jira** (Free), enable it for your space, and import a **Definition of Done** template onto a story.
7. Draft a one-page admin request describing a rule you tested locally that should apply to multiple spaces, including trigger, conditions, actions, and space keys.

## References

- [Glossary](../reference/glossary.md)
