import math

def divisors(n):
    divisors = set()
    n = int(n)
    max = int(math.floor(math.sqrt(n)))
    for i in xrange(1, max+1):
        if (n % i) is 0:
            divisors.add(i)
            divisors.add(n/i)
    return divisors 
    #factors = ecm.factors(number, False, True, 10, 1)


class Triangle(object):
    memo = [(0,0)]
    def __init__(self, n):
        self.n = n
        last = max(self.memo)
        prev = last[0]
        start = last[1]
        #print "n, start, prev: (%s, %s, %s)" % (n, start, prev)
        self.tn = reduce(lambda x,y: x+y, xrange(prev+1, n+1), start)
        self.memo.append((n, self.tn))

    def __int__(self):
        return self.tn

    def __repr__(self):
        return "<Triangle %d> %d" % (self.n, self.tn)

n = 1
while True:
    tn = Triangle(n)
    if len(divisors(tn)) > 500:
        print tn
        exit(0)
    n += 1

exit(1)
