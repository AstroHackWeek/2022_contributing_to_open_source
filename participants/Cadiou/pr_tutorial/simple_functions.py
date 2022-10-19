from typing import List


def fibonacci(vmax: int) -> List[int]:
    """Compute the fibonnaci sequence up to max.
    
    Argument:
    ---------
    vmax: int, positive
        The maximum value of the sequence.

    Returns:
    --------
    fibs: list of int
        The list of fibonacci numbers.
    """
    if vmax == 0:
        return [0]
    elif vmax == 1:
        return [0, 1]
    elif vmax < 0:
        raise ValueError('vmax must be positive')

    values = [0, 1]
    while values[-2] + values[-1] < vmax:
        values.append(values[-2] + values[-1])

    return values


def factorial(value: int) -> int:
    """Compute the factorial of a value.
    
    Argument:
    ---------
    value: int, positive
        The value to compute the factorial of.
    
    Returns:
    --------
    fact: int
        The factorial of the value.
    """
    if value < 0:
        raise ValueError("value must be positive, got {}".format(value))
    elif value == 0:
        return 1
    else:
        return value * factorial(value - 1)

def is_prime(value: int, /) -> bool:
    """Check if a value is prime.
    
    Argument:
    ---------
    value: int, positive
        The value to check if it is prime.
    
    Returns:
    --------
    is_prime: bool
        True if the value is prime, False otherwise.
    """
    if value < 0:
        raise ValueError("value must be positive, got {}".format(value))
    elif value == 0 or value == 1:
        return False

    for i in range(2, value):
        if value % i == 0:
            return False
    return True