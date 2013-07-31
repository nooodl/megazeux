from collections import Counter
from itertools import takewhile
import sys, re

def token(s):
    if re.search(r'[A-Z0-9\'\"\?]', s): return False
    return True

t = []
for s in sys.stdin:
    if s[0] == '*': print s.strip()
    t.append(' '.join(list(takewhile(token, s.split()))))

for s, c in Counter(t).most_common():
    print '%d\t"%s"' % (c, s)
