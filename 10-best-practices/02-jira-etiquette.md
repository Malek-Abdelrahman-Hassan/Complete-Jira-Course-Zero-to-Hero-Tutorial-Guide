---
title: "Jira Etiquette: Do's and Don'ts for Real Teams"
aliases:
  - "Jira Etiquette: Do's and Don'ts for Real Teams"
type: lesson
section: 10
lesson: 2
duration: "6:53"
status: done
tags:
  - jira
  - section/10
  - topic/best-practices
---

# Jira Etiquette: Do's and Don'ts for Real Teams

[Course home](../README.md) › [Section 10: Best Practices and Final Challenge](README.md) › Lesson 2 · 6:53

## TL;DR

Jira works best when every work item (formerly *issue*) tells a clear story: a short summary on the card, enough detail inside, and statuses that reflect reality. Keep discussion on the work item with comments and @mentions, update only your own work, and treat labels and components consistently. Watchers and notification schemes control who gets pinged — agree as a team so alerts stay useful, not noisy.

## Key concepts

- **Summary**: The one-line title on a board card. It should be short and informative, not a full user-story template.
- **Description**: The place for context — value to the user, acceptance criteria, links, and checklists. Detail lives here, not in the summary.
- **Definition of Done (DoD)**: A checklist of conditions that must be true before work is complete. Teams often track it with a smart checklist or a bullet list in the description.
- **History**: An audit log on each work item showing who changed which fields and when. Useful when you inherit unfamiliar work.
- **Watcher**: A person subscribed to updates on a work item. Anyone can add watchers; each watcher can stop watching on their own.
- **Notification scheme**: A space-level setting (admin-only) that defines which events email which roles. Complements personal watcher choices.

## Do's and don'ts

| Do | Don't |
|---|---|
| Write short, clear summaries everyone can scan on the board | Paste the full "As a user, I want…" story format into the summary |
| Put acceptance criteria, value, and DoD in the description or a checklist | Leave the description empty while expecting others to guess scope |
| Ask questions in **Comments** with @mentions so the thread stays on the work item | Move status or assignee on someone else's work without agreement |
| Check **History** when you take over unfamiliar work | Assume the current assignee made every past change |
| Select existing labels from the autocomplete list | Type a new label when a typo will fork the team into duplicate tags |
| Use components and fix versions the way your team agreed | Invent parallel tagging systems that ignore shared fields |
| Discuss notification noise as a team; use **Watch** thoughtfully | Force colleagues to stay watchers when they no longer need updates |

## How to do it in Jira

### Write useful summaries and descriptions

1. On create or edit, keep **Summary** to one actionable line (for example *Password reset email*).
2. Open **Description** and add why the work matters, acceptance criteria, and any links.
3. Add a DoD checklist — use a smart checklist if your space has one, or insert action-item boxes / bullet lists in the description editor.

### Ask questions without losing context

1. Open the work item and scroll to **Comments**.
2. Type `@` followed by a name to mention a teammate.
3. Post the question. The mention sends a notification; replies stay on the same work item for anyone who picks it up later.

### Investigate changes

1. Open the work item and select **History** (or **Activity** > **History**, depending on layout).
2. Scan field changes, who made them, and when.
3. Follow up in comments if something still is unclear.

### Manage labels carefully

1. Click **Labels** and start typing.
2. Pick an existing label from the dropdown instead of pressing Enter on a near-duplicate spelling.
3. If the team needs a new label, agree on the exact spelling before the first use.

### Review notifications and watchers

1. On a work item, open **Watch** to see who is watching; add or remove watchers as needed.
2. For space-wide rules, go to **Space settings** > **Notifications** (wording may vary) and open the **Notification scheme** link to see who gets emailed for which events.
3. Ask a space admin to adjust the scheme only after the team agrees on desired behavior.

## Examples

On *Stamps and Points*, story `ABC-42` has summary *Social login via Google* and description notes: customer value, three acceptance criteria, and a DoD checklist (unit tests, QA sign-off, docs updated). A new developer mentions the PO in a comment instead of reassigning the story silently.

Two teammates accidentally create `wishlist` and `whishlist` labels. Filtering by label now misses half the ideas — the team deletes the typo label and re-tags work items after agreeing on one spelling.

## Tips and pitfalls

- **Jira is a collaboration hub, not a checkbox for managers.** Rich descriptions and honest statuses help the whole team, not just reporting.
- **Accountability beats proxy updates.** Changing work on behalf of others hides who is actually responsible.

> [!IMPORTANT]
> Labels are created site-wide the first time someone confirms a new name. Typos persist because Jira does not merge near-duplicates automatically.

## Review questions

<details>
<summary>Where should acceptance criteria live — summary or description?</summary>
In the description (or a linked checklist), not in the summary. The summary stays short for board scanning.
</details>

<details>
<summary>Why mention someone in a comment instead of emailing them?</summary>
The conversation stays on the work item, notifications still go out, and anyone who takes over later sees the full thread.
</details>

<details>
<summary>What is the risk of typing a label name instead of selecting it from the list?</summary>
A typo creates a second label that looks almost the same, splitting filters and reports.
</details>

<details>
<summary>Who can change a space notification scheme?</summary>
A Jira or space admin. Individual users control their own watch settings on each work item.
</details>

<details>
<summary>When is the History tab most useful?</summary>
When you inherit a work item mid-flight and need to see what changed, by whom, before you continue the work.
</details>

## Related

- [Glossary](../reference/glossary.md)
- [Using Issue Labels and Priorities to Organize Work in Jira](../04-organizing-work/01-labels-and-priorities.md)
- [Smart Checklists: Creating Reusable Checklists in Jira Issues](../09-automation/02-smart-checklists.md)
- [Structuring Work with Components in Jira Projects](../04-organizing-work/02-components.md)

---

Previous: [Pro Tips, Shortcuts, and Smart Habits for Jira Power Users](01-pro-tips-and-shortcuts.md) · Next: [Where's My Issue? Troubleshooting Visibility Problems in Jira](03-wheres-my-issue-troubleshooting.md)
