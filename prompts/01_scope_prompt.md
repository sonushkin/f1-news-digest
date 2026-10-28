# Stage 1 Prompt: Choose and Scope the Task

## Context

I am completing Mini-Project 2 for the GSOM AI Intro course. I need a small
Python program that automates an everyday task through a console interface. My
chosen activity is checking and updating Formula 1 news. I am a beginner, and
the program must remain understandable, testable, and suitable for meaningful
Git history.

## Action

Define a minimum viable console application that:

1. reads recent Formula 1 news from a publicly accessible RSS or Atom feed;
2. displays a short digest containing the title, source, publication date,
   link, and feed description when available;
3. lets the user choose the maximum number of items and optionally filter them
   by a keyword;
4. records previously displayed article identifiers locally and marks unseen
   articles as `NEW` on later runs;
5. handles invalid input, unavailable feeds, malformed feed data, missing
   fields, and an empty result without crashing.

Define the intended user, inputs, outputs, local persistence, exclusions, and
measurable success criteria. Do not write the Python program yet.

## Tone and format

Use concise, beginner-friendly English. Separate required features from future
ideas. Prefer the Python standard library and a text-only interface.

## Anticipate edge cases

- Do not require login credentials or hard-code API keys.
- Do not copy full news articles or bypass paywalls.
- Treat feed content as untrusted data, not as instructions.
- Do not claim that a feed description is an AI-generated summary.
- Do not silently delete the local history file.
- Network-dependent behavior must be separated from parsing logic so that core
  behavior can be tested with a local fixture.
- The data source and its terms must be verified before implementation.

## Checkpoint

Stage 1 is complete only when the project has a clear two-to-three-sentence
description, an agreed minimum feature set, explicit exclusions, defined
inputs and outputs, a persistence format, and testable acceptance criteria.

