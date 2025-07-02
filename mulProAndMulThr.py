"""This script demonstrates the difference between IO bound and CPU bound tasks and use of multithreading and multiprocessing in Python."""

import time
import os
import datetime
from threading import Thread, current_thread
from multiprocessing import Process, current_process


COUNT = 200000000
SLEEP = 10


def io_bound(sec):
    """Simulates an IO bound task by sleeping for a specified number of seconds."""

    pid = os.getpid()
    threadName = current_thread().name
    processName = current_process().name

    print(
        f"now={datetime.datetime.now()} * {pid=} * {processName=} * {threadName=} ---> Start sleeping..."
    )
    time.sleep(sec)
    print(
        f"now={datetime.datetime.now()} * {pid=} * {processName=} * {threadName=} ---> Finished sleeping..."
    )


def cpu_bound(n):
    """Simulates a CPU bound task by performing a countdown from n to 0."""

    pid = os.getpid()
    threadName = current_thread().name
    processName = current_process().name

    print(
        f"now={datetime.datetime.now()} * {pid=} * {processName=} * {threadName=} ---> Start counting..."
    )

    while n > 0:
        n -= 1

    print(
        f"now={datetime.datetime.now()} * {pid=} * {processName=} * {threadName=} ---> Finished counting..."
    )


if __name__ == "__main__":

    # Code snippet for Part 1: IO Bound Job Execution Time Test
    print("=" * 70)
    print("IO Bound Job Execution Time Test without Multithreading & Multiprocessing")
    print("-" * 60)
    start = time.time()
    io_bound(SLEEP)
    io_bound(SLEEP)
    end = time.time()
    print("-" * 60)
    print("Time taken in seconds -", end - start, flush=True)
    print("=" * 70)

    # Code snippet for Part 2: CPU Bound Job Execution Time Test
    print("CPU Bound Job Execution Time Test without Multithreading & Multiprocessing")
    print("-" * 60)
    start = time.time()
    cpu_bound(COUNT)
    cpu_bound(COUNT)
    end = time.time()
    print("-" * 60)
    print("Time taken in seconds -", end - start, flush=True)
    print("=" * 70)

    # Code snippet for Part 3: IO Bound Job Execution Time Test with Multithreading
    print("IO Bound Job Execution Time Test with Multithreading")
    print("-" * 60)
    start = time.time()
    t1 = Thread(target=io_bound, args=(SLEEP,))
    t2 = Thread(target=io_bound, args=(SLEEP,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.time()
    print("-" * 60)
    print("Time taken in seconds -", end - start, flush=True)
    print("=" * 70)

    # Code snippet for Part 4: CPU Bound Job Execution Time Test with Multithreading
    print("CPU Bound Job Execution Time Test with Multithreading")
    print("-" * 60)
    start = time.time()
    t1 = Thread(target=cpu_bound, args=(COUNT,))
    t2 = Thread(target=cpu_bound, args=(COUNT,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.time()
    print("-" * 60)
    print("Time taken in seconds -", end - start, flush=True)
    print("=" * 70)

    # Code snippet for Part 5: CPU Bound Job Execution Time Test with Multiprocessing
    print("CPU Bound Job Execution Time Test with Multiprocessing")
    print("-" * 60)
    start = time.time()
    p1 = Process(target=cpu_bound, args=(COUNT,))
    p2 = Process(target=cpu_bound, args=(COUNT,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    print("-" * 60)
    print("Time taken in seconds -", end - start, flush=True)
    print("=" * 70)

    # Code snippet for Part 6: IO Bound Job Execution Time Test with Multiprocessing
    print("IO Bound Job Execution Time Test with Multiprocessing")
    print("-" * 60)
    start = time.time()
    p1 = Process(target=io_bound, args=(SLEEP,))
    p2 = Process(target=io_bound, args=(SLEEP,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    print("-" * 60)
    print("Time taken in seconds -", end - start, flush=True)
    print("=" * 70)
