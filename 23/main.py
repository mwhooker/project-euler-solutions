def is_perfect(num):
    """A perfect number is a number for which the sum of its proper divisors is
    exactly equal to the number.
    
    >>> is_perfect(28)
    True
    >>> is_perfect(3)
    False
    """
    divisors = proper_divisors(num)

    if sum(divisors) == num:
        return True
    return False

def proper_divisors(num):
    """return list of proper divisors. empty list if prime

    >>> proper_divisors(1)
    []
    >>> proper_divisors(2)
    [1]
    >>> proper_divisors(3)
    [1]
    >>> proper_divisors(28)
    [1, 2, 4, 7, 14]
    >>> proper_divisors(15)
    [1, 3, 5]

    """

    divisors = []
    for i in xrange(1, floor(num/2)+1):
        if (num % i) == 0:
            divisors.append(i)

    return divisors

def is_deficient(num):
    """A number n is called deficient if the sum of its proper divisors is less
    than n.
    
    >>> is_deficient(3)
    True
    >>> is_deficient(12)
    False
    """
    return sum(proper_divisors(num)) < num

def is_abundant(num):
    """A number n is called abundant if the sum of its proper divisors is
    greater than n.

    >>> is_abundant(3)
    False
    >>> is_abundant(12)
    True
    """
    return sum(proper_divisors(num)) > num

"""
By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. 
...
Find the sum of all the positive integers which cannot be written as the sum
of two abundant numbers."""

targets = set()
upper = 28123
#upper = 20

abundant_numbers = set()

for i in xrange(upper+1):
    if is_abundant(i):
        abundant_numbers.add(i)

abundant_sums = set()
for i in abundant_numbers:
    for j in abundant_numbers:
        abundant_sums.add(i+j)

for i in xrange(1, upper+1):
    if i not in abundant_sums:
        targets.add(i)
print sum(targets)
