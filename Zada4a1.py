#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def geometric_mean(*args):
    if args:
        multi = 1
        for i in args:
            multi *= i
        sr_geom = pow(multi, 1/len(args))
        return float(sr_geom)

    else:
        return None


if __name__ == '__main__':
    list_n = list(map(float, input("Введите несколько чисел: ").split()))
    print(geometric_mean(*list_n))
