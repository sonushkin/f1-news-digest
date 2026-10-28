# Mini-Project 2: Programming Workspace

This workspace contains an OpenCode agent team for completing the programming
mini-project according to the GSOM AI Intro course workflow.

## Agent team

- `programming-project-manager` - primary stage coordinator;
- `python-tutor` - beginner-friendly concepts and algorithms;
- `function-writer` - Python console script drafts and assertions;
- `debugger` - traceback analysis and minimal fix proposals;
- `doc-writer` - README and verified documentation.

The current OpenCode format stores project agents in `.opencode/agents/` and
project commands in `.opencode/commands/`.

## Start

Open a terminal in this folder and run:

```bash
opencode
```

Select the **programming-project-manager** primary agent with Tab, or enter:

```text
/mini-project-2 stage=1
```

Stage 1 chooses and scopes the everyday task. No application code should be
created before that checkpoint is accepted.

The specialist agents follow Topic 6: they draft but do not run code. You run
the proposed `python3 ...` or Git command in the terminal and return the exact
output for verification.

After editing agent files, restart OpenCode so the course environment reloads
the configuration.

