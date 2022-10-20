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
    
def is_prime(value):
    """Checks if a value is an integer then if it is 
    a prime number or not."""
    while True:
        try:
            val = int(value)
        except ValueError:
            print("Error! Only input integers!")
            break
        else:
            if value == 1:
                return False
            else:
                try:
                    for i in range(2,value):
                      if (value%i) == 0:
                        return False
                    return True
                except TypeError:
                    print("Error! Only input integers!")
                    break
            break
            
