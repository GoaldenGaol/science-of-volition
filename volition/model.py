# volition/model.py
"""
Core utilities for the Science of Volition frozen 2023 model.

This encodes:
- dim4 thresholds
- regime classification
- a simple hazard-of-collapse function

This file does NOT reimplement your extraction pipeline; it just
provides a clean interface on top of the thresholds defined in the
framework docs.
"""

from dataclasses import dataclass
from enum import Enum, auto
import math


# === Thresholds (from your framework) ===

DIM4_COOP_COLLAPSE = 0.92   # cooperation collapses in <40 rounds
DIM4_IRREVERSIBLE = 1.00    # irreversible demographic / institutional band
DIM4_NO_RETURN = 0.70       # no country has returned below this once > 1.0


class Regime(Enum):
    """Coarse regime classification based on dim4."""
    COOPERATIVE = auto()
    PRE_COLLAPSE = auto()
    IRREVERSIBLE = auto()


@dataclass
class VolitionalState:
    """
    Minimal representation of a country/year volitional state.

    You can extend this later with more dims or metadata.
    """
    name: str
    year: int
    dim4: float
    tfr: float | None = None  # optional, if known


def classify_regime(dim4: float) -> Regime:
    """
    Classify a state into a regime based on dim4 thresholds.

    - dim4 > 1.00 -> IRREVERSIBLE
    - dim4 > 0.92 -> PRE_COLLAPSE
    - else        -> COOPERATIVE
    """
    if dim4 > DIM4_IRREVERSIBLE:
        return Regime.IRREVERSIBLE
    if dim4 > DIM4_COOP_COLLAPSE:
        return Regime.PRE_COLLAPSE
    return Regime.COOPERATIVE


def hazard_of_collapse(dim4: float) -> float:
    """
    Smooth, monotone hazard function h(dim4) ∈ (0, 1).

    This is a placeholder interface you can later replace with the
    calibrated curve from your empirical model.
    """
    # Center logistic around the cooperation-collapse threshold
    k = 4.0  # steepness
    x0 = DIM4_COOP_COLLAPSE
    return 1.0 / (1.0 + math.exp(-k * (dim4 - x0)))


def summarize(state: VolitionalState) -> str:
    """
    Human-readable summary for quick CLI / logging use.
    """
    regime = classify_regime(state.dim4)
    hazard = hazard_of_collapse(state.dim4)
    tfr_part = f", TFR={state.tfr:.2f}" if state.tfr is not None else ""
    return (
        f"{state.name} ({state.year}) — "
        f"dim4={state.dim4:.2f}{tfr_part}, "
        f"regime={regime.name}, "
        f"hazard_of_collapse={hazard:.3f}"
    )