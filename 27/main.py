import math
from pyecm import isprime

def process(a, b):
    primes = 0
    n = 0
    while isprime(n**2 + (a * n) + b):
        primes += 1
        n += 1
    return primes


if __name__ == '__main__':

    results = []
    for a in xrange(-1000, 1001):
        for b in xrange(-1000, 1001):
            results.append((process(a, b), a, b))
    p, ca, cb = max(results, key=lambda x: x[0])
    print ca * cb
