from pr_tutorial.simple_functions import factorial, is_prime


def test_factorial_3():
    """Simplest test for one crete case"""

    assert factorial(3) == 6


def test_is_prime_returns_true_for_1():
    assert is_prime(1) == False

def test_is_prime_returns_true_for_2():
    assert is_prime(2) == True
    

def test_is_prime_returns_true_for_3():
    assert is_prime(3) == True
    

def test_is_prime_returns_false_for_4():
    assert is_prime(4) == False