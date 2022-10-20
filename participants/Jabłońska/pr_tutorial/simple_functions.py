import numpy as np

def fibonacci(max):
    values = [0, 1]
    while values[-2] + values[-1] < max:
        values.append(values[-2] + values[-1])
    return values


def factorial(value):
    if value == 0:
        return 1
    else:
        return value * factorial(value - 1)
    
    
def is_prime(value: int) -> bool:
    """Check if value is prime
    """
    if value <= 1:
        return False
    
    if value == 2:
        return True
    
    return not np.any([value%n==0 for n in range(2, int(np.sqrt(value)+1))])
