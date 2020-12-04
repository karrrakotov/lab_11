#!/usr/bin/env python3
# -- coding: utf-8 --

# Создайте рекурсивную функцию, печатающую все возможные перестановки для целых
# чисел от 1 до N.

def all_perms(arr):
    if len(arr) == 1:
        return [arr]
    else:
        a = arr[0]
        p = all_perms(arr[1:])
        r = []
        for pp in p:
            for i in range(len(pp)):
                tmp = pp[0:i] + [a] + pp[i:]
                r.append(tmp)
            r.append(pp + [a])
        return r


if __name__ == '__main__':
    n = int(input("Введите n: "))
    print(all_perms([i for i in range(1, n + 1)]))
