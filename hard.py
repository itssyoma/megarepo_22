#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def sinus(x, eps):
    a = x
    sum, n = a, 1

    # Сумма членов ряда
    while math.fabs(a) > eps:
        a *= (-1) * (x**2 * (2*n+1)) / ((2*n+2)*((2*n+3)**2))
        sum += a
        n += 1

    return(sum)


if __name__ == '__main__':
    x = float(input("Введите значение x: "))
    eps = float(input("Введите желаемую точность: "))
    print("Значение Si(x) =", sinus(x, eps))
