import sys

while True:
    first, second = map(int, sys.stdin.readline().rstrip().split())
    if (first, second) == (0, 0):
        break
    else:
        if first%second == 0:
            print('multiple')
        elif second%first == 0:
            print('factor')
        else:
            print('neither')