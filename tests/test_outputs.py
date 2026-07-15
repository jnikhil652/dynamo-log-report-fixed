import json
from pathlib import Path

REPORT = Path("/app/report.json")


def _load_report():
    """Load /app/report.json as JSON (fails if missing or not valid JSON)."""
    assert REPORT.exists(), "no report.json found at /app/report.json"
    return json.loads(REPORT.read_text())


def test_total_requests():
    """Success criterion 1: total_requests is the number of requests in the log (6)."""
    assert _load_report()["total_requests"] == 6


def test_unique_ips():
    """Success criterion 2: unique_ips is the number of distinct client IPs (3)."""
    assert _load_report()["unique_ips"] == 3


def test_top_path():
    """Success criterion 3: top_path is the most-requested path (/index.html)."""
    assert _load_report()["top_path"] == "/index.html"
