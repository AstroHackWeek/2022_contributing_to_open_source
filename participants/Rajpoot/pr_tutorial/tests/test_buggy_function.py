from pr_tutorial.buggy_function import angle_to_sexagesimal

def test_angle_to_sexigesimal():
    """Simplest test for one case"""

    assert angle_to_sexagesimal(66.8, decimals=3) == '66° 48′ 0″'
