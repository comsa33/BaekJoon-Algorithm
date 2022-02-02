import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
def solution(n,m):
    if n < m:
        n, m = m, n
    if n%m == 0:
        return m
    else:
        return solution(m, n%m)

ans1 = solution(n,m)
print(ans1)
print(ans1*(n//ans1)*(m//ans1))