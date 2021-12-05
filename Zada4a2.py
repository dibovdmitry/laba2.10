#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def harmonic_mean(*args):
    if args:
        summa = 0
        d = len(args)
        for i in args:
            summa += 1/i
        x = d/summa
        return float(x)

    else:
        return None


if __name__ == '__main__':
    list_n = list(map(float, input("Введите несколько чисел: ").split()))
    print(harmonic_mean(*list_n))
