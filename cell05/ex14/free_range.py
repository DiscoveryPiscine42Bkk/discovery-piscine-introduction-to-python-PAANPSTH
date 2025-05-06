#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("none")
else:
    num1 = sys.argv[1]
    num2 = sys.argv[2]
    start = int(num1)
    stop = int(num2)

    if start <= stop:
        increase = list(range(start, stop + 1, + 1))
        print(increase)
    else:
        decrease = list(range(start, stop - 1, -1))
        print(decrease)

#if stop not +- 1 it will ended before stop