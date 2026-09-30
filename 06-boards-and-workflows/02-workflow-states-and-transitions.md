---
title: "Workflow States and Transitions: What You Can See and Do"
aliases:
  - "Workflow States and Transitions: What You Can See and Do"
type: lesson
section: 6
lesson: 2
duration: "8:06"
status: done
tags:
  - jira
  - section/06
  - topic/workflows
---

# Workflow States and Transitions: What You Can See and Do

[Course home](../README.md) › [Section 6: Projects, Boards, Workflows, and Statuses](README.md) › Lesson 2 · 8:06

## TL;DR

A **workflow** defines the statuses a work item (formerly *issue*) can be in and the **transitions** that move it between them. You change status by dragging cards on a board or picking a status on the work item. When transitions are confusing, open **View workflow** from the status menu to see the full diagram. Regular users can explore workflows but not edit them—that requires a Jira administrator. Every status belongs to a **status category** (To Do, In Progress, or Done), and completed work also gets a **resolution** explaining why it stopped.

## Key concepts

- **Workflow**: The rules that govern which statuses exist for a work type and which moves between them are allowed.
- **Status**: A step in the workflow where a work item currently sits—for example **Open**, **In Progress**, or **Testing**.
- **Transition**: A named move from one status to another—for example the **Prioritize** transition from **Open** to **To Do**. The name shown to users may differ from the destination status.
- **Status category**: A grouping Jira uses for reporting and progress bars: **To Do** (work not started), **In Progress** (work underway), and **Done** (work finished). Custom statuses still map to one of these three categories.
- **Resolution**: A value recorded when work reaches a Done-category status, explaining *why* it closed—for example **Done**, **Won't Do**, or **Duplicate**.
- **Global transition ("any")**: A transition that allows a move from any status to a target status. Convenient for edge cases but can bypass process discipline if overused.
- **Workflow viewer**: A read-only diagram opened from a work item's status menu, showing all statuses and transitions for that item's workflow.

## Status categories at a glance

| Category | Typical color on diagrams | Meaning | Examples |
|---|---|---|---|
| To Do | Gray | Work has not started | Open, To Do, Backlog |
| In Progress | Blue | Work is actively being done | In Progress, Testing, Design, Legal review |
| Done | Green | Work has stopped | Done, Closed |

## How to do it in Jira

### Change status as a regular user

1. **On a board** — drag a card from one column to another. Each column maps to one or more statuses; the drag performs the underlying transition.
2. **On the work item** — open the work item, click the **Status** field, and pick an available destination. Only transitions you are permitted to use appear in the list.

### Inspect a workflow you cannot edit

1. Open a work item and click **Status**.
2. Choose **View workflow** (wording may vary slightly by Jira version).
3. Read the diagram: circles or nodes are statuses; arrows are transitions. Labels on arrows are transition names; a box marked **any** means a global transition from every status.
4. If a status you expect is missing from the dropdown, the diagram shows whether no transition exists from the current status or a condition blocks the move.

### Understand resolutions on completed work

1. Move a work item to a Done-category status (for example **Done**).
2. Jira prompts for a **Resolution** when the workflow requires one. Simple workflows may offer only **Done**; richer setups add **Won't Fix**, **Duplicate**, and similar values.
3. After resolution is set, it typically cannot be changed—treat it as a permanent record of why the item closed.

### Who can change workflows

- **Jira administrator** — creates and edits workflows, often under **Settings** (gear) > **Work items** > **Workflows** (exact path can vary).
- **Regular user / board admin** — uses transitions and views the workflow diagram; cannot redesign the workflow itself.
- **Company-managed spaces** — workflows are usually shared across multiple spaces and maintained centrally. Request changes through an admin rather than expecting per-team edits.

## Examples

On the *Stamps and Points* demo workflow, dragging a story from **To Do** to **In Progress** to **Testing** to **Done** performs one transition at each step. The same moves can be done from the work item's status dropdown.

The workflow includes a **Prioritize** transition from **Open** to **To Do**, used when grooming the Kanban backlog: newly created items land in **Open**, then **Prioritize** moves them to **To Do** where they appear on the board backlog.

Several global **any** transitions allow jumping to **Open**, **To Do**, **In Progress**, **Testing**, or **Done** from any status. That flexibility helps emergencies but makes it easy to skip steps—many teams prefer fewer, deliberate transitions.

When an epic's progress bar counts story points, only items in **In Progress** and **Done** categories contribute according to their status category—not the custom status name alone.

## Tips and pitfalls

- **Dropdown ≠ full workflow.** The status picker shows only transitions available *right now* from the current status, not every status in the workflow.
- **Categories drive metrics.** Reports, epic progress, and burndowns rely on status categories. A custom **QA** status should be **In Progress**, not **Done**, while work is still active.
- **Resolution explains closure.** **Done** the status means work reached a finished column; **Done** the resolution means it was completed successfully. Other resolutions close work without finishing it.
- **Shared workflows need coordination.** Changing a company-managed workflow affects every space that uses it—plan with an admin before requesting new statuses.

> [!NOTE]
> Workflows can also attach **conditions**, **validators**, **triggers**, and **post functions** to transitions. Those advanced pieces are covered in the next lesson; for daily work, knowing which transitions exist is enough to start.

## Review questions

<details>
<summary>What is the difference between a status and a transition?</summary>
A status is where the work item is now (for example In Progress). A transition is the allowed move between statuses (for example Start Progress from To Do to In Progress). Transition names and destination statuses are not always the same word.
</details>

<details>
<summary>What are the three status categories, and what does each represent?</summary>
To Do (work not started), In Progress (work underway), and Done (work finished). Every status—custom or built-in—maps to one category for reporting.
</details>

<details>
<summary>Why might a status appear on the workflow diagram but not in the work item's status dropdown?</summary>
No transition exists from the current status to that destination, or a condition, validator, or permission blocks that transition for you or for this work item.
</details>

<details>
<summary>What is a resolution, and when is it set?</summary>
Resolution records why work in a Done-category status stopped—for example completed (Done), deferred (Won't Do), or removed as a duplicate. It is set when transitioning to a finished status, often through a prompt or transition screen.
</details>

<details>
<summary>Can a regular board administrator edit the workflow diagram?</summary>
No. Viewing the workflow is available from the work item; editing the workflow requires Jira administrator access (or equivalent workflow permissions on the site).
</details>

## Related

- [Glossary](../reference/glossary.md)
- [Customizing Your Jira Board View Without Admin Access](01-customizing-board-view.md)
- [Navigating Complex Workflows Without Getting Lost in Jira](03-navigating-complex-workflows.md)
- [Create Work Items: Epics, Stories & Subtasks](../02-jira-fundamentals/03-create-epics-stories-subtasks.md)

---

Previous: [Customizing Your Jira Board View Without Admin Access](01-customizing-board-view.md) · Next: [Navigating Complex Workflows Without Getting Lost in Jira](03-navigating-complex-workflows.md)
