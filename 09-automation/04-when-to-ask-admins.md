---
title: "When to Ask Admins for Help with Jira Automation"
aliases:
  - "When to Ask Admins for Help with Jira Automation"
type: lesson
section: 9
lesson: 4
duration: "4:26"
status: done
tags:
  - jira
  - section/09
  - topic/automation
---

# When to Ask Admins for Help with Jira Automation

[Course home](../README.md) › [Section 9: Jira Automation](README.md) › Lesson 4 · 4:26

## TL;DR

Space admins automate inside one space; **global automation** requires a Jira admin. Before requesting a global rule, prototype it locally, document the exact trigger, conditions, and actions, and specify which spaces it should cover. The lesson demonstrates a cross-space epic rule: when an epic moves to **Done**, every child work item (formerly *issue*) that is not already Done is transitioned to Done — including children in other spaces linked to the same epic.

## Key concepts

- **Global automation**: Site-wide rule management with the same builder UI as space automation, but rules can target multiple spaces at once. Only Jira admins access it.
- **Rule scope**: Where a rule applies — a single space, selected spaces, or globally across the site. Space admins control single-space scope; multi-space and global scope need a Jira admin.
- **Prototype first**: Build and test the rule in a space you administer, then hand the working recipe to an admin for global rollout.
- **Detailed admin request**: Include trigger, every condition, every action, target spaces, and expected behavior. Vague requests lead to back-and-forth testing.
- **Cross-space parent/child**: An epic in one space can have child work items in another space. Global rules are the practical way to sync status across that boundary.
- **Change communication**: Rules that auto-transition work items affect everyone in the affected spaces. Tell the team before enabling them.

## Space admin vs Jira admin

| Capability | Space admin | Jira admin |
|---|---|---|
| Create rules in one space | Yes | Yes |
| Choose a single-space scope | Yes | Yes |
| Apply one rule to multiple spaces | No | Yes |
| Global automation console | No | Yes |
| Install Marketplace apps | No | Yes |

## How to do it in Jira

### Prototype in your space

1. Build the rule under **Space settings > Automation** in a space you admin.
2. Test triggers, conditions, and actions with real work items.
3. Note exact component names, field values, and JQL if used.

### Request a global rule from a Jira admin

1. Write a specification: purpose, trigger, conditions, actions, and list of space keys.
2. Describe test cases and edge cases (for example what happens to work items already in Done).
3. Ask the admin to set **Rule details > Scope** to the needed spaces or global.
4. Request a short verification window after go-live.

### Enable a global rule (Jira admin)

1. Open **Global automation** from the space automation screen or site **Settings > Automation** (exact entry point may vary by Jira version).
2. Start from a template or clone the prototype rule.
3. In **Rule details**, set scope to **Global**, **Multiple projects**, or selected spaces.
4. Turn the rule on and monitor the audit log.

## Examples

### Close all epic children when the epic is Done (cross-space)

- **Trigger**: Work item transitioned → status **Done**
- **Branch**: For each **child** work item of the trigger work item
- **Condition**: Status is not **Done**
- **Action**: Transition work item → **Done**
- **Scope**: Global or multiple spaces (including the *Stamps and Points* space and an *App store* space)

The lesson links work item `APPL-10` from a second space as a child of epic `SP-1`. When `SP-1` moves through **In Progress** to **Done**, every linked child — regardless of space — transitions to **Done** automatically.

### When to stay local (no admin needed)

- Email the assignee on assignment within one team space.
- Reopen on comment for a single support space.
- Auto-label onboarding stories in your HR space.

### When to involve an admin

- The same reopen-on-comment rule must run in five team spaces.
- Parent/child status sync crosses space boundaries.
- A rule must integrate with a site-wide app or send email through a restricted mail handler.

## Tips and pitfalls

- **Vague tickets waste time.** "Please automate epic closing" is not enough. Attach the tested rule structure or screenshots from your prototype.
- **Surprise auto-closes erode trust.** Teammates searching for active work items that silently moved to Done will lose confidence in Jira. Announce global rules before activation.
- **Global does not mean careless.** Start with the smallest scope that solves the problem — two spaces, not the whole site — when the admin offers that option.
- **You can do a lot locally.** Most day-to-day team automation stays within space admin rights; reserve admin requests for cross-space or site-wide needs.

> [!IMPORTANT]
> Prototype locally, document precisely, then ask. Admins implement faster when you deliver a working recipe instead of a rough idea.

## Review questions

<details>
<summary>What is the main difference between space automation and global automation?</summary>
Space automation applies to one space and is managed by a space admin. Global automation can target multiple spaces or the whole site and is managed by a Jira admin.
</details>

<details>
<summary>Why should you build a rule in your own space before asking an admin?</summary>
You can prove the trigger, conditions, and actions work, catch edge cases, and give the admin an exact specification instead of a vague request that requires trial-and-error.
</details>

<details>
<summary>Should you ask an admin: "Please add a rule that closes things when epics finish"?</summary>
No — that is too vague. Provide the trigger (epic transitioned to Done), branch (for each child), condition (status not Done), action (transition to Done), and the space keys involved.
</details>

<details>
<summary>In the cross-space epic demo, why did closing SP-1 also change APPL-10?</summary>
APPL-10 was linked as a child of epic SP-1 even though it lives in a different space. A global (or multi-space) rule transitioned every non-Done child when the epic reached Done.
</details>

## Related

- [Glossary](../reference/glossary.md)
- [What Can Be Automated in Jira by Non-Admins?](01-what-non-admins-can-automate.md)
- [Examples of Simple Automation Rules for Teams](03-simple-automation-rules.md)
- [Parent-Child Hierarchy vs Linked Work Items](../02-jira-fundamentals/04-parent-child-vs-linked-work-items.md)

---

Previous: [Examples of Simple Automation Rules for Teams](03-simple-automation-rules.md) · Next: [Section 9 Quiz](05-section-9-quiz.md)
