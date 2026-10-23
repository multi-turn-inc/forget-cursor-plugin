---
name: memory-setup
description: Connect this Bot to Forget and check that its memory works. Use once when Forget is first added, when a memory call fails with an authorization error, or when the user asks whether memory is connected.
---

# Connect Forget

Forget is the user's own long-term memory, shared by every AI tool they connect to it (Claude Code, Codex, other Bots). It keeps what was said word for word, with the date and source, and it says "not in memory" when it has no evidence.

## Steps

1. Make sure the agent has a real name. The name is written on everything this Bot remembers (`agent_id` = `grok-bot:<bot-name-in-lowercase-with-dashes>`), so a Bot still called "Grok Bot" should ask the user for a name first.
2. If the Forget connector is not installed, ask the user to add a custom connector with the URL `https://cloud.forget.sh/mcp`, sign in with GitHub or Google, and approve the connection. Tell them they can choose read-only on the approval screen.
3. Check the connection with one small read: `search_memories` with a short query about the user (for example "user's current projects") and `top_k` 3.
   - If it answers, say in one line that memory is connected and what kind of things it already knows.
   - If it fails with an authorization error, ask the user to reconnect Forget from Connect apps. Do not guess other addresses.
4. If writing is allowed, save one note that this agent exists: `add_memory` with `text` "<Bot name> is a Grok Bot that <its job in one line>.", `agent_id` from step 1, and `infer` false.

## Rules

- Never paste tokens or keys into chat or memory.
- If `add_memory` returns a permission error, the user connected read-only. Respect it: keep working from memory without writing, and say once that new things will not be remembered.
- Deleting, overwriting and changing memory settings are not available to Bots. If something should be removed, tell the user to do it in Forget.
