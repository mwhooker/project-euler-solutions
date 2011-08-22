from __future__ import division
from collections import defaultdict

found = defaultdict(list)


for i in xrange(1, 100):
    for j in xrange(1, 100):
        div = i / j
        found[str(div)].append(("%s/%s" % (i, j), len(str(i)) == 1 and
                                len(str(j)) == 1))

print [found[key] for key in found if len(found[key]) > 1]
