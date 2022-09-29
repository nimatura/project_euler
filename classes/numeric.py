from collections import defaultdict
from functions.divisibility import get_prime_factors


class PrimeDecomposition(object):
    """
    Prime factorization representation of a natural number.
    """
    def __init__(self, n):
        if isinstance(n, int):
            self.prime_factors = get_prime_factors(n)
        elif isinstance(n, defaultdict):
            self.prime_factors = n
        else:
            raise ValueError('n must be an int or defaultdict object')

    def __mul__(self, other):
        mul_factors = defaultdict(int)
        for p in self.prime_factors.keys():
            mul_factors[p] += self.prime_factors[p]
        for p in mul_factors.keys():
            mul_factors[p] += other.prime_factors[p]
        return PrimeDecomposition(mul_factors)

    def __div__(self, other):
        div_factors = defaultdict(int)
        for p in self.prime_factors.keys():
            div_factors[p] += self.prime_factors[p]
        for p in div_factors.keys():
            div_factors[p] -= other.prime_factors[p]
            if div_factors[p] < 0:
                raise ValueError('p is not divisible by q')
        return PrimeDecomposition(div_factors)

    def __pow__(self, power, modulo=None):
        pow_factors = defaultdict(int)
        for p, q in self.prime_factors.items():
            pow_factors[p] = q * power
        return PrimeDecomposition(pow_factors)

    def __eq__(self, other):
        return self.prime_factors == other.prime_factors

    def get_product(self):
        product = 1
        for p in self.prime_factors.keys():
            product *= p ** self.prime_factors[p]
        return product


class RationalNumber(object):
    """
    Fractional representation of a rational number. Comes with simplification utility.
    """
    def __init__(self, p, q=None):
        self.p = p
        self.q = q if q else 1

    def __neg__(self):
        return RationalNumber(-self.p, self.q)

    def __add__(self, other):
        new_p = self.p * other.q + self.q * other.p
        new_q = self.q * other.q
        return RationalNumber(new_p, new_q)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        new_p = self.p * other.p
        new_q = self.q * other.q
        return RationalNumber(new_p, new_q)

    def __div__(self, other):
        new_p = self.p * other.q
        new_q = self.q * other.p
        return RationalNumber(new_p, new_q)

    def __truediv__(self, other):
        return self.__div__(other)

    def __pow__(self, power, modulo=None):
        new_p = self.p ** power
        new_q = self.q ** power
        return RationalNumber(new_p, new_q)

    def __str__(self):
        return '%i / %i' % (self.p, self.q)

    def __eq__(self, other):
        return self.p * other.q == self.q * other.p

    def __ne__(self, other):
        return self.p * other.q != self.q * other.p

    def __lt__(self, other):
        return self.p * other.q < self.q * other.p

    def __gt__(self, other):
        return self.p * other.q > self.q * other.p

    def __le__(self, other):
        return self.p * other.q <= self.q * other.p

    def __ge__(self, other):
        return self.p * other.q >= self.q * other.p

    def simplify(self):
        p_decomposition = PrimeDecomposition(self.p)
        q_decomposition = PrimeDecomposition(self.q)
        for k in p_decomposition.prime_factors.keys():
            if k in q_decomposition.prime_factors.keys():
                common_power = min(p_decomposition.prime_factors[k], q_decomposition.prime_factors[k])
                p_decomposition.prime_factors[k] -= common_power
                q_decomposition.prime_factors[k] -= common_power
        new_p = p_decomposition.get_product()
        new_q = q_decomposition.get_product()
        return RationalNumber(new_p, new_q)

    def get_division(self):
        return self.p / self.q
    
    
class BinaryNumber(object):
    """
    Binary representation of a natural number
    """
    def __init__(self, n):
        if isinstance(n, int):
            self.bin = self.get_binary_representation(n)
        elif isinstance(n, str):
            self.bin = n
        else:
            raise ValueError('n must be an int or str')
        
    @staticmethod
    def get_binary_representation(n):
        powers_of_two = []
        rest = n
        digits = ''
        i = 0
        while True:
            power_of_two = 2 ** i
            if power_of_two > rest:
                break
            else:
                powers_of_two.append(power_of_two)
            i += 1
        digits += '1'
        rest -= powers_of_two[-1]
        for power_of_two in powers_of_two[::-1][1:]:
            if rest >= power_of_two:
                digits += '1'
                rest -= power_of_two
            else:
                digits += '0'
        return digits[::-1]
