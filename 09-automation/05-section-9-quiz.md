---
title: "Section 9 Quiz"
aliases:
  - "Section 9 Quiz"
type: quiz
section: 9
lesson: 5
duration: ""
status: done
tags:
  - jira
  - section/09
  - quiz
  - flashcards
---

# Section 9 Quiz

[Course home](../README.md) › [Section 9: Jira Automation](README.md) › Quiz

> [!IMPORTANT]
> The official Udemy quiz questions are not reproduced here. The practice questions and flashcards below are original and cover the same topics.

## Topics covered

- [What Can Be Automated in Jira by Non-Admins?](01-what-non-admins-can-automate.md)
- [Smart Checklists: Creating Reusable Checklists in Jira Issues](02-smart-checklists.md)
- [Examples of Simple Automation Rules for Teams](03-simple-automation-rules.md)
- [When to Ask Admins for Help with Jira Automation](04-when-to-ask-admins.md)

## Practice questions

<details>
<summary>1. You are a space admin but not a Jira admin. Can you create an automation rule that emails the assignee when a work item is assigned in your space?</summary>
Yes. Space admins can create and manage automation rules within spaces they administer.
</details>

<details>
<summary>2. Design the rule: notify the assignee by email when someone else assigns them a work item. List trigger, condition, and action.</summary>
Trigger: work item assigned. Condition (JQL): assignee != currentUser(). Action: send email to assignee with smart values for key and summary.
</details>

<details>
<summary>3. A support team wants closed tickets to reopen when a customer comments. Design the rule.</summary>
Trigger: work item commented. Condition: status equals Done. Action: transition work item to Open.
</details>

<details>
<summary>4. Why should you use Transition work item instead of Edit work item when changing status in a rule?</summary>
Workflows control valid status changes through transitions. The transition action follows those paths; edit may not offer or allow a direct status change.
</details>

<details>
<summary>5. An HR space creates many work items with "onboarding" in the title. Design a rule to tag them automatically.</summary>
Trigger: work item created. Condition: summary contains onboarding. Action: edit work item to add label onboarding.
</details>

<details>
<summary>6. Should you ask a Jira admin to install Smart Checklist, or can a space admin do it?</summary>
Ask a Jira admin. Installing Marketplace apps requires site admin rights. Space admins enable and use the app after installation.
</details>

<details>
<summary>7. When is a checklist inside a work item preferable to subtasks?</summary>
When steps are lightweight verification items (Definition of Done checks) that do not need separate assignees, estimates, or board visibility.
</details>

<details>
<summary>8. Should you ask an admin? You built a reopen-on-comment rule in one space and now need the identical rule in twelve spaces.</summary>
Yes. Multi-space or global scope requires a Jira admin. Provide your tested trigger, conditions, actions, and the list of space keys.
</details>

<details>
<summary>9. Should you ask an admin? You want to auto-close all child work items when an epic reaches Done, but children live in three different spaces.</summary>
Yes. Cross-space parent/child automation needs global or multi-space scope, which only a Jira admin can configure.
</details>

<details>
<summary>10. What should you include in an admin request for a global automation rule?</summary>
Purpose, exact trigger, every condition, every action, target space keys, test cases, and expected behavior — ideally copied from a working prototype in your space.
</details>

<details>
<summary>11. A template closes all subtasks when the parent is marked Done. What risk should you consider before enabling it?</summary>
Teammates may not expect work items to close automatically and could lose track of work still in progress. Communicate the rule and enable it only when the team understands automation.
</details>

<details>
<summary>12. Where do you check whether a rule ran and troubleshoot failures?</summary>
The automation audit log under Space settings > Automation (or the global automation log for site-wide rules).
</details>

## Flashcards

What three parts make up an automation rule?::Trigger, optional conditions, and actions
Who can automate in a single space?::A space admin for that space
Who can create global multi-space rules?::A Jira admin
What is a trigger?::The event that starts a rule, such as work item assigned or work item commented
What is a condition?::A check that must pass before the next step runs
What is an action?::What the rule does, such as send email or transition work item
What is a smart value?::A placeholder like {{issue.key}} filled with live data when the rule runs
What is a branch (For each)?::Repeats actions over related items such as all subtasks of a parent
What does the automation audit log show?::History of rule executions for debugging and verification
Why test JQL in Filters before using it in automation?::The automation editor does not autocomplete JQL like search does
What trigger reopens a Done ticket on new feedback?::Work item commented, with status = Done, transition to Open
Which action changes workflow status in a rule?::Transition work item, not generic edit
What is Smart Checklist?::A Marketplace app that adds reusable checklists inside work items
Who installs Marketplace apps?::A Jira admin
What is a Definition of Done checklist?::Team agreement on verification steps before work is truly complete
Checklist vs subtask?::Checklists stay inside one work item; subtasks appear as separate board cards
What is global automation?::Site-wide rule management that can target multiple spaces; Jira admin only
Why prototype a rule locally first?::To prove it works and give admins an exact specification
What is rule scope?::Which spaces a rule applies to: one space, selected spaces, or global
What risk comes with auto-closing child work items?::Surprising teammates who did not know work was closed automatically
How many global templates on free Smart Checklist?::Five in the lesson demo

## Easy to confuse

| Concept A | Concept B | How to tell them apart |
|---|---|---|
| Trigger | Action | The trigger is the event that starts the rule. The action is what the rule does in response. |
| Condition | Action | A condition decides whether the next step runs. An action changes something — email, status, labels. |
| Space admin | Jira admin | Space admins automate inside their spaces. Jira admins can run global rules across many spaces and install apps. |
| Transition work item | Edit work item | Use transition for status changes through the workflow. Use edit for fields like labels, assignee, or description. |
| Checklist (Smart Checklist) | Subtask | Checklists are tick boxes inside one work item. Subtasks are separate work items with their own keys and board cards. |
| Space automation | Global automation | Same builder UI, but space automation is limited to one space; global automation can span the site and needs a Jira admin. |

---

Previous: [When to Ask Admins for Help with Jira Automation](04-when-to-ask-admins.md) · Next: [Section 10: Best Practices and Final Challenge](../10-best-practices/README.md)
