---
title: "Final Challenge: Apply What You've Learned in Jira"
aliases:
  - "Final Challenge: Apply What You've Learned in Jira"
type: lesson
section: 10
lesson: 4
duration: "3:47"
status: done
tags:
  - jira
  - section/10
  - topic/final-challenge
---

# Final Challenge: Apply What You've Learned in Jira

[Course home](../README.md) › [Section 10: Best Practices and Final Challenge](README.md) › Lesson 4 · 3:47

## TL;DR

The final challenge is a full lap through Jira on your own site: create a company-managed Scrum space, wire up a board filter that can span more than one space, populate it with varied work types and organizing fields, and add quick filters plus dashboards that match how you would run a real team. Pick any theme — a startup idea, an event, or a travel plan — and treat it as production practice, not a demo.

## Key concepts

- **Sandbox space**: A practice space where you can safely repeat the course workflow end to end without affecting a shared company site.
- **Company-managed space**: Recommended for the challenge because it exposes the full set of configuration options the course uses (workflows, components, cross-space boards). Team-managed spaces are worth comparing separately.
- **Cross-space board**: A board whose filter JQL can include work items from more than one space key, useful when one team tracks related work across spaces.
- **Quick filter**: A saved JQL toggle on the board — for example "assigned to Alex" or "open longer than five days".

## Challenge brief

Work through these steps on a free Jira Cloud site or another sandbox you control:

1. **Create a space** — Use **Create** > **Space** (or the **+** menu). Choose **Scrum** with the **Basic** template and **Company-managed** (team-managed is optional for comparison).
2. **Name the space** — Pick a theme from the examples below or your own idea.
3. **Configure the board filter** — Create or edit the board's saved filter so it can include more than one space if you create a second space later (for example `project in (KEY1, KEY2)`).
4. **Add varied work items** — Create epics, stories, tasks, and bugs. Attach **Components** and **Fix versions**. Set **Priority**, **Labels**, and backlog order so the board reads clearly at a glance.
5. **Add quick filters** — At minimum, one filter by assignee (or "unassigned") and one for stale work (for example created or updated more than five days ago and still open).
6. **Run the board** — Move cards through statuses, plan a sprint if using Scrum, and open reports or a personal dashboard gadget to watch progress.
7. **Keep using it** — Extend the space after the challenge finishes so skills stay current.

## Example project ideas

### Cupcake delivery startup

Structure a fictional bakery delivery business from scratch.

| Epic (suggested) | Sample stories / tasks |
|---|---|
| Brand and menu | Logo brief, flavor lineup, pricing sheet |
| Kitchen operations | Supplier setup, oven capacity plan, food-safety checklist |
| Ordering app | Customer menu page, checkout flow, order notifications |
| Delivery logistics | Driver zones, route tracking, proof-of-delivery |

### Film or game night with friends

Plan a social event as if you were the organizer.

| Epic (suggested) | Sample stories / tasks |
|---|---|
| Pick the activity | Poll friends, choose film or game, set date |
| Venue and gear | Reserve room, test projector or console, seating plan |
| Food and drinks | Snack shopping list, dietary preferences, cleanup rota |
| Invitations | Create guest list, send invites, collect RSVPs |

Sample subtasks under *Snack shopping list*: buy popcorn, buy drinks, prepare serving table.

### World tour planner

Even as a thought exercise, plan travel to five dream destinations — one epic per destination — plus cross-cutting epics.

| Epic (suggested) | Sample stories / tasks |
|---|---|
| Destination: Tokyo | Flights research, hotel shortlist, must-see list |
| Destination: Lisbon | Flights research, hotel shortlist, must-see list |
| Destination: Cape Town | Flights research, hotel shortlist, must-see list |
| Destination: Buenos Aires | Flights research, hotel shortlist, must-see list |
| Destination: Reykjavik | Flights research, hotel shortlist, must-see list |
| Paperwork and prep | Passport renewal, travel insurance, budget tracker |
| Getting the most from each trip | Local guides, language basics, packing checklist |

## How to do it in Jira

1. From the Jira home page, open **Create** > **Space** (or **+** > **Space**).
2. Select **Scrum**, **Basic** template, and **Company-managed**.
3. After creation, open **Space settings** > **Board** (or the board itself) and note the filter JQL.
4. Create epics first, then stories and tasks under them; add bugs where realistic.
5. Define at least two **Components** and one **Fix version**; assign them to work items.
6. Open **Board settings** > **Quick filters** and add assignee-based and age-based filters (JQL examples below).
7. Optional: build a personal dashboard with a filter gadget pointed at your challenge filter.

## Examples

Quick filter for work assigned to one teammate:

```sql
project = ABC AND assignee = currentUser()
```

Quick filter for items open more than five days (adjust the function name if your site uses a different JQL helper):

```sql
project = ABC AND status != Done AND updated <= -5d
```

Board filter spanning two practice spaces:

```sql
project in (ABC, XYZ) ORDER BY Rank ASC
```

## Tips and pitfalls

- **Prefer Scrum + company-managed for the first run.** Some lightweight templates hide configuration the course relies on; you can explore team-managed afterward.
- **Make the board readable before adding volume.** Components, versions, and labels only help when applied consistently from the start.

> [!TIP]
> Reusing Jira for a personal project — chores, learning goals, or a hobby — keeps daily habits alive between formal practice sessions.

## Review questions

<details>
<summary>Why does the course recommend a company-managed Scrum space for the challenge?</summary>
It exposes the full configuration surface — workflows, components, cross-space filters — that most course lessons assume.
</details>

<details>
<summary>What is one quick filter that helps surface stale work?</summary>
A JQL quick filter that finds open work items not updated in several days, for example combining status != Done with updated <= -5d.
</details>

<details>
<summary>What work types should the challenge include at minimum?</summary>
Epics, stories, tasks, and bugs, plus components and fix versions for organization.
</details>

<details>
<summary>How can a board show work from more than one space?</summary>
Point the board filter JQL at multiple space keys, for example project in (KEY1, KEY2).
</details>

## Related

- [Glossary](../reference/glossary.md)
- [Set Up Your Free Jira Cloud Site (Optional Hands-On Setup)](../01-introduction/04-set-up-free-jira-cloud-site.md)
- [Create Work Items: Epics, Stories & Subtasks](../02-jira-fundamentals/03-create-epics-stories-subtasks.md)
- [Creating and Saving Filters in Jira for Quick Access](../05-filters-and-jql/02-creating-and-saving-filters.md)
- [Structuring Work with Components in Jira Projects](../04-organizing-work/02-components.md)
- [Planning and Releasing with Versions in Jira](../04-organizing-work/03-versions-and-releases.md)

---

Previous: [Where's My Issue? Troubleshooting Visibility Problems in Jira](03-wheres-my-issue-troubleshooting.md) · Next: [What's Next on Your Jira Journey: Advanced Skills and Resources](05-whats-next.md)
