#!/usr/bin/env python3
# -- coding: utf-8 --

# Создайте рекурсивную функцию, печатающую все возможные перестановки для целых
# чисел от 1 до N.

def per(s):
    if len(s) == 1:
        return [s]
    perm_list = []
    for a in s:
        elements = [x for x in s if x != a]
        z = per(elements)

        for t in z:
            perm_list.append([a] + t)

    return perm_list


if __name__ == '__main__':
    n = int(input("Введите число: "))
    arr = [i + 1 for i in range(n)]

    for line in per(arr):
        print("Вывод: ", line)
