---
name: memory-reflect
description: Answer questions about the user's past, history, habits or earlier decisions from memory, with sources. Use when the user asks "what did I decide", "when did we", "why did we", "do you remember", or anything whose answer lives in past conversations or work done in other tools.
---

# Answer from memory, with sources

## Steps

1. Turn the question into a short query ("why we moved off vendor A").
2. Call `search_memories` with `recall` set to `"extra"` and `top_k` 8.
3. Read `sufficiency` first:
   - `full`: answer from the cited lines and name the source dates.
   - `partial`: answer what the sources support and say what is missing.
   - `none`: say it is not in memory. Offer to look it up or ask the user. Do not answer from general knowledge as if it were memory.
   - missing, with a `fallback_reason`: deep recall did not run. Answer from the plain results if they clearly cover it; otherwise say memory could not be checked fully right now.
4. Quote or paraphrase only what the cited lines say. Keep each claim tied to its `[S#]`, and keep the source date when the user will act on it.
5. If you need to check a specific claim you are about to make, `verify_memory_claims` with `claims` (a list of short sentences) reports which ones memory supports.

## Rules

- A citation means the line came from a stored record, not that the record is still true. If the user is about to act on it, mention how old it is.
- If two records disagree, show both with dates and say which is newer.
