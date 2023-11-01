#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    result = []
    
    for i in range(100, 1000):
        number = str(i)
        a = int(number[0])
        b = int(number[1])
        c = int(number[2])
        if a*b*c == a+b+c:
            result.append(i)
    
    print(result)

