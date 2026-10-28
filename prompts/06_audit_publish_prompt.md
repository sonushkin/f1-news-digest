# Stage 6 Prompt: Final Audit and GitHub Publication

## Context

F1 News Digest has completed implementation, validation, and documentation.
Five local tests pass, the live console workflow was verified, the README was
followed from the project root, and the working tree was clean after four
genuine commits. The assignment requires a public GitHub repository link.

## Action

1. Audit the working tree, concise Git history, tracked-file list, ignored
   runtime history, and repository configuration.
2. Rerun the documented tests immediately before publication.
3. Search tracked text for likely secrets or credentials without printing
   unrelated local data.
4. Confirm that prompts, AI outputs, reports, code, tests, and README are
   included and that `data/news_history.json` is excluded.
5. Create a final audit record and submission checklist.
6. Ask the learner to confirm the public repository name.
7. Check GitHub authentication, create one public repository, add its HTTPS
   remote, and push `main` only after the learner authorizes those actions.
8. Verify the repository URL and public visibility after the push.

## Tone and format

Give one safe command at a time and use exact observed output. Clearly separate
local verification from external publication.

## Anticipate edge cases

- Do not publish `data/news_history.json`, caches, secrets, or credentials.
- Do not force-push, rewrite, squash, or fabricate Git history.
- Do not amend the first commit merely because its automatically selected local
  email is not linked to GitHub.
- Do not create a private repository when the assignment requires a public one.
- Do not overwrite an existing remote repository with the same name.
- Do not print or commit authentication tokens.
- Stop and report authentication, naming, permission, or push errors exactly.

## Checkpoint

Stage 6 is complete only when the audit passes, the learner-approved public
repository exists, branch `main` is pushed without history rewriting, the
public URL opens, and the submission checklist records the final link and
required files.

