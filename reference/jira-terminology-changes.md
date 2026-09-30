---
title: "Jira Terminology Changes"
aliases:
  - "Jira Terminology Changes"
  - "Old vs new Jira terms"
type: reference
tags:
  - jira
  - reference
  - topic/terminology
---

# Jira Terminology Changes

[Course home](../README.md) · Related: [Glossary](glossary.md) · Lesson: [Jira Has Changed](../01-introduction/03-jira-has-changed.md)

Atlassian has renamed several core Jira concepts. Older videos, documentation, Marketplace apps, and colleagues still use the old words, so it helps to know both.

## Old term vs current term

| Older term | Current term | Notes |
|---|---|---|
| Jira Software, Jira Work Management | **Jira** | The two products were merged into a single Jira product. |
| Project | **Space** | A space key such as `ABC` still forms work item keys like `ABC-123`. |
| Issue | **Work item** | Epics, stories, tasks, bugs, and subtasks are all work items. |
| Issue type | **Work type** | Epic, Story, Task, Bug, Subtask, or a custom type. |
| Sub-task | **Subtask** | Same concept, new spelling. |
| Project settings | **Space settings** | Where space admins configure the space. |
| Classic project | **Company-managed space** | Configured by Jira admins, and schemes can be shared. |
| Next-gen project | **Team-managed space** | Configured by the space's own admins. |
| Roadmap (inside a space) | **Timeline** | Plans epics and their children over time. |
| Advanced Roadmaps | **Plans** | Cross-team planning in Jira Premium and Enterprise. |
| Epic Link and Parent Link fields | **Parent** field | A single field now expresses every level of the hierarchy. `"Epic Link"` was retired from JQL in February 2024; only filters saved before then still use it. |
| Issue Statistics, Projects, Recently Created Issues (gadgets) | **Work item Statistics**, **Spaces**, **Recently Created Work items** | Dashboard gadget names follow the new terms. |
| Issue created, Issue commented, Issue assigned (automation triggers) | **Work item created**, **Work item commented**, **Work item assigned** | Same triggers, new names. |
| Bulk change | **Bulk change work items** | In the **More actions (⋯)** menu of the search results. |

## Old and new JQL names

JQL is being renamed too. Atlassian's documentation now shows the new names, but says that existing queries don't change and that some new names may not work on every site yet. The old names always work, so the notes and the [JQL cheat sheet](jql-cheat-sheet.md) use them, with this table for translation.

| Old JQL name (works everywhere) | New JQL name |
|---|---|
| `project` | `space` |
| `issuetype` (or `type`) | `workType` (or `type`) |
| `issue`, `issuekey`, `key` | `workItem`, `workItemKey`, `key` |
| `issueLinkType` | `workItemLinkType` |
| `linkedIssues()` | `linkedWorkItems()` |
| `issueHistory()` | `workItemHistory()` |
| `watchedIssues()`, `votedIssues()` | `watchedWorkItems()`, `votedWorkItems()` |
| `standardIssueTypes()`, `subTaskIssueTypes()` | `standardWorkTypes()`, `subtaskWorkTypes()` |
| `projectsLeadByUser()` | `spacesLeadByUser()` |

## Where the old terms still appear

- **JQL**: `project`, `issuetype`, and `issue` (for example `issue in linkedIssues(ABC-1)`) keep working everywhere, next to the new names in the table above.
- **REST APIs and integrations** keep their original names for backward compatibility.
- **Older documentation, community answers, and videos** recorded before the change.
- **Marketplace apps** that have not updated their interface text.

> [!TIP]
> Confluence also uses the word *space*. A Jira space holds work items, while a Confluence space holds pages. They are different things even though they share a name.

## Notes from the course

- **Products**: Jira Software and Jira Work Management are now one product, **Jira**. Jira Service Management (customer requests handled in a queue) stays a separate product, and Jira Product Discovery (ideas and evidence before they become work) is a newer one. **Rovo** is Atlassian's AI assistant and is useful for asking why a setting or action is missing; it comes with the paid plans and their trials, not with the Free plan. See [Jira Has Changed](../01-introduction/03-jira-has-changed.md).
- **Cloud vs Data Center**: The course uses Jira Cloud. Long-lived Data Center installations can look different and lack newer Cloud features, but the concepts still apply. Atlassian stopped selling Data Center to new customers on March 30, 2026, and Data Center reaches end of life on March 28, 2029.
- **The videos use the old words.** Most lessons were recorded before the renames, so they say *project*, *issue*, and *issue type*. The notes in this repo use *space*, *work item*, and *work type*, except in official lesson titles.
- **Old words that remain in the interface**: **Create issue** in the backlog, **Project settings** on some screens, and the Kanban setting **Completed issues**. Gadget names and automation triggers shown with old names in the videos have since been renamed (see the table above).
- **JQL**: The course's queries use `project`, `issuetype`, and `issue`, for example `project = ABC AND issuetype = Story`. They keep working; the new names are listed in the JQL table above. See [JQL Basics](../05-filters-and-jql/03-jql-basics.md).
- **Epic Link to Parent**: The course shows the retired `"Epic Link" = ABC-1` next to the current `parent = ABC-1` and `parentEpic = ABC-1`. New filters must use `parent` (or `parentEpic` in company-managed spaces). See [Link-Based and Hierarchy JQL Queries for Advanced Filtering](../05-filters-and-jql/05-link-and-hierarchy-jql.md).
- **Components**: Space settings may offer *Compass components*, a separate software catalog. The course uses classic Jira components; look for **Switch to Jira components**. See [Structuring Work with Components in Jira Projects](../04-organizing-work/02-components.md).
- **Roadmap to Timeline**: The lesson title still says *Roadmaps*, but the space view is called **Timeline**. It covers one space; planning across spaces uses **Plans** (Premium and Enterprise). See [Roadmaps in Jira](../07-cross-team-collaboration/03-roadmaps-plans-and-dependencies.md).
