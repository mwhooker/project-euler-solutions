
def is_power_sum(number, pow):
    """True if the number can be written as the sum of `pow` powers of its
    digits.

    >>> is_power_sum(1634, 4)
    True
    >>> is_power_sum(1, 4)
    False
    >>> is_power_sum(1234, 4)
    False
    """

    if len(str(number)) <= 1:
        return False
    sum = 0
    for digit in str(number):
        sum += int(digit) ** pow

    return sum == number



"""
max number:
    9^5 = 59049
    9^5 * 5 = 295245
    9^5 * 6 = 354294
"""
print sum([i for i in xrange(1, 354294) if is_power_sum(i, 5)])
