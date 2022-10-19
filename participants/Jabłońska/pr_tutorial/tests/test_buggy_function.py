from pr_tutorial.buggy_function import angle_to_sexigesimal


def test_angle_to_sexigesimal_zero():
    assert angle_to_sexigesimal(0.0) == '0:0:0.000'


def test_angle_to_sexigesimal_positive():
    assert angle_to_sexigesimal(10.0) == '0:40:0.000'
    
    
def test_angle_to_sexigesimal_positive():
    assert angle_to_sexigesimal(-10.0) == '-0:40:0.000'
    
    
def test_angle_to_sexigesimal_over_180():
    assert angle_to_sexigesimal(275.60) == '18:22:24.000'
    
    
def test_angle_to_sexigesimal_over_180_negative():
    assert angle_to_sexigesimal(-275.60) == '-18:22:24.000'