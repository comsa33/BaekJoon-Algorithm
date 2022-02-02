# import sys
# N = int(sys.stdin.readline())
# arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

# output = [0]*N
# count = [0]*(max(arr)+1)
# # count numbers in the given array
# for i in range(N):
#     count[arr[i]] += 1
# for i in range(1, max(arr)+1):
#     count[i] += count[i-1]
# i = N-1
# while i >= 0:
#     output[count[arr[i]]-1] = arr[i]
#     count[arr[i]] -= 1
#     i -= 1
# for num in output:
#     print(num)   


import sys
from collections import Counter

def solution(n):
    arr = (int(sys.stdin.readline().rstrip()) for num in range(n)) # [1,1.....1]
    cnt = Counter(arr) # {1:100} {h:1, e:1, l:2, o:1}
    nums = sorted(cnt.keys()) # [1,2,3,5]
    for num in nums:
        for i in range(cnt[num]):
            print(num)

if __name__ == '__main__':
    N = int(input())
    solution(N)