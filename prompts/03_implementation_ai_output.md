# Stage 3 AI Output: Draft Ready for Learner Testing

The `function-writer` prepared:

- `scripts/f1_news_digest.py` - the console application;
- `tests/fixtures/sample_f1_feed.xml` - synthetic RSS input;
- `tests/test_f1_news_digest.py` - three focused standard-library tests.

The draft uses only the Python standard library. Its core operations are split
into functions for feed retrieval, RSS parsing, filtering, history loading,
and atomic history saving. The command-line layer validates a positive limit
and reports expected failures without exposing a traceback.

This output is a draft, not proof that the program works. Following Topic 6,
the learner must run the proposed test command, inspect the real result, and
return the exact output before a live-feed run or Git commit.

