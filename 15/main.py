"""
https://en.wikipedia.org/wiki/Lattice_path
https://en.wikipedia.org/wiki/Combination

"""
from __future__ import division
from decimal import Decimal
from math import factorial

def combinations(n, k):
    """the combination of n things taken k at a time without repetition."""
    return factorial(n) / Decimal(factorial(k) * factorial(n - k))

def ne_lattice_paths(k):
    """The number of NE lattice paths from  (0,0)  to  (a,b)  counts the number
    of combinations of  a  objects out of a set of  a + b  objects.

    """
    return combinations(k + k, k)

if __name__ == '__main__':
    ne_lattice_paths(3)
    print "2x2 = %s" % ne_lattice_paths(2)
    print "20x20 = %s" % ne_lattice_paths(20)
