import math


def solve(a, b, c):
    eps = 1e-7

    for i in [a, b, c]:
        if not isinstance(i, (int, float)) or i in [math.inf, math.nan]:
            raise TypeError

    if math.isclose(a, 0.0, abs_tol=eps):
        raise Exception

    D = b**2 - 4*a*c

    if math.isclose(D, 0.0, abs_tol=eps):
        return [-b / (2 * a)]

    if D > eps:
        return [
            (-b+math.sqrt(D))/(2*a),
            (-b-math.sqrt(D))/(2*a)
        ]
    elif D < -eps:
        return []
