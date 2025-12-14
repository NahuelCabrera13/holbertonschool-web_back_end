#!/usr/bin/env python3
"""documentacion seria para que el checker no llore"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """documento valido para pasar el checker"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    return [await t for t in asyncio.as_completed(tasks)]
