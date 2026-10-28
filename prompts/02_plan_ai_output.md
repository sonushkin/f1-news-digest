# Stage 2 AI Output: Source and Scaffold Plan

## Selected source

- **Publisher:** BBC Sport
- **Feed:** BBC Sport - Formula 1
- **URL:** `https://feeds.bbci.co.uk/sport/formula1/rss.xml`
- **Expected format:** RSS 2.0 XML
- **Planned credit:** `Source: BBC Sport` with the article's original link.

The source is suitable for a small personal feed reader because it provides
Formula 1 headlines, links, dates, and short descriptions without requiring an
account or API key. Availability is external and can change, so the program
must handle network and feed failures honestly.

## Usage boundary

This is a non-commercial academic application. It will display current feed
fields without changing their meaning, link to the original BBC pages, show
BBC Sport attribution, and avoid BBC logos or claims of endorsement. Runtime
feed content and local reading history will not be committed to Git. The
repository will contain only original program code, tests, documentation, and
a small synthetic XML fixture written for testing.

## Planned standard-library modules

- `argparse` for the console interface;
- `urllib.request` and `urllib.error` for HTTP retrieval and errors;
- `xml.etree.ElementTree` for RSS parsing;
- `json` and `pathlib` for local history;
- `html`, `re`, and `datetime` only where needed for safe formatting.

No external package is required for the minimum version.

## Project structure

```text
mini_project_2_programming/
├── .gitignore
├── AGENTS.md
├── README.md
├── data/                  # ignored runtime history; placeholder tracked
├── prompts/               # accepted prompts and AI outputs
├── reports/               # checkpoints and test evidence
├── scripts/               # application script will be added in Stage 3
└── tests/
    └── fixtures/          # synthetic RSS fixture will be added in Stage 3
```

## Git checkpoint commands

The learner should initialize Git in this project, inspect the staged file
list, and create one real commit named `chore: scaffold mini project`. The
commit is not verified until the learner returns the exact output of
`git status` and `git log --oneline`.

## Deferred work

No application implementation, live-feed run, debugging, README replacement,
or GitHub publication belongs to Stage 2.

