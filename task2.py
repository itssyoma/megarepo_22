#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
    

def color(cycle_year):
    cycle_year %= 10
    if cycle_year == 0 or cycle_year == 1:
        return "Зеленый"
    if cycle_year == 2 or cycle_year == 3:
        return "Красный"
    if cycle_year == 4 or cycle_year == 5:
        return "Желтый"
    if cycle_year == 6 or cycle_year == 7:
        return "Белый"
    else:
        return "Черный"

def animal(cycle_year):
    animals = ['мышь', 'корова', 'тигр', 'заяц', 'дракон', 'змея', 'лошадь', 'овца', 'обезьяна', 'курица', 'собака', 'свинья']
    return animals[cycle_year % 12]

if __name__ == "__main__":
    year = int(input("Введите год: "))
    if year < 1984:
        print("Недопустимое значение года!", file=sys.stderr)
        exit(1)

    cycle_year = (year - 1984) % 60
    print(f"{year} год по японскому календарю\nГод в цикле: {cycle_year+1}\nЦвет: {color(cycle_year)}\nЖивотное: {animal(cycle_year)}")

