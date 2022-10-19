from typing import Sequence

def fibonacci(max: int) -> List[int]:
    """ Calculate the Fibonacci series up to max """
    values = [0, 1]
    while values[-2] + values[-1] < max:
        values.append(values[-2] + values[-1])
    return values


def factorial(value: int) -> int:
    """ Calculate the factorial of a positive value """
    if value < 0:
        raise ValueError("Value needs to be positive")
    if value == 0:
        return 1
    else:
        return value * factorial(value - 1)
