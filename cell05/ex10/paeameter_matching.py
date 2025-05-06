#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    correct = sys.argv[1]
    answer = input(f"What was the parameter? ")
    if answer != correct:
        print("Nope, sorry...")
    else:
        print("Good job!")