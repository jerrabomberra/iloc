# encryption

import pandas as pd
import numpy as np

# def key(a, b):
#     keys = a * b
#     return keys

# print("Key =",key(8,7))


def prime(a, b):
    # set up list
    data = []
    # iterate over a and b
    for digit in range(a, b + 1):
        # If digit in range >1
        if digit > 1:
            # set is_prim to True
            is_prime = True
            # limit the calculation to values gt 2 for prime numbers divisor
            for i in range(2, digit):
                # check if mod of digit / i == 0 - which indicates a non prime value
                if (digit % i) == 0:
                    is_prime = False
                    break
                # append the value of digit to the list
            if is_prime:
                data.append(digit)
    return data


def multi(data):
    for index, element in enumerate(data):
        print(f"Index: {index}, Element: {element}")


multi(prime(2, 24))
