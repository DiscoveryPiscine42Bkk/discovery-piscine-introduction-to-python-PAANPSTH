#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    print("none")

else:
    for number in range(11):
        print(f"Table de {number} :", end="")    
        for i in range(11):
            print(f" {i * number}", end="")
        print()
            