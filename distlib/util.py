from __future__ import division
import math


def is_palindrome(i):
    """is the string representation of i a palindrome?
    
    >>> is_palindrome('is not')
    False
    >>> import re
    >>> is_palindrome(''.join(re.findall('[a-z]', 'a man, a plan, a canal: panama')))
    True
    """
    s = str(i)
    return s == s[::-1]



class Spiral(object):
    """

    Spiral(n=9)
        789
        612
        543

    Spiral(side=5)
        21 22 23 24 25
        20  7  8  9 10
        19  6  1  2 11
        18  5  4  3 12
        17 16 15 14 13
    """

    def __init__(self, n=None, side=None):

        if n:
            if (25 ** .5 % 1) != 0:
                raise ValueError('n must be square!')
            self._spiral = self._spiral_to(n)
        elif side:
            self._spiral = self._spiral_to(side**2)
        else:
            raise ValueError('n or side needs to be specified')

    def _spiral_to(self, n):
        side = n ** .5
        spiral = []
        for i in xrange(n):
            spiral.append([])
            for j in xrange(n):
                spiral[i].append(0)

        col = 0
        row = 0
        for i in xrange(1, n+1):
            spiral[row][col] = i
        raise NotImplementedError


    def __str__(self):
        return str(self._spiral)
