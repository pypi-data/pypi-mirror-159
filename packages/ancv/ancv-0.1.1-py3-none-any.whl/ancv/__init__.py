from enum import IntEnum
from pathlib import Path

import toml

PROJECT_ROOT = Path(__file__).parent
PACKAGE = __package__


class SIPrefix(IntEnum):
    KILO = 1e3
    MEGA = 1e6

METADATA = toml.load(PROJECT_ROOT / "pyproject.toml")
