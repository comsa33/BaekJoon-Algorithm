import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
if len(arr) == 1:
    print(arr[0]**2)
else:
    print(min(arr)*max(arr))