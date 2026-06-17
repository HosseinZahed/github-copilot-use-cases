## GitHub Copilot CLI Slash Commands Quick Reference

### Commands
- `/new` — Start new conversation
- `/compact` — Summarize to free context
- `/exit`, `/quit` — Exit CLI
- `/agent` — Browse and select agents
- `/model` — Select AI model
- `/plan` — Create implementation plan
- `/delegate` — Offload to cloud agent
- `/review` — Run code review agent
- `/context` — Context window usage
- `/instructions` — Toggle instruction files
- `/ide` — Connect to VS Code

### Shortcuts
- `@filename` — Include file in context
- `Shift+Tab` — Cycle modes
- `Ctrl+Y` — View/edit plan
- `Ctrl+T` — Toggle reasoning
- `!command` — Jump to shell mode

### Session Management
- `/session` — Show current session info
- `/session checkpoints` — List compaction checkpoints
- `/session plan` — View implementation plan
- `/rename` — Rename the current session
- `/share file ./notes.md` — Export session to Markdown
- `/compact` — Manually trigger context compaction
- `copilot --resume` / `copilot --continue` / `copilot --resume ID` — Resume previous sessions