"""Filter registry.

WORKSHOP NOTE
-------------
This file is the intentional merge-conflict hotspot.
When multiple contributors register new filters at the same
time, they all edit the FILTERS dictionary below and the
imports above — which produces real merge conflicts that
teams will learn to resolve during the workshop.
"""

from .filters.base import Filter
from .filters.grayscale import GrayscaleFilter

from .filters.sepia import SepiaFilter  # <-- YENI IMPORT

FILTERS: dict[str, type[Filter]] = {
    "grayscale": GrayscaleFilter,
    "sepia": SepiaFilter,  # <-- YENI KAYIT
    "blur": BlurFilter
}

def get_filter(name: str) -> Filter:
    if name not in FILTERS:
        available = ", ".join(FILTERS.keys())
        raise ValueError(f"Unknown filter: {name!r}. Available: {available}")
    return FILTERS[name]()