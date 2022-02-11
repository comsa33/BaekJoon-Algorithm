import sys
from itertools import permutations

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().rstrip().split())
    for x in permutations(range(1, N+1), M):
        print(*x)