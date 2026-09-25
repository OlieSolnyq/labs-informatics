#!/usr/bin/python3
from turtle import *
from math import cos
from math import sqrt
from math import pi


k = 5

up()
fd(5 * k)
down()

N = 3
R = 5
for i in range(5):
    def storona(r, n):
        return sqrt(2 * r ** 2 * (1 - cos(2 * pi / n)))

    def outer_angle(n):
        return (2 * 180)/n 


    lt(180 - (90 * (N - 2))/N)

    for _ in range(N):
        fd(storona(R,N) * k)
        lt(outer_angle(N))

    rt(outer_angle(N) + (90 * (N-2)/N))

    up()
    fd(5 * k)
    down()

    R += 5
    N += 1

done()
