#!/usr/bin/python3
"""
Log parsing: reads a stdin line by line and computes metrics
"""
import fileinput
from typing import List


line_count = 0
total_size = 0
status_codes = []

for line in fileinput.input():
    ln = line.split()

    if len(ln) != 9:
        continue

    line_count += 1
    status_codes.append(ln[7])
    total_size += int(ln[8])

    if line_count == 10:
        for status in set(sorted(status_codes)):
            counts = status_codes.count(status)
            print("{}: {}".format(status, counts))

        print("File size: {}".format(total_size))
        line_count = 0
        total_size = 0
