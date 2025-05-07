#!/usr/bin/env python3

print("Enter a number less than 25")
x = int(input())

if x > 25:
    print("Error")

while x <= 25:
    x += 1
    print(f"Inside the loop, my variable is {x - 1}")