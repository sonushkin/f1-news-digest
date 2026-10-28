# F1 News Digest

F1 News Digest is a beginner-friendly Python console application for Formula 1
fans who want to check recent news without opening several pages manually. It
loads the BBC Sport Formula 1 RSS feed, displays a compact digest, and uses a
local history file to show which items are new since an earlier run.

This project was created for **Mini-Project 2: Programming** in the GSOM AI
Intro course.

## Features

- downloads current Formula 1 RSS items from BBC Sport;
- displays the title, publication date, original link, and feed description;
- limits the number of displayed items with `--limit`;
- filters titles and descriptions with a case-insensitive `--keyword`;
- marks displayed items as `NEW` or `SEEN` between successful runs;
- validates ordinary input and reports expected failures without a traceback;
- stores reading history locally and protects malformed history from silent
  replacement.

## Source and attribution

News metadata comes from the **BBC Sport - Formula 1** RSS feed:

<https://feeds.bbci.co.uk/sport/formula1/rss.xml>

Every live result is identified as coming from BBC Sport and retains its
original link. Feed descriptions are publisher-provided text; they are not
AI-generated summaries. The application is a non-commercial academic project,
does not use BBC logos, and does not imply BBC endorsement. Review the current
[BBC Terms of Use](https://www.bbc.co.uk/usingthebbc/terms/) before reusing the
feed, especially for commercial purposes.

Downloaded feed content and local reading history are not committed to this
repository.

## Requirements

- Python 3.10 or later;
- an internet connection for live news;
- no third-party Python packages.

## Run the program

Open a terminal in the repository root.

Show five recent items (the default):

```bash
python3 scripts/f1_news_digest.py
```

Show at most three items:

```bash
python3 scripts/f1_news_digest.py --limit 3
```

Find at most five items whose title or description contains `Antonelli`,
ignoring letter case:

```bash
python3 scripts/f1_news_digest.py --limit 5 --keyword Antonelli
```

Show all available options:

```bash
python3 scripts/f1_news_digest.py --help
```

The live headlines change over time. The output follows this structure:

```text
F1 News Digest — Source: BBC Sport
Feed: https://feeds.bbci.co.uk/sport/formula1/rss.xml

1. [NEW] <headline from the current feed>
   Published: <publication date>
   Link: <original BBC link>
   Description: <description supplied by the feed>

Displayed 1 item(s); 1 marked NEW.
```

On a later run, a previously displayed item is marked `SEEN`.

## Input validation

`--limit` must be a whole number greater than zero. For example, this command
is rejected before any network request:

```bash
python3 scripts/f1_news_digest.py --limit 0
```

If no item matches a keyword, the program prints:

```text
No news items matched your request.
```

Network, invalid XML, and invalid-history problems produce a concise error
message. They do not silently replace valid history.

## Run the tests

The tests use a synthetic local RSS file and do not require internet access:

```bash
python3 tests/test_f1_news_digest.py
```

The verified suite contains five tests covering RSS parsing, missing fields,
case-insensitive filtering, limiting, history persistence, limit validation,
and malformed-history protection.

## Local history

After a successful live run, the program creates:

```text
data/news_history.json
```

The file stores only identifiers for items displayed by the program. It is
listed in `.gitignore`, remains on the local computer, and can be removed by
the user to reset `NEW`/`SEEN` tracking. The program never deletes it
automatically.

## Project structure

```text
.
├── scripts/f1_news_digest.py       # console application
├── tests/test_f1_news_digest.py    # standard-library tests
├── tests/fixtures/                 # synthetic RSS test data
├── prompts/                        # prompts and recorded AI outputs
├── reports/                        # source and verification evidence
├── data/                           # ignored local runtime history
├── .opencode/                      # course agent definitions and commands
├── AGENTS.md                       # project workflow rules
└── README.md
```

## Limitations

- the minimum version uses one English-language source;
- live results depend on the external feed and network availability;
- the parser targets the selected RSS 2.0 structure, not every RSS/Atom variant;
- keyword matching is literal text matching, not semantic search;
- the program displays feed descriptions rather than generating new summaries;
- it does not verify claims in articles;
- there is no graphical interface, scheduler, notification system, or
  multi-source duplicate detection.

## Use of AI

An AI assistant helped scope the task, draft the Python program and tests,
plan edge-case checks, and prepare this README. The accepted prompts and AI
outputs are stored separately in `prompts/`. The learner ran the commands,
reviewed the actual output, verified the tests and live workflow, and kept only
evidence-backed results. No debugging failure or `fix:` commit was invented.

