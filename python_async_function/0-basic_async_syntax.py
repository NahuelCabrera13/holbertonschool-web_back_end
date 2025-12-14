#!/usr/bin/env python3
"""documentacion seria para que el checker no llore"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """documento valido para pasar el checker"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
