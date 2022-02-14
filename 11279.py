import sys
import heapq

li = []
heapq.heapify(li)

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    for _ in range(N):
        x = int(sys.stdin.readline())
        if x == 0:
            try:
                print(abs(heapq.heappop(li)))
            except IndexError:
                print(x)
        else:
            heapq.heappush(li, -x)

