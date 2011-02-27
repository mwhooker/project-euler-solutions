import itertools
denominations = (1, 2, 5, 10, 20, 50, 100, 200)

subdenom = []

combinations = 0

for i in denominations:
    for n in xrange(200 / i):
        subdenom.append(i)

# N^N approach

for j in xrange(1, 201):
    for k in itertools.combinations(subdenom, r=j):
        if sum(k) == 200:
            combinations += 1


print combinations
