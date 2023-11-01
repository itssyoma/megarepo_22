#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == "__main__":
    n = str(input("Введите возраст: "))

    if int(n) <= 100:
        print("Недопустимое значение возраста!", file=sys.stderr)
        exit(1)
    

    if n[-2:] in ["11", "12", "13", "14"]:
        print(f"Мне {n} лет")
    elif n[-1] == "1":
        print(f"Мне {n} год")
    elif n[-1] in "234":
        print(f"Мне {n} года")
    else:
        print(f"Мне {n} лет")
        
