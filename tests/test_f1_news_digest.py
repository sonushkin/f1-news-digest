"""Small standard-library tests for F1 News Digest."""

import sys
import tempfile
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

import f1_news_digest as digest  # noqa: E402


class DigestTests(unittest.TestCase):
    """Check core logic without using the live network."""

    @classmethod
    def setUpClass(cls) -> None:
        fixture = PROJECT_ROOT / "tests" / "fixtures" / "sample_f1_feed.xml"
        cls.items = digest.parse_rss(fixture.read_bytes())

    def test_parse_rss_and_missing_fields(self) -> None:
        self.assertEqual(len(self.items), 3)
        self.assertEqual(
            self.items[0].description,
            "The team completed several long runs.",
        )
        self.assertEqual(self.items[2].link, "Link unavailable")

    def test_keyword_filter_is_case_insensitive_and_limited(self) -> None:
        selected = digest.select_items(self.items, limit=1, keyword="FERRARI")
        self.assertEqual([item.identifier for item in selected], ["test-item-001"])

    def test_history_round_trip(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            history_path = Path(directory) / "history.json"
            self.assertEqual(digest.load_history(history_path), set())
            digest.save_history(history_path, {"test-item-001"})
            self.assertEqual(
                digest.load_history(history_path), {"test-item-001"}
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)

