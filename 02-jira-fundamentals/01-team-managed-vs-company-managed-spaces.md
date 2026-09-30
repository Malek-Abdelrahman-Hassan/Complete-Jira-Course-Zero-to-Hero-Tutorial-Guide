---
title: "Team-Managed vs Company-Managed Spaces"
aliases:
  - "Team-Managed vs Company-Managed Spaces"
type: lesson
section: 2
lesson: 1
duration: "5:15"
status: done
tags:
  - jira
  - section/02
  - topic/spaces
---

# Team-Managed vs Company-Managed Spaces

[Course home](../README.md) › [Section 2: Jira Fundamentals](README.md) › Lesson 1 · 5:15

## TL;DR

When you create your first space in Jira Cloud, it is often **team-managed** by default. **Company-managed** spaces use centrally defined workflows, work types, and fields that can be shared across many spaces. The course uses a company-managed Scrum space because it matches larger organizations and exposes more of Jira's configuration. Both types are valid; the choice is mainly about governance and how much control stays with the team.

## Key concepts

- **Team-managed space**: A space where the team configures its own workflows, work types, fields, and rules. Setup is intuitive and flexible, which suits small teams that want full local control.
- **Company-managed space**: A space that inherits centrally managed configuration. Workflows, work types, and fields can be standardized across the site, which helps consistency in larger organizations.
- **Configuration and governance**: The real difference between the two types is not Agile versus non-Agile, but who owns the configuration and whether settings are shared site-wide.
- **Space key**: A short code (often two to four letters) assigned when the space is created. Every work item (formerly *issue*) in that space starts with this key, for example `SP-1`. It can be changed later, but saved filters, board filters, and dashboard gadgets that use the old key then need updating, so choose it carefully.

## Team-managed vs company-managed

| | Team-managed | Company-managed |
|---|---|---|
| Who configures workflows and fields | The team, inside the space | Site admins; shared across spaces |
| Best fit | Small teams wanting simplicity and local control | Organizations needing consistency |
| Course focus | Referenced for comparison | Primary workspace for demos |

## How to do it in Jira

1. Open **Spaces** in the sidebar. If the menu is collapsed, expand the sidebar first.
2. Select **Create space** (the **+** next to Spaces, or **Create** from the spaces list).
3. Choose a template. The course uses **Scrum**; other templates exist for HR, legal, and similar workflows.
4. Select **Use template**, then pick **Company-managed** when asked (team-managed is the other option).
5. Enter a **name** and a **key**. The key should be short, recognizable, and meaningful, because it appears on every work item and is disruptive to change later.
6. Confirm **Scrum** and **Company-managed**, then create the space.

The lesson creates **Stamps and Points App** with key **SP** as the company-managed practice space and keeps the original default space renamed for later comparison.

## Examples

- A startup team that owns its process end to end might choose a **team-managed** space so members can adjust columns and work types without waiting for a site admin.
- A company with several product teams might use **company-managed** spaces so every team shares the same workflow names, required fields, and work types.
- Key **SP** produces work item keys such as `SP-1`, `SP-2`, and so on. Even if `SP-1` is deleted, the next item is still numbered sequentially.

## Tips and pitfalls

- **Default is often team-managed.** If your first space was created automatically, check its type before following along with the rest of the course.
- **Pick the space key once.** It can be changed under **Space settings > Details** (in company-managed spaces only Jira admins can do it). Old work item links keep redirecting, but every filter and gadget that names the old key must be edited by hand.
- **Both types can coexist.** You may keep a team-managed sandbox alongside a company-managed main space; menus and options will differ slightly between them.
- **Type cannot be switched in place.** Jira has no convert button. To change type, create a new space of the other type and bulk-move the work items into it, which renumbers their keys. Plan the choice before creating the space.

> [!NOTE]
> The course demos use a company-managed space not because it is always better, but because it reflects setups common in larger organizations and allows deeper exploration of shared configuration.

## Review questions

<details>
<summary>What is the main difference between team-managed and company-managed spaces?</summary>
Configuration and governance. Team-managed spaces let the team control local settings. Company-managed spaces use centrally managed configuration that can be shared across multiple spaces for consistency.
</details>

<details>
<summary>Why does the course recommend a company-managed space?</summary>
It exposes more of Jira's shared configuration and matches the kind of setup common in larger organizations, even though team-managed spaces are fine for many teams.
</details>

<details>
<summary>What is a space key used for?</summary>
It is a short code prefixed to every work item in that space, such as SP in SP-12. It helps identify where work belongs and is used in search and JQL.
</details>

<details>
<summary>What happens if you change a space key after creation?</summary>
Jira renames the work item keys and keeps redirecting links that use the old key, but saved filters, board filters, and dashboard gadgets that name the old key stop matching until someone edits them. That extra work is why the key should be chosen carefully at the start.
</details>

## Related

- [Glossary](../reference/glossary.md)
- [Jira Terminology Changes](../reference/jira-terminology-changes.md)
- [Set Up Your Free Jira Cloud Site (Optional Hands-On Setup)](../01-introduction/04-set-up-free-jira-cloud-site.md)
- [How Jira Is Structured: Spaces, Boards & Work Items](06-how-jira-is-structured.md)

---

Previous: [Section overview](README.md) · Next: [Understanding Jira Work Types & Hierarchy](02-work-types-and-hierarchy.md)
