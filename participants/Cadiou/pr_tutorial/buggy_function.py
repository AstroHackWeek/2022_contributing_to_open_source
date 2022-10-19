import math
from numbers import Integral


def angle_to_sexigesimal(angle_in_degrees: float, decimals: int=3) -> str:
    """
    Convert the given angle to a sexigesimal string of hours of RA.

    Parameters
    ----------
    angle_in_degrees : float
        A scalar angle, expressed in degrees
    decimals : int, optional
        The number of decimals to use in the output string, by default 3

    Returns
    -------
    hms_str : str
        The sexigesimal string giving the hours, minutes, and seconds of RA for
        the given `angle_in_degrees`

    """
    if not isinstance(decimals, Integral):
        raise OSError('decimals should be an integer!')

    hours_num = angle_in_degrees*24/360
    hours = math.floor(hours_num)

    min_num = (hours_num - hours)*60
    minutes = math.floor(min_num)

    seconds = (min_num - minutes)*60

    format_string = '{}:{}:{:.' + str(decimals) + 'f}'
    return format_string.format(hours, minutes, seconds)
