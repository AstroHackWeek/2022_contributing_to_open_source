from pr_tutorial.buggy_function import angle_to_sexigesimal



def test_angle_to_sexigesimal_len():
    """ A simple test that the length of the angle string is correct (HH:mm:ss.sss)  """

    assert len(angle_to_sexigesimal(30)) == 12
    #The length must be 12 if the string is formatted correctly with 3 decimal places and leading zeros


def test_seconds_60():

    assert angle_to_sexigesimal(350)[-6] == '0'
    #For 350 degrees, the tens digit of the seconds should be 0, not 6

def test_angle_wrapping():

    assert angle_to_sexigesimal(370)[0:2] == '00'

def test_angle_wrapping_negative():

    assert angle_to_sexigesimal(-10)[0:2] == '24'
