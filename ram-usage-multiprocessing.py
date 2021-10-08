"""
* produce NUM_INTS of random numbers in a numpy array
* make them a property of an object
* spawn process with target — object method
* observer rise in memory. entire object is copied

to observe ram, install memory_profiler
    pip install memory_profiler

Then run the profiler:
    mprof run -C -M python3 ram-usage-multiprocessing.py

Look at the plots:
    mprof plot

Lesson: fork is useful for global variables, they are available in CoW fashion
from subprocesses

https://stackoverflow.com/questions/38084401/leveraging-copy-on-write-to-copy-data-to-multiprocessing-pool-worker-process
https://stackoverflow.com/questions/659865/multiprocessing-sharing-a-large-read-only-object-between-processes
"""

import time
import multiprocessing as mp
import numpy as np
from numpy import random

NUM_INTS = 10000000
NUM_PROC = 5


class A:
    def __init__(self, data):
        self.data = data

    def another_func(self, arg):
        return arg[0] + arg[1]

    def process(self):
        self.data[0] = 145
        time.sleep(5)

    def run(self):
        ctx = mp.get_context("fork")
        processes = [ctx.Process(target=self.process) for i in range(NUM_PROC)]
        [p.start() for p in processes]


def main():
    data = np.random.rand(NUM_INTS)
    print(data[0])
    a = A(data)
    a.run()
    time.sleep(2)
    print(data[0])


if __name__ == "__main__":
    main()
