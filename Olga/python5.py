#!/usr/bin/python3
from turtle import *
shape("turtle")
a = 1
for i in range(10):
    for i in range(4):
        fd(a * 10)
        lt(90)
    up()
    rt(90)
    fd(10)
    rt(90)
    fd(10)
    rt(180)
    a += 2
    down()
done()
    
