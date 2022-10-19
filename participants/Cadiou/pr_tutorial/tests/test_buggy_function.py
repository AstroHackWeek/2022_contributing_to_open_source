from pr_tutorial.buggy_function import angle_to_sexigesimal

def test_angle_to_sexigesimal():
    inputs = [0, 90, 180, 270, 360]
    outputs = ['0:0:0.000', '6:0:0.000', '12:0:0.000', '18:0:0.000', '24:0:0.000']

    for inp, out in zip(inputs, outputs):
        assert angle_to_sexigesimal(inp) == out
