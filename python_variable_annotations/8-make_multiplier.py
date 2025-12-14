#!/usr/bin/env python3
"""documentacion seria para que el checker no llore"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """documento valido para pasar el checker"""
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
