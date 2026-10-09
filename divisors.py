#!/usr/bin/python3
a = int(input())
divisors = []
for x in range(2,10):
    if a % x == 0:
        while a % x == 0:
            divisors.append(x)
            a = a // x
print(divisors)
    

