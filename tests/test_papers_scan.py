from __future__ import annotations

import importlib.util
import random
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]


def _scanner():
    spec = importlib.util.spec_from_file_location("papers_scan", ROOT / "scripts" / "papers_scan.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.unit
def test_scanner_reads_item_id_from_proceedings_extract() -> None:
    item = str(random.randint(10**7, 10**8 - 1))
    assert _scanner().ID_IN_PDF.match(f"nptm_{item}.pdf").group(1) == item, (
        "Scanner does not read the eLibrary id from a proceedings extract name"
    )


@pytest.mark.unit
def test_scanner_reads_item_id_from_elibrary_download() -> None:
    item = str(random.randint(10**7, 10**8 - 1))
    assert _scanner().ID_IN_PDF.match(f"elibrary_{item}_{random.randint(1, 10**8)}.pdf").group(1) == item, (
        "Scanner does not read the eLibrary id from an eLibrary download name"
    )
