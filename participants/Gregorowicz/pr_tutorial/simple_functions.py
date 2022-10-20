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


def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True