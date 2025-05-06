#!/usr/bin/env python3

import sys

x = len(sys.argv) - 1



if x != 1:
    print("none")
else:
    y = sys.argv[1]
    z = y.upper()
    print(z)