from decimal import *

def get_cycle(offset, s):
    for j in xrange(1, len(s)/2):
        if s[offset:j] == s[j+offset:(j*2)+offset]:
            return j
    return None

if __name__ == '__main__':
    getcontext().prec = 200
    found = []
    one = Decimal(1)
    for i in xrange(1, 1000):
        part = str(one / Decimal(i))[2:]
        for j in xrange(len(part)/2):
            cycle = get_cycle(j, part)
            if cycle:
                found.append((cycle, i))

    print found
    answer = max(found)
    print "found %s. its sequence is %s digits long" % tuple(reversed(answer))
    print one / Decimal(answer[1])
