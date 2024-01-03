# параметр ламме h1
def h1(v, E):
    return E / (2 * (1 + v))


# поле перемещения
def U_r(r, a, b, qa, qb, h1):
    return [((qb - qa) / (2 * h1)) * ((a * a * b * b) / (a * a - b * b)) * (1 / r) for r in r]


# поле напряжения
def Or_r(r, a, b, qa, qb):
    return [(qb - qa) * (b * b) / (a * a - b * b) * (1 - (a * a) / (r * r)) - qa for r in r]


# поле напряжения
def Oo_r(r, a, b, qa, qb):
    return [(qb - qa) * (b * b) / (a * a - b * b) * ((a * a) / (r * r) + 1) - qa for r in r]
