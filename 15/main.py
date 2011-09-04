from itertools import izip


def find_answer(x, y=None):
    """

    >>> find_answer(2)
    6
    >>> find_answer(3)
    20
    """

    if not y:
        y = x

    if y != x:
        raise Exception("the case where y != x is not supported yet")

    edges = x + 1

    answer = 0
    for (i,j)  in izip(xrange(1, edges+1), xrange(edges, 0, -1)):
        answer += i * j 

    return answer
