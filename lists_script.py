#!/usr/bin/python3
from sys import stdin
a = []
for line in stdin:
    a.append(line)
a.sort(reverse = True)
print(a)

