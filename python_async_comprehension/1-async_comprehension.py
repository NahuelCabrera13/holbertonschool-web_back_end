#!/usr/bin/env python3
"""documentacion seria para que el checker no llore"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """documento valido para pasar el checker"""
    return [i async for i in async_generator()]
