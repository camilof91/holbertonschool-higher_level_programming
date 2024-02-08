#!/usr/bin/python3
for numero in range(0, 88):
    if numero / 10 < numero % 10:
        print(f'{numero:02}, ', end='')
print(89)
