"""
Generator-Expressions
"""

import psutil
import os
import sys

print("sys interpreter", sys.executable)


pid = os.getpid()
process = psutil.Process(pid=pid)
print(f"current memory of Process {pid} before x:", process.memory_info().rss / 1024**2)

x = [(i, i**2) for i in range(10**6)]

print(f"current memory of Process {pid} after x:", process.memory_info().rss / 1024**2)

y = ((i, i**2) for i in range(10**6))

print(
    f"current memory of Process {pid} after None:", process.memory_info().rss / 1024**2
)
# print(y[0])
