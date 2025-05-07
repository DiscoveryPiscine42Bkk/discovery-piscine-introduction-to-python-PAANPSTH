#!/usr/bin/env python3

import sys

x = len(sys.argv) - 1

if x < 2:
    print("none")
else:
    for i in range(len(sys.argv) - 1, 0 , -1):
        print(sys.argv[i])