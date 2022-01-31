import sys
from collections import Counter

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
cnt = dict(zip(sorted(Counter(arr).keys()), range(len(Counter(arr).keys()))))
for num in arr:
    print(cnt[num], end=' ')