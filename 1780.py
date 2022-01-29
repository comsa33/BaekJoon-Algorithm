import sys
import re

N = int(sys.stdin.readline())

arr = [sys.stdin.readline().rstrip().split() for _ in range(N)]

def solution(arr):
    if len(arr) == 3:
        arr_str = ''.join([''.join(line) for line in arr])

        if arr_str == '1'*9:
            return '1'
        elif arr_str == '0'*9:
            return '0'
        elif arr_str =='-1'*9:
            return '-1'
        else:
            return arr_str
    else:
        mid = len(arr)//3
        up_left = solution([line[:mid] for line in arr[:mid]])
        up_mid = solution([line[mid:mid*2] for line in arr[:mid]])
        up_right = solution([line[mid*2:] for line in arr[:mid]])
        mid_left = solution([line[:mid] for line in arr[mid:mid*2]])
        mid_mid = solution([line[mid:mid*2] for line in arr[mid:mid*2]])
        mid_right = solution([line[mid*2:] for line in arr[mid:mid*2]])
        dw_left = solution([line[:mid] for line in arr[mid*2:]])
        dw_mid = solution([line[mid:mid*2] for line in arr[mid*2:]])
        dw_right = solution([line[mid*2:] for line in arr[mid*2:]])
        arr_str = up_left+up_mid+up_right+mid_left+mid_mid+mid_right+dw_left+dw_mid+dw_right

        if arr_str == '1'*9:
            return '1'
        elif arr_str == '0'*9:
            return '0'
        elif arr_str =='-1'*9:
            return '-1'
        else:
            return arr_str

result = solution(arr)
print(result.count('-1'))
print(result.count('0'))
result = result.replace('-1', '')
print(result.count('1'))