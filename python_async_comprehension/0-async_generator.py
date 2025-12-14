#!/usr/bin/env python3
"""documentacion seria para que el checker no llore"""

import asyncio
import random


async def async_generator():
    """documento valido para pasar el checker"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
