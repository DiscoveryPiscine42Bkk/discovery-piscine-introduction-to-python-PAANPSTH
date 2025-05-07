#!/usr/bin/env python3

import sys

def shrink(arg):
    print(arg[:8])

def enlarge(arg):
    x = 8 - len(arg)
    print(arg + x * "Z")

if len(sys.argv) < 2:
    print("none")

else:
    for arg in sys.argv[1:]:
        if len(arg) == 8:
            print(arg)
        else: 
            if len(arg) > 8:
                shrink(arg)
            else:
                enlarge(arg)