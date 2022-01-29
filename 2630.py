import sys

N = int(sys.stdin.readline())

arr = [sys.stdin.readline().rstrip().split() for _ in range(N)]

def solution(arr):
    arr_str = ''.join([''.join(line) for line in arr])
    if len(arr) == 1:
        return arr[0][0]
    elif arr_str == '1'*len(arr)**2:
        return '1'
    elif arr_str == '0'*len(arr)**2:
        return '0'

    else:
        mid = len(arr)//2
        up_left = solution([line[:mid] for line in arr[:mid]])
        up_right = solution([line[mid:] for line in arr[:mid]])
        dw_left = solution([line[:mid] for line in arr[mid:]])
        dw_right = solution([line[mid:] for line in arr[mid:]])
        arr_str = up_left+up_right+dw_left+dw_right

        return arr_str

result = solution(arr)
print(result.count('0'))
print(result.count('1'))