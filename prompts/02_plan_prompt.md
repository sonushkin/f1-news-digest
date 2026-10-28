# Stage 2 Prompt: Source Review and Project Plan

## Context

Stage 1 defined **F1 News Digest**, a beginner-friendly Python console program
that reads a public Formula 1 RSS or Atom feed, filters and limits the items,
and records locally which items have already been seen. The project must follow
the GSOM AI Intro workflow and create genuine Git history.

## Action

1. Verify one real Formula 1 feed and record its URL, publisher, format,
   availability evidence, attribution requirements, and usage limitations.
2. Design a minimal project structure for one Python script, local test
   fixtures, runtime history, prompts, and reports.
3. Prefer the Python standard library and identify the modules expected for
   networking, XML parsing, JSON persistence, and command-line arguments.
4. Prepare a `.gitignore` that excludes runtime history, temporary files,
   Python caches, virtual environments, secrets, and editor files.
5. Propose the commands for initializing Git and creating one genuine scaffold
   commit. Do not execute them for the learner.
6. Do not implement the news application yet.

## Tone and format

Use concise beginner-friendly English. Clearly distinguish verified facts,
design decisions, and work reserved for later stages.

## Anticipate edge cases

- Do not invent a feed or claim that a live network resource is permanent.
- Do not commit downloaded feed content or local reading history.
- Do not present BBC feed descriptions as original or AI-generated text.
- Do not use BBC logos or imply BBC endorsement.
- Keep the project non-commercial and credit BBC Sport prominently in the
  eventual console output and README.
- Do not add dependencies before they are justified.
- Do not fabricate Git commits or execute Git on the learner's behalf.

## Checkpoint

Stage 2 is complete only after the source review and scaffold exist, the
learner has run the proposed Git commands, and the exact `git status` and
`git log --oneline` output confirm a real scaffold commit.

