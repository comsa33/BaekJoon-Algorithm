import sys
N = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
new_m = 0
ans = 0
for m in arr:
    new_m += m
    ans += new_m
print(ans)