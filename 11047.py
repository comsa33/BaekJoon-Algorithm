import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

coins = sorted(list(filter(lambda x: x<=K, [int(sys.stdin.readline().rstrip()) for _ in range(N)])), reverse=True)
wallet = {}
for coin in coins:
    no_coin = K//coin
    wallet[coin] = no_coin
    K -= coin*no_coin
    if K == 0:
        break
print(sum(wallet.values()))
