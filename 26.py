from decimal import *

def get_cycle(s):
    for j in xrange(1, len(s)/2):
        if s[:j] == s[j:j*2]:
            return j

if __name__ == '__main__':
    getcontext().prec = 2000
    answer = (0,0)
    one = Decimal(1)
    for i in xrange(1, 1000):
        part = str(one / Decimal(i))[2:]
        for k in xrange(len(part)):
            cycle = get_cycle(part[k:])
            # print part[k:], cycle
            if cycle > answer[0]:
                answer = (cycle, i)

    print answer
    print "found %s. its sequence is %s digits long" % (answer[1], answer[0])
    print one / Decimal(answer[1])
