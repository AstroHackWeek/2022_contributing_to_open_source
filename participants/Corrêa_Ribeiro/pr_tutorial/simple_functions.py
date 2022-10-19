def fibonacci(max:int) -> int:
    values = [0, 1]
    while values[-2] + values[-1] < max:
        values.append(values[-2] + values[-1])
    return values


def factorial(value: int) -> int:
    if value == 0:
        return 1
    else:
        return value * factorial(value - 1)


def is_prime(num:int) -> int:
    sum_of_divisors = 0

    if n == 2:
        return True
    elif n == 1 or n % 2 == 0:
        return False

    for n in range(1, n+1):
        if num % n == 0:
            sum_of_divisors += 1

    return sum_if_divisors <= 2
