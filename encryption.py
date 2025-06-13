# encryption

import pandas as pd
import numpy as np

# def key(a, b):
#     keys = a * b
#     return keys

# print("Key =",key(8,7))


def prime(a, b):
    data = []
    for digit in range(a, b + 1):
        if digit > 1:
            is_prime = True
            for i in range(2, digit):
                if (digit % i) == 0:
                    is_prime = False
                    break
            if is_prime:
                data.append(digit)
    return data


print(prime(3, 1000))
