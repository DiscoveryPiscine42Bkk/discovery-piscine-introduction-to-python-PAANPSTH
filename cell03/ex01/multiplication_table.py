#!/usr/bin/env python3

print("Enter a number")
x = int(input())
for i in range(10):
    result = i * x #this row must be under for loop
    print(f"{i} x {x} = {result}") #this row must be under for loop
