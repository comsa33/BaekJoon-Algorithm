import sys

K, N = map(int, sys.stdin.readline().rstrip().split())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(K)]

# max_len = sum(arr)//N
max_len = min(list(map(lambda x: x//round(N*x/sum(arr)), arr)))
while True:
    if sum(list(map(lambda x: x//max_len, arr))) >= N:
        print(max_len)
        break
    max_len -= 1