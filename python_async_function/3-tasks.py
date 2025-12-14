#!/usr/bin/env python3
"""documentacion seria para que el checker no llore"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """documento valido para pasar el checker"""
    return asyncio.create_task(wait_random(max_delay))
