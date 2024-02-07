#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
print(f'Last digit of {number} is {last}',end=' ')
if last != 0 and last < 6:
    print('and is less than 6 and not 0\n')
elif last > 5:
    print('and is greater than 5\n')
elif last == 0:
    print('and is 0\n')