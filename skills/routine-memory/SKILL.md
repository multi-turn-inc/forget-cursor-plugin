---
name: routine-memory
description: Give a scheduled routine a history so each run continues the last one. Use when creating or editing a routine, and at the start and end of every routine run.
---

# Routines that remember

A routine has a schedule but no memory of its last run. Without a record, every run repeats old searches and reports old news as new.

## When creating a routine

Write these steps into the routine's own instructions, so they run when nobody is in the chat:

1. Start: call `get_task_state` with `task_id` = `routine:<bot-name>:<routine-name>` and read what the last run found and what it said to check next.
2. Work, using the last run to skip what is already done and to notice what changed.
3. End: call `record_task_state` with the same `task_id`, `status` (`completed`, `blocked` or `in_progress`), a one-line `summary` of what this run found, `next_actions` for the next run, and `blockers` if any source was unavailable.

## Rules

- Record a run even when nothing changed. "Checked inbox and calendar, nothing new" is information; silence is not.
- If a source was missing or stale, record that as a blocker instead of reusing old data.
- Keep the summary short and factual; the routine's full output belongs in the conversation, not in memory.
