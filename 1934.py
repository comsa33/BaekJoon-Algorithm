import sys

def solution(n,m):
    if n < m:
        n, m = m, n
    if n%m == 0:
        return m
    else:
        return solution(m, n%m)

for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    ans = solution(n,m)
    print(ans*(n//ans)*(m//ans))
