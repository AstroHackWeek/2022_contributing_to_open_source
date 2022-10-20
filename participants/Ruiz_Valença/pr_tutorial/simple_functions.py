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

def is_prime(n):
    s = 0
    if n == 2:
        return True
    elif n == 1 or n % 2 == 0:
        return False
    else:
        for i in range(1, n+1):
            if n % i == 0:
                s += 1
        if s > 2:
            return False
        else:
            return True
