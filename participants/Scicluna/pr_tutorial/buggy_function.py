import math


def angle_to_sexigesimal(angle_in_degrees, decimals=3):
    """
    Convert the given angle to a sexigesimal string of hours of RA.

    Parameters
    ----------
    angle_in_degrees : float
        A scalar angle, expressed in degrees

    Returns
    -------
    hms_str : str
        The sexigesimal string giving the hours, minutes, and seconds of RA for
        the given `angle_in_degrees`

    """
    if math.floor(decimals) != decimals:
        raise OSError('decimals should be an integer!')

    #convert angle to half-open interval range [0,360)
    angle_in_degrees %= 360

    hours_num = angle_in_degrees*24/360
    hours = math.floor(hours_num)

    min_num = (hours_num - hours)*60
    minutes = math.floor(min_num)

    seconds = round((min_num - minutes)*60, decimals)

    if round(seconds, decimals) >= 60:
        minutes+=1
        seconds-=60

    if minutes > 59:
        hours+=1
        minutes-=60

    format_string = '{0:02d}:{1:02d}:{2:0'+str(3+decimals)+ '.' + str(decimals) + 'f}'
    return format_string.format(hours, minutes, seconds)
