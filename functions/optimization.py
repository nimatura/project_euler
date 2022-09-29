from decimal import Decimal


def newton_raphson(f, df, x0=0, max_iter=None, tol=None):
    """
    Newton-Raphson method using Decimals for greater precision.
    """
    iteration = 0
    xn = Decimal(x0)
    while True:
        if max_iter is not None and iteration == max_iter:
            break
        xn -= Decimal(f(xn)) / Decimal(df(xn))
        if tol is not None and abs(f(xn)) < tol:
            break
        iteration += 1
    return xn
