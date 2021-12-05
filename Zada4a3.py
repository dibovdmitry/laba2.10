#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sort(**kwargs):
    s_num = []
    [s_num.append(s) for s in kwargs.keys()]
    values = []
    [values.append(v) for v in kwargs.values()]
    values.sort()

    return dict(zip(s_num, values))


if __name__ == '__main__':
    sort_num = sort(f=5, s=2, t=8, fr=1, fv=9, sx=16, sv=4, e=21, n=12, tn=7)

    for value in sort_num.items():
        print(value)
