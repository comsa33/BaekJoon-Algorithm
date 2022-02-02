import sys
from collections import deque

que = deque()
for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().rstrip().split()
    if len(command) > 1:
        que.append(command[1])
    else:
        command = command[0]
        if command == 'pop': 
            if len(que) > 0:
                print(que.popleft())
            else:
                print(-1)
        elif command == 'size':
            print(len(que))
        elif command == 'empty':
            if len(que) == 0:
                print(1)
            else:
                print(0)
        elif command == 'front':
            if len(que) > 0:
                print(que[0])
            else:
                print(-1)
        elif command == 'back':
            if len(que) > 0:
                print(que[-1])
            else:
                print(-1)