import sys

def fiv0(n, memo={}):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fiv0(n-2, memo)+fiv0(n-1, memo)
    return memo[n]

def fiv1(n, memo={}):
    if n == 0:
        return 1
    if n == 1:
        return 0
    if n in memo:
        return memo[n]
    memo[n] = fiv1(n-2, memo)+fiv1(n-1, memo)
    return memo[n]

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline().rstrip())
        print(fiv1(n), fiv0(n))
        