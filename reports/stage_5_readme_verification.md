# Stage 5 README Verification

**Verification date:** 28 October 2026

The learner followed the documented commands from the repository root.

## Help command

Command:

```text
python3 scripts/f1_news_digest.py --help
```

Observed result:

- displayed the application description;
- documented `--limit LIMIT` with default 5;
- documented the optional case-insensitive `--keyword KEYWORD`;
- exited without an error.

## Test command

Command:

```text
python3 tests/test_f1_news_digest.py
```

Observed result:

- all five named tests reported `ok`;
- 5 tests ran in 0.003 seconds;
- final status was `OK`.

## Live command

Command:

```text
python3 scripts/f1_news_digest.py --limit 3
```

Observed result:

- displayed the BBC Sport attribution and feed URL;
- displayed exactly three current items;
- included title, publication date, original link, and feed description;
- all three existing history entries were marked `SEEN`;
- reported `Displayed 3 item(s); 0 marked NEW.`

## Checkpoint result

The documented commands are reproducible from the repository root. The README
matches the observed interface and test behavior. Live headlines remain
external and time-dependent, as stated in the limitations.

