import math


def solve(a, b, c):
    for i in [a, b, c]:
        if not isinstance(i, (int, float)):
            raise TypeError

    if math.isclose(a, 0.0):
        raise Exception

    D = b**2 - 4*a*c

    if D > 0:
        return [
            (-b+math.sqrt(D))/(2*a),
            (-b-math.sqrt(D))/(2*a)
        ]
    elif D < 0:
        return []
    else:
        return [-b/(2*a)]

