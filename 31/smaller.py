def stupid_partition(n, p=None):
    """
    really stupid way to find number partition
    p: restrict components to this set

    >>> len(list(stupid_partition(10, [1,2,5,10])))
    11
    """
    if not p:
        accelAsc(n)
    else:
        for i in accelAsc(n):
            if set(i).issubset(set(p)):
                yield i


def integer_partitions(n, l):
    """
    from http://tardate.blogspot.com/2008/10/rolling-project-euler-on-ruby.html
    l: restrict components to this set

    10 x 1
    5 x 2
    4 x 2; 2 x 1
    3 x 2; 4 x 1
    2 x 2; 6 x 1
    1 x 2; 8 x 1
    >>> integer_partitions(10, [1, 2])
    6
    >>> integer_partitions(10, [1, 2, 5, 10])
    11
    >>> integer_partitions(200, [1, 2, 5, 10, 20, 50, 100, 200])
    73682
    """
    l = sorted(l, reverse=True)
    def partition(n, p):
        """
        def integer_partitions(pArray, p=0)  
            if p==pArray.length-1  
              1  
            else  
              self >= 0 ? (self - pArray[p]).integer_partitions(pArray ,p) + self.integer_partitions(pArray,p+1) : 0 
            end  
        end  
        """
        if p == len(l) - 1:
            return 1
        else:
            if n >= 0:
                return partition(n-l[p], p) + partition(n, p+1)
            else:
                return 0
    return partition(n, 0)


def accelAsc(n):
    """number partition generator
    from http://homepages.ed.ac.uk/jkellehe/partitions.php

    >>> len(list(accelAsc(10)))
    42
    """
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2*x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]


partitions = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
def pent(n):
    return (n*(3*n - 1))/2

def gen_pent(n):
    if n%2:
        i = (n + 1)/2
    else:
        i = -n/2
    return pent(i)

def partition(n):
    """http://stackoverflow.com/questions/3164305/optimizing-a-partition-function
    
    >>> partition(10)
    42
    >>> partition(200)
    3972999029388
    """
    try:
        return partitions[n]
    except IndexError:
        total, sign, i = 0, 1, 1
        k = gen_pent(i)
        while n - k >= 0:
            total += sign*partition(n - k)

            i += 1
            if i%2: sign *= -1
            k = gen_pent(i)

        partitions.insert(n, total)
        return total

if __name__ == '__main__':
    denominations = (1, 2, 5, 10, 20, 50, 100, 200)
    n = 200

    print integer_partitions(n, denominations)
