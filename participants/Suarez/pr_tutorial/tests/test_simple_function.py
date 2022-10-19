from pr_tutorial.simple_functions import factorial, prime


def test_factorial_3():
    """Simplest test for one create case"""

    assert factorial(3) == 6


def test_prime():
  """Simplest test for one create case"""

  assert prime(3) == True
  assert prime(2) == False
