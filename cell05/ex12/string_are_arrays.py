#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else: 
    arg1 = sys.argv[1]
    if "z" in arg1:
        for char in arg1:
            if char == "z":
                print("z", end="")
    else: 
        print("none")