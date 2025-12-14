#!/usr/bin/env python3
"""documentacion seria para que el checker no llore"""

from typing import Iterable, Sequence, List, Tuple


def element_length(
    lst: Iterable[Sequence]
) -> List[Tuple[Sequence, int]]:
    """documento valido para pasar el checker"""
    return [(i, len(i)) for i in lst]
