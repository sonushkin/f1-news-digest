# Stage 4 AI Output: Test Plan

The `debugger` should not change the working program before a failure is
observed. The planned sequence is:

1. run with `--limit 0` and confirm a helpful validation error;
2. repeat with a negative and non-numeric value;
3. run a live case-insensitive keyword search;
4. run a deliberately unmatched keyword and confirm a clear message;
5. add local tests for limit validation and protection of malformed history;
6. rerun all local tests;
7. save the exact evidence and review Git status.

An `argparse` usage message followed by `limit must be greater than zero` is an
expected result for `--limit 0`. It should not be reported as a program defect
unless a traceback appears or the process continues into the news workflow.

