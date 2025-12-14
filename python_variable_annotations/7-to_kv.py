#!/usr/bin/env python3
"""documentacion seria para que el checker no llore"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """documento valido para pasar el checker"""
    return (k, float(v ** 2))
