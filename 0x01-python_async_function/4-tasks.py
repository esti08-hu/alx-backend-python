#!/usr/bin/env python3
'''Task 4's module.
'''
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes task_wait_random n times.

    Parameters:
    n (int): The number of times the task_wait_random function should be executed.
    max_delay (int): The maximum delay (in seconds) for the task_wait_random function.

    Returns:
    List[float]: A list of wait times generated by the task_wait_random function, sorted in ascending order.
    '''
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
