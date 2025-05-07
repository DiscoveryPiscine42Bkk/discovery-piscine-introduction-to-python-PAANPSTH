#!/usr/bin/env python3

def greetings(x=None):
    if x is None:
        print("Hello, noble stranger.")
    elif isinstance(x, str):
        print(f"Hello, {x}.")
    else:
        print("Error! It was not a name.")


greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)