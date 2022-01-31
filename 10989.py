import heapq
import sys
# from collections import Counter

# def solution(n):
#     arr = [sys.stdin.readline().rstrip() for num in range(n)]
#     cnt = Counter(arr)
#     nums = sorted(cnt.keys())
#     for num in nums:
#         for i in range(cnt[num]):
#             print(num)

def solution(n):
    arr = [sys.stdin.readline().rstrip() for num in range(n)]
    heapq.heapify(arr)
    for i in range(len(arr)):
        print(heapq.heappop(arr))

if __name__ == '__main__':
    N = int(input())
    solution(N)
