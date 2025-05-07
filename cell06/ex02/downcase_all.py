#!/usr/bin/env python3

import sys

if len(sys.argv) <= 1:
    print("none")
else:
    def down():
        for arg in sys.argv[1:]:
            print(arg.lower())
    
    down()