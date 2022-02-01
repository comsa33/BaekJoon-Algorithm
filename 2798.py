import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().rstrip().split())
cards = list(map(int, sys.stdin.readline().rstrip().split()))

print(max(list(map(sum, list(filter(lambda x: sum(x) <= M, list(combinations(cards, 3)))))))
)