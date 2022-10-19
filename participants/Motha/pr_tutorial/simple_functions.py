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

 

def is_Prime(value):
    if(value==1):
        return False
    if(value==2):
        return True
    if(value%2==0):
        return False

    i = 3

    while(i<math.sqrt(value)+1):
        if value%i==0:
            return False
        i += 2
    return True
