# Stage 4 Prompt: Validation and Debugging

## Context

The minimum F1 News Digest application passed three local tests and two live
RSS runs. The first run marked three items as `NEW`; the second marked the same
items as `SEEN`. Stage 4 must test edge cases using actual terminal evidence.
No defect should be invented merely to create a debugging commit.

## Action

1. Ask the learner to run one safe test command at a time.
2. Verify rejection of zero, negative, and non-numeric limits.
3. Verify a case-insensitive keyword filter using the live feed.
4. Verify an unmatched keyword returns a clear empty-result message.
5. Add focused automated tests for command-line limit validation and malformed
   history protection.
6. Rerun the full local test file after any test or code change.
7. If an actual failure appears, give the `debugger` the exact command, output,
   traceback, and relevant code. Apply only the smallest justified fix and add
   a regression test.
8. Save exact evidence and commit only genuine completed work.

## Tone and format

Use beginner-friendly explanations. Clearly distinguish expected validation
messages from defects. Keep every command reproducible and inspect its real
output before continuing.

## Anticipate edge cases

- `argparse` normally writes validation errors to standard error and exits with
  status 2; this is expected behavior, not automatically a defect.
- Live headlines can change between runs, so a keyword may legitimately match
  zero items.
- Runtime history must remain ignored by Git.
- A malformed history file must never be silently overwritten.
- Do not alter Git history, fabricate an error, or create an unnecessary
  `fix:` commit.

## Checkpoint

Stage 4 is complete only when the learner supplies actual output for invalid
input, keyword filtering, and an empty result; the expanded automated tests
pass; the evidence is saved; and any real defect is either fixed and verified
or explicitly reported as unresolved.

