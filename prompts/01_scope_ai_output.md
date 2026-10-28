# Stage 1 AI Output: Accepted Project Scope

## Working title

**F1 News Digest**

## Short description

F1 News Digest is a beginner-friendly Python console application for Formula 1
fans who want to check recent news without opening several pages manually. It
loads a public RSS or Atom feed, presents a compact list of recent items, and
uses a local history file to show which items are new since an earlier run.

## Intended user and everyday problem

- **User:** a Formula 1 fan using a terminal.
- **Problem:** manually checking a news site and remembering which stories have
  already been seen is repetitive.
- **Automation:** retrieve, filter, format, and locally track recent feed items.

## Minimum required features

1. Accept a positive item limit.
2. Accept an optional case-insensitive keyword filter.
3. Retrieve one verified public Formula 1 RSS or Atom feed.
4. Display each matching item's status (`NEW` or `SEEN`), title, source,
   publication date, link, and available feed description.
5. Store stable article identifiers in a local JSON history file.
6. Report ordinary input, network, parsing, and empty-result problems in clear
   language without a traceback.

## Inputs

- required or defaulted maximum number of items;
- optional keyword;
- a feed URL selected and documented during Stage 2.

## Outputs

- a numbered text digest in the terminal;
- a clear message when no items match or the feed cannot be processed;
- a locally updated JSON history file after a successful run.

## Persistence

Use a documented JSON file inside the project, for example
`data/news_history.json`. Update it only after a feed has been processed
successfully. Preserve valid existing history and use a safe write strategy so
an interrupted write does not silently destroy it.

## Explicit exclusions for the minimum version

- no graphical interface;
- no scheduled background process or notifications;
- no account login, paid API, or secret key;
- no full-article scraping or paywall bypass;
- no AI-generated paraphrase of an article;
- no sentiment analysis, prediction, or claim verification;
- no multi-source deduplication in the minimum version.

## Acceptance criteria

1. A documented command starts the program with Python 3.
2. With a valid feed and limit `5`, at most five matching items are displayed.
3. Keyword matching is case-insensitive and checks the available title and
   description.
4. The first successful run marks unseen identifiers as `NEW`; a later run
   against the same fixture recognizes them as `SEEN`.
5. A zero, negative, or non-numeric limit produces a helpful validation message.
6. Unavailable or malformed feed input produces a helpful message without
   corrupting history.
7. Missing optional fields are displayed with an honest fallback rather than
   causing a crash.
8. Parsing, filtering, limiting, and history logic can be tested without live
   network access using a small local feed fixture.

## Future ideas, outside the minimum version

- multiple feeds and duplicate detection;
- scheduled updates and desktop notifications;
- user-selectable teams or drivers;
- an external summarization service added only with explicit key management,
  source attribution, and documented limitations.

