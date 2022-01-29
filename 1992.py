import sys

def solution(arr):
    arr_str = ''.join(map(''.join, arr))
    if arr_str == '0'*len(arr_str):
        return '0'
    elif arr_str == '1'*len(arr_str):
        return '1'
    else:
        mid = len(arr)//2
        ul = solution([line[:mid] for line in arr[:mid]])
        ur = solution([line[mid:] for line in arr[:mid]])
        dl = solution([line[:mid] for line in arr[mid:]])
        dr = solution([line[mid:] for line in arr[mid:]])
        return f'({ul}{ur}{dl}{dr})'

if __name__ == '__main__':
    arr = [list(sys.stdin.readline().rstrip()) for _ in range(int(sys.stdin.readline()))]
    print(solution(arr))
        