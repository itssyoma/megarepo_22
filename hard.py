#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def sinus(x, eps):
    sum = 0
    n = 0
    while True:
        term = ((-1)**n * x**(2*n+1)) / (factorial(2*n+1) * (2*n+1))
        sum += term
        if math.fabs(sum - term) < eps:
            break
    return sum


if __name__ == '__main__':
    x = float(input("Введите значение x: "))
    eps = float(input("Введите желаемую точность: "))
    print("Значение Sin(x) =", sinus(x, eps))
