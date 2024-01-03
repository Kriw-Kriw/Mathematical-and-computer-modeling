# параметры ламме l1 и h1
def l1(v, E):
    return (v * E) / ((1 + v) * (1 - 2 * v))


def h1(v, E):
    return E / (2 * (1 + v))


# Константы интегрирования C1 и C2
def C1(a, b, qa, qb, l1, h1):
    return (qb * b * b * b - qa * a * a * a) / ((3 * l1 + 2 * h1) * (a * a * a - b * b * b))


def C2(a, b, qa, qb, h1):
    return ((qa - qb) * a * a * a * b * b * b) / ((4 * h1) * (b * b * b - a * a * a))


#поле перемещения
def U_r(r, C1, C2):
    return [(C1 * r + C2 * (1 / (r * r))) for r in r]


# def U_r(r, a, b, qa, qb, l1, h1):
#      return [(qb * b * b * b - qa * a * a * a) / ((3 * l1 + 2 * h1) * (a * a * a - b * b * b)) * r + ((qa - qb) * a * a * a * b * b * b) / (4 * h1 * (b * b * b - a * a * a) * r * r) for r in r]


# поле напряжения
def Or_r(r, a, b, qa, qb):
    return [
        (qa * a * a * a * (r * r * r - b * b * b)) / (r * r * r * (b * b * b - a * a * a)) +
        (qb * b * b * b * (a * a * a - r * r * r)) / (r * r * r * (b * b * b - a * a * a))
        for r in r
    ]


# поле напряжения
def Oo_r(r, a, b, qa, qb):
    return [
        (qa * a * a * a * (2 * r * r * r + b * b * b)) / (2 * r * r * r * (b * b * b - a * a * a)) -
        (qb * b * b * b * (2 * r * r * r + a * a * a)) / (2 * r * r * r * (b * b * b - a * a * a))
        for r in r
    ]