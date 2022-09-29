from collections import defaultdict


class Polynomial(object):
    """
    Polynomial symbolic representation.
    """
    def __init__(self, coef=None):
        if coef is not None:
            self.coef = defaultdict(int, coef)
        else:
            self.coef = defaultdict(int)

    def __add__(self, other):
        result = self
        for j, b in other.coef.items():
            result.coef[j] += b
        return result

    def __mul__(self, other):
        result = Polynomial()
        for i, a in self.coef.items():
            for j, b in other.coef.items():
                result.coef[i + j] += a * b
        return result
