from pr_tutorial.buggy_function import angle_to_sexigesimal

def test_buggy_function():

    assert angle_to_sexigesimal(180) == '12:0:0.000'
