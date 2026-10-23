"""Static checks for the Forget Cursor plugin (no network)."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {"turn_context", "search_memories", "search_memory", "get_memory", "get_memories", "list_memories",
           "assemble_context", "prepare_context_autopilot", "get_task_state", "verify_memory_claims",
           "add_memory", "add_memories", "supersede_memory", "confirm_memory", "record_task_state"}


def test_manifest():
    m = json.loads((ROOT / ".cursor-plugin" / "plugin.json").read_text())
    assert re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", m["name"])
    assert (ROOT / m["logo"]).is_file() and m["license"] == "Apache-2.0"
    assert json.loads((ROOT / "mcp.json").read_text())["mcpServers"]["forget"]["url"] == "https://cloud.forget.sh/mcp"


def test_skills_have_frontmatter_and_only_name_allowed_tools():
    for f in list((ROOT / "skills").glob("*/SKILL.md")) + list((ROOT / "rules").glob("*.mdc")):
        t = f.read_text()
        assert t.startswith("---\n") and "\ndescription:" in t.split("---")[1], f
        named = set(re.findall(r"`([a-z_]+)`", t)) & (ALLOWED | {"delete_memory", "update_memory", "delete_all_memories"})
        assert named <= ALLOWED, (f, named - ALLOWED)
