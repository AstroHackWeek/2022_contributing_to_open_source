from pr_tutorial.simple_functions import factorial, is_prime
import pytest

def test_factorial():
    inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    outputs = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

    for inp, out in zip(inputs, outputs):
        assert factorial(inp) == out

def test_factorial_invalid():
    with pytest.raises(ValueError):
        factorial(-1)

def test_factorial_invalid_type():
    with pytest.raises(TypeError):
        factorial('a')

def test_is_prime():
    inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    outputs = [False, True, True, False, True, False, True, False, False, False]

    for inp, out in zip(inputs, outputs):
        assert is_prime(inp) is out