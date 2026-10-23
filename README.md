# Forget for Cursor and Grok Bot

One long-term memory shared by all of your AI tools. Connect Forget once, and every agent you use (Cursor agents, Grok Bot, and your other tools that speak MCP) starts each turn with what you already told the others: decisions, preferences, people, outcomes. Each memory comes with its date and source. When memory has no evidence, the agent is told so and says "not in memory" instead of guessing.

Made by [Multi-turn Inc.](https://www.multi-turn.ai) · [forget.sh](https://forget.sh)

## How it works

The plugin adds one remote MCP server, `https://cloud.forget.sh/mcp`, a rule, and a few skills.

At the start of every turn the agent calls one tool, `turn_context`, with your message and its own previous reply word for word. That single call:

1. **Recalls.** It returns the memories relevant to this turn, newest first where it matters, each labelled green (safe to act on), yellow (confirm first) or red (outdated). With `deep: true` it reads much more of your memory and answers from your original records, with a source on every line.
2. **Remembers.** It saves the exchange to your memory, word for word. The agent never decides what is worth keeping. Forget does that on the server and keeps the original words as the source.

There is no separate "remember this" step for the agent to forget.

## Connect

1. Install the plugin, or add a custom connector with the URL `https://cloud.forget.sh/mcp`.
2. Sign in with GitHub or Google and approve the connection. Reading is always on. Writing is a separate checkbox on the approval screen; without it, nothing is saved.
3. Start a new conversation.

## What the agent can and cannot do

| Can | Cannot |
|---|---|
| Recall (`turn_context`, `search_memories`, `get_memory`, `assemble_context`, ...) | Delete memories |
| Save turns and explicit notes, if you allowed writing | Overwrite memories, change settings, or reach anyone else's memory |
| Supersede or confirm a memory, keeping the original | See your sign-in tokens |

These limits are enforced on the server, not by the skill text.

## Your data

- **Where your memory lives.** In your own memory store on the Forget server in Seoul, South Korea (AWS). One account maps to one store, and no request can name another.
- **What passes through.** The connection server (`cloud.forget.sh`, hosted on Fly.io in the United States) forwards each request to your store. It does not keep request or response bodies. For limits and for your account page it records your account, the connected app, the tool name, and the time.
- **What is saved.** Your messages and the agent's replies sent through `turn_context`, and notes the agent saves when you ask. Before anything is stored, the server removes things that look like passwords, API keys, tokens, card numbers and one-time codes. This is best effort, so avoid pasting secrets.
- **Who else sees it.** Memories returned to an agent reach that agent's model provider, as with any tool result. Deep recall (`deep: true`) also sends the candidate memories for that question to Anthropic's API to write the cited answer.
- **Disconnecting and deleting.** Disconnect any app from your Forget account page. To delete your memory or your account, see the [privacy policy](https://forget.sh/privacy).

Full details: [Privacy Policy](https://forget.sh/privacy) · [Terms](https://forget.sh/terms)

## Price

Forget Cloud is free, with fair-use limits per account.

## Support

hello@forget.sh

## License

Apache-2.0. This repository contains the plugin (manifest, rule, skills, MCP configuration and logo). The Forget server is operated by Multi-turn Inc.
