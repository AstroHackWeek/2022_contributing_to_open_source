def fibonacci(max):
    """
    Input: an integer value
    Output: the list of fibonacci numbers that are not greater than the input value
    """
    if type(max) != int:
        raise ValueError('max value should be integer')
    if max < 1:
        raise ValueError('max value should be more than 1')
    values = [0, 1]
    while values[-2] + values[-1] <= max:
        values.append(values[-2] + values[-1])
    return values


def factorial(value):
    if value == 0:
        return 1
    else:
        return value * factorial(value - 1)
