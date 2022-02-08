from itertools import combinations
import sys

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

diff = list(map(lambda x: abs(x[0]-x[1]), combinations(arr, 2)))
min_diff = min(diff)
ans = []
for i in range(2, min_diff+1):
    if min_diff%i == 0:
        ans.append(str(i))
print(' '.join(ans))