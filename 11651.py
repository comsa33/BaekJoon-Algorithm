import sys

N = int(sys.stdin.readline())
cords = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
cords.sort(key=lambda x: (x[1], x[0]))
for cord in cords:
    print(cord[0], cord[1])