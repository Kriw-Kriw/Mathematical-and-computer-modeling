# параметры ламме l1 и h1
def l1(v, E):
    return (v * E) / ((1 + v) * (1 - 2 * v))


def h1(v, E):
    return E / (2 * (1 + v))


# Константы интегрирования C1 и C2
def C1(a, b, qa, qb, l1, h1):
    return ((qb * (b * b) - qa * (a * a)) / (2 * (l1 + h1) * (a * a - b * b)))


def C2(a, b, qa, qb, h1):
    return ((qb - qa) * (a * a) * (b * b)) / ((2 * h1) * (a * a - b * b))

# поле перемещения
def U_r(r, C1, C2):
    return [(C1 * r + C2 * (1 / r)) for r in r]

# поле напряжения
def Or_r(r, a, b, qa, qb):
    return [
        (qa * a * a * (r * r - b * b)) / (r * r * (b * b - a * a)) + (qb * b * b * (a * a - r * r)) / (
                r * r * (b * b - a * a))
        for r in r
    ]

# поле напряжения
def Oo_r(r, a, b, qa, qb):
    return [
        (qa * a * a * (r * r + b * b)) / (r * r * (b * b - a * a)) - (qb * b * b * (r * r + a * a)) / (
                r * r * (b * b - a * a))
        for r in r
    ]
