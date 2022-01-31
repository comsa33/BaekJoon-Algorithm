import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
cnt = dict(zip(sorted(set(arr)), range(len(set(arr)))))
for num in arr:
    print(cnt[num], end=' ')