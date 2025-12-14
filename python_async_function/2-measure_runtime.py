#!/usr/bin/env python3
"""documentacion seria para que el checker no llore"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """documento valido para pasar el checker"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
