import sys
for _ in range(int(sys.stdin.readline())):
    x1,y1,r1,x2,y2,r2 = map(int, sys.stdin.readline().rstrip().split())
    dist = (abs(x1-x2)**2+abs(y1-y2)**2)**0.5
    
    if dist == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if r1+r2 > dist:
            print(2)
        elif r1+r2 == dist:
            print(1)
        else:
            print(0)