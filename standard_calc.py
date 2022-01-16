from math import fmod


def bound_to_180(angle):
    """Bounds the provided angle between [-180, 180) degrees.

    Args:
        angle (float): The input angle in degrees.

    Returns:
        float: The bounded angle in degrees.
    """

    angle = fmod(angle + 180, 360)
    if angle < 0:
        angle += 360
    return angle - 180


def is_angle_between(first_angle, middle_angle, second_angle):
    """Determines whether an angle is between two other angles.

    Args:
        first_angle (float): The first bounding angle in degrees.
        middle_angle (float): The angle in question in degrees.
        second_angle (float): The second bounding angle in degrees.

    Returns:
        bool: True when `middle_angle` is not in the reflex angle of `first_angle` and `second_angle`, false otherwise.
    """

    f = bound_to_180(first_angle)
    m = bound_to_180(middle_angle)
    s = bound_to_180(second_angle)

    f, s = sorted((f, s))
    if f - s > 180:
        [f, m, s] = [f, m, s].map(lambda x: -x)
    return f < m < s
