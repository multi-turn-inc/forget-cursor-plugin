---
name: memory-retain
description: Saving happens through turn_context at the start of each turn. Use this skill only when the person explicitly asks you to remember something right now, or corrects a memory.
---

# Saving is automatic

Every `turn_context` call already saves the exchange (your previous reply and the person's new message, word for word). Forget's server decides what lasts. You do not choose.

## Only when asked explicitly

- "Remember that ..." or "save this": call `add_memory` with `messages` = `[{"role": "user", "content": "<their words>"}]`, `infer` `true`, and `source_role` `user`.
- A correction to something memory said: the correction is already in the turn you send; if the person points at a specific memory id, call `supersede_memory` with that id and the corrected text.

## Rules

- Never rewrite a plan as if it were done. If you only drafted something, your reply already says so.
- Deleting is not available to you. If something should be removed, tell the person and they will do it in Forget.
- Forget removes passwords, keys, card numbers and one-time codes on the server, but do not paste them into replies in the first place.
