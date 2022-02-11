import sys

def solution(coins, m, cnt=0):
    if m < min(coins):
        return cnt
    if m in coins:
        cnt += 1
        return cnt
    else:
        for coin in coins:
            if m-coin > 0:
                cnt += solution(coins, m-coin, cnt)
        return cnt


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        coins = list(map(int, sys.stdin.readline().rstrip().split()))
        m = int(sys.stdin.readline())
        print(solution(coins, m))


