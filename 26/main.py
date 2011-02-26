from __future__ import division
from decimal import Decimal, getcontext
from operator import itemgetter


def find_cycle(r):
    """Find cycles


    bug: only returns the first cycle
    
    >>> find_cycle('1.666')
    '6'
    >>> find_cycle('0.14285714285714285')
    '142857'
    >>> find_cycle('0.12121234512345')
    '12345'
    >>> find_cycle('0.035714285714285712')
    '571428'
    >>> find_cycle('0.1231')
    False
    >>> find_cycle('0.1')
    False
    """
    r = str(r)
    found_cycles = []

    for i in xrange(len(r)):
        #current cycle we're looking for
        cycle = ''

        for n, c in enumerate(r[i:]):
            if len(cycle):
                #print cycle,' == ',r[i+n:][:len(cycle)]
                if cycle == r[i+n:][:len(cycle)]:
                    found_cycles.append(cycle)
                    cycle = ''
            cycle += c

    if len(found_cycles):
        data =  sorted(map(lambda x: (len(x), x), found_cycles),
                       key=itemgetter(0), reverse=True)
        return ''.join(data[0][1])
    return False

def division_cycle(n,d):
    return find_cycle(Decimal(str(n)) / Decimal(str(d)))

if __name__ == '__main__':
    getcontext().prec = 1000
    cycles = []
    for i in xrange(1, 1000):
        cycle = division_cycle(1, i)
        if cycle:
            cycles.append((i, cycle))


    data =  sorted(map(lambda x: {'len':len(x[1]), 'n': x[0], 'cycle': x[1]}, cycles),
                   key=lambda y: y['len'], reverse=True)
    print data
    print "cycle: ", data[0]['n']#''.join(data[0][1][1])
