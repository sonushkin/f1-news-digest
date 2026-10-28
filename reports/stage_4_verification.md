# Stage 4 Validation and Debugging Evidence

**Verification date:** 28 October 2026

## Manual validation

The learner ran the application with three invalid limits.

| Input | Observed message | Result |
| --- | --- | --- |
| `--limit 0` | `limit must be greater than zero` | Expected rejection |
| `--limit -2` | `limit must be greater than zero` | Expected rejection |
| `--limit abc` | `limit must be a whole number` | Expected rejection |

Each case displayed command usage, stopped before the feed workflow, and did
not expose a Python traceback.

## Live keyword checks

The learner ran `--limit 5 --keyword AnToNeLlI` against the documented live
feed. Five matching items were displayed, proving that the search ignored
letter case and respected the requested limit. Two items were already `SEEN`
and three were `NEW` at that moment.

The learner then used the deliberately unmatched keyword
`__NO_MATCH_EXPECTED_123__`. The observed result was:

```text
No news items matched your request.
```

No traceback was displayed.

## Expanded automated tests

Two tests were added for command-line limit validation and malformed-history
protection. The learner reran the complete test file and observed:

- `test_history_round_trip` — `ok`
- `test_keyword_filter_is_case_insensitive_and_limited` — `ok`
- `test_limit_validation` — `ok`
- `test_malformed_history_is_not_overwritten` — `ok`
- `test_parse_rss_and_missing_fields` — `ok`
- 5 tests ran in 0.003 seconds
- final status: `OK`

## Debugging conclusion

No reproducible program defect was found during Stage 4. Therefore, the
`debugger` did not propose a code fix and no artificial `fix:` commit is
justified. The genuine change in this stage is the expanded validation test
coverage.

