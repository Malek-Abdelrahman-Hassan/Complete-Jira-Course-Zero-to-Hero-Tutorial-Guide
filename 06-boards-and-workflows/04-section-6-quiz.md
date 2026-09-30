---
title: "Section 6 Quiz"
aliases:
  - "Section 6 Quiz"
type: quiz
section: 6
lesson: 4
duration: ""
status: done
tags:
  - jira
  - section/06
  - quiz
  - flashcards
---

# Section 6 Quiz

[Course home](../README.md) › [Section 6: Projects, Boards, Workflows, and Statuses](README.md) › Quiz

> [!IMPORTANT]
> The official Udemy quiz questions are not reproduced here. The practice questions and flashcards below are original and cover the same topics.

## Topics covered

- [Customizing Your Jira Board View Without Admin Access](01-customizing-board-view.md)
- [Workflow States and Transitions: What You Can See and Do](02-workflow-states-and-transitions.md)
- [Navigating Complex Workflows Without Getting Lost in Jira](03-navigating-complex-workflows.md)

## Practice questions

<details>
<summary>1. A teammate moves a story to Testing on the Stamps and Points board, and the card vanishes from both Active sprints and Backlog. What is the most likely cause?</summary>
Testing is an unmapped status—no board column includes it. Map Testing to a column in Board settings > Layout > Columns so work items in that status appear again.
</details>

<details>
<summary>2. You need to add WIP limits and map a new QA status to columns, but you are not a Jira site admin. Can you still do this?</summary>
Yes, if you are a board administrator for that board. Board settings cover columns, WIP limits, swimlanes, and card layout without site admin rights.
</details>

<details>
<summary>3. On a Kanban board, released-version work keeps cluttering Done. Which setting should you review first?</summary>
The sub-filter on the board—often a JQL clause that hides work tied to released versions. Adjust or restore it under Board settings > General settings.
</details>

<details>
<summary>4. A work item sits in In Progress, but the status dropdown does not offer Testing even though Testing exists on the workflow diagram. Why?</summary>
No transition from In Progress to Testing is defined, or a condition, validator, or permission blocks that transition. View workflow from the work item to see allowed outgoing moves.
</details>

<details>
<summary>5. What is the difference between moving a card to Done and setting resolution Won't Do?</summary>
Done is a status in the Done category—the work item reached a finished column. Won't Do is a resolution value explaining why it closed without being completed. Both can apply to the same item after a resolve transition.
</details>

<details>
<summary>6. An epic progress bar counts story points. A story is in custom status Legal review. Which status category should Legal review use so the bar reflects active work?</summary>
In Progress. Status category—not the custom label—drives how Jira treats work for progress and many reports.
</details>

<details>
<summary>7. After QA finds bugs, the team wants work to return to development without looking like a brand-new backlog item. Which status design fits?</summary>
A dedicated Reopened status in the In Progress category, with a transition from In QA to Reopened and Start progress from Reopened back to In progress.
</details>

<details>
<summary>8. A global any transition lets every status jump straight to Done. What is one benefit and one drawback?</summary>
Benefit: teams can close emergencies quickly from any step. Drawback: it bypasses review and QA gates, weakening process discipline if used routinely.
</details>

<details>
<summary>9. You transition a bug to Done and pick resolution Cannot reproduce on the resolve screen. Can you change that resolution later?</summary>
Generally no. Resolution is stored permanently once set. Avoid casual resolution choices; ask an administrator if a correction is truly needed.
</details>

<details>
<summary>10. Card layout was updated on the Scrum board, but active sprint cards still lack Days in column. What did you miss?</summary>
Card layout is configured separately for Backlog and Active sprints on Scrum boards. Enable Days in column under both views in Board settings > Layout > Card layout.
</details>

<details>
<summary>11. An administrator publishes a new workflow through a workflow scheme. When do existing work items in that space start following the new transitions?</summary>
After the workflow scheme change is published. Until publish completes, items keep the previous workflow paths.
</details>

<details>
<summary>12. A column header turns red after a fourth card is dragged into In Progress, but Jira still accepts the move. What is happening?</summary>
The column WIP max was exceeded. Jira highlights the overload as a signal; it does not hard-block the transition unless separate workflow rules do.
</details>

## Flashcards

What is an unmapped status?::A workflow status not assigned to any board column, causing work items in that status to disappear from the board and Scrum backlog
Who can open Board settings?::Board administrators for that board, without requiring Jira site admin rights
What does a board filter define?::Which work items appear on the board, often via saved JQL that can include one or more spaces
What is a Kanban sub-filter?::An extra JQL clause—commonly hiding released-version work—that further narrows items on a Kanban board
What does Days in column show?::How many days a work item has been in its current status, often as dots on the card
What are the three status categories?::To Do, In Progress, and Done
What is a transition?::A named allowed move from one workflow status to another
What is a resolution?::A value recorded when work reaches a Done-category status, explaining why it closed
What does a global any transition do?::Allows a move to a target status from every other status in the workflow
What is a transition screen?::A form shown during a transition, often to pick resolution or required fields
What is a workflow scheme?::Configuration that links workflows to spaces and work types; changes apply after publish
What is an orphan status in the workflow editor?::A status with no incoming transitions until one is created
Why use a Reopened status?::To show work returned after QA or review rather than treating it like brand-new To Do work
What is a post function?::An action Jira runs after a successful transition, such as updating status or sending notifications
What is a condition on a transition?::A rule that must be true before the transition is offered to a user
Can regular users edit workflows?::No; they can view the workflow diagram and use transitions, but editing requires Jira admin access
What drives epic progress bars by category?::Status category (To Do, In Progress, Done), not the custom status name alone
What happens when WIP max is exceeded?::The column header turns red as a warning; Jira may still allow the move
Why might Timeline be missing in board settings?::Timeline typically requires a single-space filter; multi-space boards may not support it
What should you check first when a work item disappears after a status change?::Unmapped statuses in Board settings > Layout > Columns

## Easy to confuse

| Concept A | Concept B | How to tell them apart |
|---|---|---|
| Status | Transition | Status is where the work item is (In QA). Transition is the named move that gets it there (Start QA). |
| Status Done | Resolution Done | Done status means the item reached a finished workflow step. Done resolution means it was successfully completed—not deferred or duplicate. |
| Status category | Status name | Category is To Do, In Progress, or Done for reporting. Name is the label on the work item (Testing, In review, Legal review). |
| Board administrator | Jira site administrator | Board admins configure one board's columns, cards, and filters. Site admins create and edit workflows and workflow schemes. |
| Board filter | Kanban sub-filter | The board filter selects all candidate work items. The sub-filter is an additional JQL slice applied only on Kanban boards. |
| Unmapped status | Blocked transition | Unmapped hides items from the board entirely. Blocked transition means the workflow or permissions disallow a specific move from the current status. |

---

Previous: [Navigating Complex Workflows Without Getting Lost in Jira](03-navigating-complex-workflows.md) · Next: [Section 7: Cross-Team Collaboration](../07-cross-team-collaboration/README.md)
