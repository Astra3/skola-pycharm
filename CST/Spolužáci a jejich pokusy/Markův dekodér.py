def soucet(a, b, c, d):
    y = a and b and c and d
    return y


def dekoder(cy, sum2, sum1, sum0):
    a1 = soucet(1, 1, sum1, not sum0)
    a2 = soucet(not cy, 1, sum1, 1)
    a3 = soucet(cy, sum2, sum1, sum0)
    a4 = soucet(not cy, sum2, 1, sum0)
    a5 = soucet(cy, not sum2, not sum1, 1)
    a6 = soucet(cy, 1, not sum1, not sum0)
    a7 = soucet(not cy, not sum2, not sum1, not sum0)

    a = a1 or a2 or a3 or a4 or a5 or a6 or a7

    b1 = soucet(1, not sum2, sum1, not sum0)
    b2 = soucet(not cy, not sum2, 1, 1)
    b3 = soucet(not cy, 1, sum1, sum0)
    b4 = soucet(not cy, 1, not sum1, not sum0)
    b5 = soucet(cy, 1, not sum1, sum0)
    b6 = soucet(cy, not sum2, not sum1, 1)

    b = b1 or b2 or b3 or b4 or b5 or b6

    c1 = soucet(cy, not sum2, 1, 1)
    c2 = soucet(not cy, sum2, 1, 1)
    c3 = soucet(not cy, 1, 1, sum0)
    c4 = soucet(1, 1, not sum1, sum0)
    c5 = soucet(1, not sum2, not sum1, not sum0)

    c = c1 or c2 or c3 or c4 or c5

    d1 = soucet(1, sum2, sum1, not sum0)
    d2 = soucet(not cy, not sum2, sum1, 1)
    d3 = soucet(1, not sum2, sum1, sum0)
    d4 = soucet(1, sum2, not sum1, sum0)
    d5 = soucet(cy, sum2, not sum1, 1)
    d6 = soucet(1, not sum2, not sum1, not sum0)

    d = d1 or d2 or d3 or d4 or d5 or d6

    e1 = soucet(1, 1, sum1, not sum0)
    e2 = soucet(cy, not sum2, sum1, 1)
    e3 = soucet(not cy, not sum2, 1, not sum0)
    e4 = soucet(cy, sum2, not sum1, 1)
    e5 = soucet(cy, 1, not sum1, not sum0)

    e = e1 or e2 or e3 or e4 or e5

    f1 = soucet(1, sum2, sum1, not sum0)
    f2 = soucet(cy, not sum2, 1, 1)
    f3 = soucet(not cy, sum2, not sum1, 1)
    f4 = soucet(1, 1, not sum1, not sum0)

    f = f1 or f2 or f3 or f4

    g1 = soucet(1, 1, sum1, not sum0)
    g2 = soucet(cy, not sum2, 1, 1)
    g3 = soucet(not cy, not sum2, sum1, 1)
    g4 = soucet(cy, 1, 1, sum0)
    g5 = soucet(not cy, sum2, not sum1, 1)

    g = g1 or g2 or g3 or g4 or g5

    return a, b, c, d, e, f, g


print(dekoder(1, 0, 0, 0))
