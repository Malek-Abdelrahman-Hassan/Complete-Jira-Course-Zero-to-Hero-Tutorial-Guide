---
title: "Examples of Simple Automation Rules for Teams"
aliases:
  - "Examples of Simple Automation Rules for Teams"
type: lesson
section: 9
lesson: 3
duration: "5:24"
status: done
tags:
  - jira
  - section/09
  - topic/automation
---

# Examples of Simple Automation Rules for Teams

[Course home](../README.md) › [Section 9: Jira Automation](README.md) › Lesson 3 · 5:24

## TL;DR

Two practical rules show how triggers, conditions, and actions fit real team workflows. The first reopens a **Done** work item (formerly *issue*) when someone adds a comment — useful for support-style spaces where closed tickets come back to life. The second auto-adds an **onboarding** label when a newly created work item's summary contains that word, so HR work is easier to filter. Status changes use the **Transition work item** action, not a generic field edit.

## Key concepts

- **Work item commented trigger** (formerly *Issue commented*): Fires whenever a new comment is added to a work item, regardless of who wrote it.
- **Field condition**: Checks a field value — here, status equals *Done* — before the action runs.
- **Transition work item action**: Moves a work item through the workflow to a named status such as *Open*. Prefer this over *Edit work item* when changing status, because workflows may restrict which transitions are valid.
- **Work item created trigger** (formerly *Issue created*): Fires once when a new work item is saved.
- **Summary contains condition**: Matches text in the work item title. Useful for tagging work by keyword without manual labeling.
- **Edit work item action (labels)**: Adds or sets labels on the work item. Labels are lightweight tags anyone with edit access can also add by hand.

## How to do it in Jira

### Rule 1: Reopen when commented

1. Go to **Space settings > Automation** and select **Create rule**.
2. Set the **trigger** to *Work item commented*.
3. Add an **If** component: *Field value condition* — **Status** equals **Done**.
4. Add a **Then** action: search for *Transition* and choose **Transition work item**. Set the destination status to **Open**.
5. Name the rule (for example *Reopen when commented*), turn it on, and wait a moment for it to activate.
6. Test: move a work item to **Done**, add a comment, refresh, and confirm the status returns to **Open**.

### Rule 2: Auto-label onboarding work

1. Create a new rule with trigger *Work item created*.
2. Add an **If** condition: *Summary* **contains** `onboarding` (case sensitivity depends on the condition type — test if unsure).
3. Add a **Then** action: **Edit work item** → set **Labels** to `onboarding` (create the label if prompted).
4. Name the rule, turn it on, and test by creating a work item titled *Do user onboarding*.

## Examples

### Reopen when commented (support desk)

- **Trigger**: Work item commented
- **Condition**: Status = Done
- **Action**: Transition work item → Open

A customer comments on a closed support ticket saying the fix did not work. The rule moves the work item back to **Open** so the team does not miss it.

### Auto-label onboarding (HR team)

- **Trigger**: Work item created
- **Condition**: Summary contains `onboarding`
- **Action**: Edit work item → add label `onboarding`

New hire tasks are tagged automatically. Combine with a saved filter `labels = onboarding AND project = ABC` to build a board or dashboard view.

### Variation: match description too

Extend the condition with a second **If** branch or a JQL condition such as:

```sql
project = ABC AND (summary ~ onboarding OR description ~ onboarding)
```

This catches onboarding mentions in the description as well as the title.

## Tips and pitfalls

- **Use Transition, not Edit, for status.** The lesson first tried *Edit work item* for status and found no status field. Workflow transitions are the supported path.
- **Refresh after testing.** Rule execution can take a few seconds. Reload the work item if the status change is not visible immediately.
- **Keyword labels need discipline.** Auto-labeling by summary text works when titles follow a convention. Random wording in summaries creates missed tags or false positives.
- **Reopen rules suit reactive work.** Support, operations, and service spaces benefit most from the comment-triggered reopen pattern.

> [!TIP]
> Pair the onboarding label rule with a quick filter or JQL saved filter so HR work appears on a dedicated board without manual triage.

## Review questions

<details>
<summary>What trigger and condition reopen a Done work item when someone comments?</summary>
Trigger: work item commented. Condition: status equals Done. Action: transition work item to Open.
</details>

<details>
<summary>Why use Transition work item instead of Edit work item to change status?</summary>
Workflows define allowed transitions between statuses. The transition action follows those paths; a generic edit may not expose or permit a status change.
</details>

<details>
<summary>Design a rule: auto-label work items about security reviews. What trigger, condition, and action would you use?</summary>
Trigger: work item created (or work item updated if retroactive tagging is needed). Condition: summary or description contains "security review". Action: edit work item to add label <code>security-review</code>.
</details>

<details>
<summary>A Done bug gets a "thanks, fixed!" comment from the reporter. Should the reopen rule fire?</summary>
Yes, with the lesson's design — any comment on a Done work item triggers the reopen. Teams that want to ignore thank-you comments would need an extra condition (for example comment body does not match a pattern), which is more advanced.
</details>

## Related

- [Glossary](../reference/glossary.md)
- [What Can Be Automated in Jira by Non-Admins?](01-what-non-admins-can-automate.md)
- [Using Issue Labels and Priorities to Organize Work in Jira](../04-organizing-work/01-labels-and-priorities.md)
- [When to Ask Admins for Help with Jira Automation](04-when-to-ask-admins.md)

---

Previous: [Smart Checklists: Creating Reusable Checklists in Jira Issues](02-smart-checklists.md) · Next: [When to Ask Admins for Help with Jira Automation](04-when-to-ask-admins.md)
