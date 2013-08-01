from collections import Counter
from itertools import takewhile
import sys, re

t = []
for s in sys.stdin:
    s = re.sub(r'''['"].*''', '', s)
    s = re.sub(r' (for|to|is|at|from|then).*', '', s)
    s = re.sub(r' [0-9].*', '', s)
    s = re.sub(r' c[0-9a-f\?]{2}.*', '', s)
    s = re.sub(r'\s+$', '', s)
    t.append(s)

for s, c in Counter(t).most_common():
    print '%d\t"%s"' % (c, s)
