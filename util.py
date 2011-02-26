from __future__ import division


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
