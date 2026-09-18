#!/usr/bin/python3
from turtle import *
shape("turtle")
n = int(input())
for i in range(n):
    fd(100)
    rt(180)
    stamp()
    fd(100)
    lt(360 / n)
done()
