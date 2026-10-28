# Stage 3 Verification

**Verification date:** 28 October 2026

## Local tests

The learner ran:

```text
python3 tests/test_f1_news_digest.py
```

Observed result:

- `test_history_round_trip` — `ok`
- `test_keyword_filter_is_case_insensitive_and_limited` — `ok`
- `test_parse_rss_and_missing_fields` — `ok`
- 3 tests ran in 0.002 seconds
- final status: `OK`

## Live RSS run

The learner ran the application with `--limit 3` against the documented BBC
Sport Formula 1 RSS feed.

First observed run:

- 3 items displayed;
- all 3 items marked `NEW`;
- every displayed item included a title, publication date, link, and
  description;
- the output credited BBC Sport and printed the feed URL.

Second observed run with the same command:

- the same 3 items displayed;
- all 3 items marked `SEEN`;
- 0 items marked `NEW`.

This confirms that the history persisted between the two observed runs.

## Git-safety check

The runtime file `data/news_history.json` exists locally and Git reports it as
ignored (`!!`). It will not be included in the application commit.

## Checkpoint result

The Stage 3 draft passed its local tests and minimum live console workflow. No
debugging change was required for this checkpoint. The files are not committed
yet.
