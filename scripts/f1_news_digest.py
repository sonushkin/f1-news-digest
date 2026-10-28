"""Display and locally track a small digest of Formula 1 RSS news."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen


FEED_URL = "https://feeds.bbci.co.uk/sport/formula1/rss.xml"
SOURCE_NAME = "BBC Sport"
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_HISTORY = PROJECT_ROOT / "data" / "news_history.json"
USER_AGENT = "F1NewsDigest/1.0 (non-commercial educational project)"


class FeedError(Exception):
    """Raised when the RSS feed cannot be downloaded or parsed."""


class HistoryError(Exception):
    """Raised when existing reading history is invalid or unreadable."""


@dataclass(frozen=True)
class NewsItem:
    """One normalized item from the RSS feed."""

    identifier: str
    title: str
    published: str
    link: str
    description: str


def positive_integer(value: str) -> int:
    """Convert a command-line value to a positive integer."""
    try:
        number = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("limit must be a whole number") from exc
    if number <= 0:
        raise argparse.ArgumentTypeError("limit must be greater than zero")
    return number


def clean_text(value: str | None, fallback: str) -> str:
    """Remove simple markup and normalize whitespace from feed text."""
    if not value:
        return fallback
    without_tags = re.sub(r"<[^>]+>", " ", html.unescape(value))
    cleaned = " ".join(html.unescape(without_tags).split())
    cleaned = re.sub(r"\s+([.,;:!?])", r"\1", cleaned)
    return cleaned or fallback


def fetch_feed(url: str = FEED_URL, timeout: int = 10) -> bytes:
    """Download RSS bytes with a timeout and a descriptive user agent."""
    request = Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urlopen(request, timeout=timeout) as response:
            return response.read()
    except (URLError, TimeoutError, OSError) as exc:
        raise FeedError(f"could not download the RSS feed: {exc}") from exc


def parse_rss(xml_data: bytes) -> list[NewsItem]:
    """Parse RSS 2.0 bytes into normalized news items."""
    try:
        root = ET.fromstring(xml_data)
    except ET.ParseError as exc:
        raise FeedError(f"the RSS feed contains invalid XML: {exc}") from exc

    news_items: list[NewsItem] = []
    for element in root.findall(".//item"):
        title = clean_text(element.findtext("title"), "Untitled item")
        published = clean_text(
            element.findtext("pubDate"), "Publication date unavailable"
        )
        link = clean_text(element.findtext("link"), "Link unavailable")
        description = clean_text(
            element.findtext("description"), "No description provided"
        )
        identifier = clean_text(element.findtext("guid"), "") or link
        if identifier == "Link unavailable":
            raw_key = f"{title}|{published}|{description}".encode("utf-8")
            identifier = hashlib.sha256(raw_key).hexdigest()
        news_items.append(
            NewsItem(identifier, title, published, link, description)
        )

    if not news_items:
        raise FeedError("the RSS feed contains no news items")
    return news_items


def select_items(
    items: list[NewsItem], limit: int, keyword: str | None
) -> list[NewsItem]:
    """Filter by an optional keyword, then return at most the requested limit."""
    if keyword:
        query = keyword.casefold().strip()
        items = [
            item
            for item in items
            if query in f"{item.title} {item.description}".casefold()
        ]
    return items[:limit]


def load_history(path: Path) -> set[str]:
    """Load seen identifiers; reject malformed history instead of replacing it."""
    if not path.exists():
        return set()
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise HistoryError(f"could not read valid history from {path}: {exc}") from exc

    identifiers = payload.get("seen_ids") if isinstance(payload, dict) else None
    if not isinstance(identifiers, list) or not all(
        isinstance(value, str) for value in identifiers
    ):
        raise HistoryError(f"history has an unexpected format: {path}")
    return set(identifiers)


def save_history(path: Path, identifiers: set[str]) -> None:
    """Save history through a temporary file, then replace the old file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = path.with_suffix(path.suffix + ".tmp")
    payload = {"seen_ids": sorted(identifiers)}
    try:
        temporary_path.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        temporary_path.replace(path)
    except OSError as exc:
        raise HistoryError(f"could not save history to {path}: {exc}") from exc


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line parser."""
    parser = argparse.ArgumentParser(
        description="Show recent Formula 1 news from BBC Sport."
    )
    parser.add_argument(
        "--limit",
        type=positive_integer,
        default=5,
        help="maximum number of items to display (default: 5)",
    )
    parser.add_argument(
        "--keyword",
        help="optional case-insensitive word or phrase to find",
    )
    return parser


def run(limit: int, keyword: str | None, history_path: Path) -> int:
    """Run the digest workflow and return a process exit code."""
    try:
        items = parse_rss(fetch_feed())
        selected = select_items(items, limit, keyword)
        seen_ids = load_history(history_path)
    except (FeedError, HistoryError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"F1 News Digest — Source: {SOURCE_NAME}")
    print(f"Feed: {FEED_URL}\n")
    if not selected:
        print("No news items matched your request.")
        return 0

    new_count = 0
    for number, item in enumerate(selected, start=1):
        status = "SEEN" if item.identifier in seen_ids else "NEW"
        if status == "NEW":
            new_count += 1
        print(f"{number}. [{status}] {item.title}")
        print(f"   Published: {item.published}")
        print(f"   Link: {item.link}")
        print(f"   Description: {item.description}\n")

    updated_ids = seen_ids | {item.identifier for item in selected}
    try:
        save_history(history_path, updated_ids)
    except HistoryError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"Displayed {len(selected)} item(s); {new_count} marked NEW.")
    return 0


def main() -> int:
    """Parse arguments and start the application."""
    arguments = build_parser().parse_args()
    return run(arguments.limit, arguments.keyword, DEFAULT_HISTORY)


if __name__ == "__main__":
    raise SystemExit(main())

