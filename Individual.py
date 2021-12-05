#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sum_of_arguments(*args):
    a = 1
    negative = 0
    for idx, n in enumerate(args):
        if n < 0:
            args = args[idx+1:]
            negative += 1
            break
    for idx, n in enumerate(args):
        if n < 0:
            args = args[:idx]
            negative += 1
            break
    if negative != 2:
        return "Нет отрицательных аргументов"
    else:
        for n in args:
            a *= n
        return a


if __name__ == '__main__':
    arg = list(map(float, input("Введите несколько чисел: ").split()))
    print(sum_of_arguments(*arg))
    if not arg:
        print("None")
