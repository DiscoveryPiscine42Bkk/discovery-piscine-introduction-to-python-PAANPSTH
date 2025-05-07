#!/usr/bin/env python3

x = [2, 8, 9, 48, 8, 22, -12, 2]
y = set()


for number in x:
    if number > 5:
        y.add(number + 2)


print("Original array: ", x)
print("New array: ", y)