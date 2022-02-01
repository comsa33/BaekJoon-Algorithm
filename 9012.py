import sys
from collections import Counter

K = int(sys.stdin.readline())
result  = []
for _ in range(K):
    s = sys.stdin.readline().rstrip()
    cnt = Counter(s)
    if len(list(cnt.values())) > 1:
        if list(cnt.values())[0] == list(cnt.values())[1] and s[-1] != '(':
            result.append('YES')
        else:
            result.append('NO')
    else:
        result.append('NO')

for ans in result:
    print(ans)
        