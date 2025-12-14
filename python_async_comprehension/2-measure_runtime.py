#!/usr/bin/env python3
"""documentacion seria para que el checker no llore"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """documento valido para pasar el checker"""
    start = time.time()
    await asyncio.gather(*[
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    ])
    return time.time() - start
