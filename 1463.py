import sys

def solution(n, memo = {1:0, 2:1, 3:1}):
    if n in memo:
        return memo[n]
    ans = 1 + min(solution(n//3)+n%3, solution(n//2)+n%2)
    memo[n] = ans
    return ans
    

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    print(solution(n))