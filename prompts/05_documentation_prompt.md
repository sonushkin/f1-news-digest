# Stage 5 Prompt: README Documentation

## Context

F1 News Digest has a verified console workflow, five passing local tests, and
three genuine Git commits. It reads the BBC Sport Formula 1 RSS feed, supports
a positive limit and optional keyword, and tracks `NEW`/`SEEN` identifiers in
an ignored local JSON file. No reproducible defect was found during Stage 4.

## Action

Replace the workspace README with a submission-quality README that explains:

1. what the application does and why it is useful;
2. source attribution and the non-commercial academic usage boundary;
3. Python requirements and dependencies;
4. exact commands for default, limited, filtered, help, invalid-input, and test
   runs;
5. the output format without copying live articles into the repository;
6. local history behavior and Git exclusion;
7. project structure, tested behavior, limitations, and AI use.

Use only verified behavior. Do not change application code, make a commit, or
publish the repository.

## Tone and format

Write clear academic English for a beginner. Use short sections, exact commands,
and honest limitations. Keep live feed descriptions distinct from AI output.

## Anticipate edge cases

- Live headlines change, so do not promise particular current stories.
- Do not state that descriptions are AI-generated summaries.
- Do not include downloaded feed content or local history.
- Do not claim support for arbitrary feeds, background updates, or GUI features.
- Do not claim that tests cover the live network.
- Include the minimum supported Python version implied by the syntax.

## Checkpoint

Stage 5 is complete only after the learner follows the README from the project
root, verifies the help and test commands, confirms that all five tests pass,
and reviews the documented limitations before committing the README.

