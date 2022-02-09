# 메모이제이션
# def fiv(n, memo):
#     if n < 3:
#         return 1
#     if n in memo:
#         return memo[n]
#     memo[n] = fiv(n-2, memo)+fiv(n-1, memo)
#     return memo[n]
        

# if __name__ == '__main__':
#     n = 10000
#     memo = {}
#     print(fiv(n, memo))

# 태블로
# def fiv(n):
#     arr = [num for num in range(n+1)]
#     if n < 2:
#         return n
#     for i in range(2, n+1):
#         arr[i] = arr[i-1]+arr[i-2]
#     return arr[n]

# calculated = {}
# def fiv(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     elif n in calculated:
#         return calculated[n]
#     else:
#         calculated[n] = fiv(n-1) + fiv(n-2)
#         return calculated[n]

def fiv(n, memo={}):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fiv(n-2, memo)+fiv(n-1, memo)
    return memo[n]

if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(100000000)
    n = int(sys.stdin.readline())
    if n % 2 == 0:
        for i in range(n):
            if 2*i-1 == n-1:
                ans = fiv(i)**2 + fiv(i-1)**2
            if 2*i-1 == n+1:
                ans = fiv(i)**2 + fiv(i-1)**2 - ans
    else:
        for i in range(n):
            if 2*i-1 == n:
                ans = fiv(i)**2 + fiv(i-1)**2
    
    print(ans%1000000007)



import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
fibonacci = {0: 0, 1: 1, 2: 1}


def getFibonacci(n):
    if not fibonacci.get(n):
        if n % 2 == 1:
            fibonacci[n] = (getFibonacci((n+1)//2)**2 +
                            getFibonacci((n+1)//2-1)**2) % 1000000007
        else:
            fibonacci[n] = (getFibonacci(n+1) - getFibonacci(n-1)) % 1000000007

    return fibonacci[n]


if __name__ == '__main__':
    N = int(input())

    print(getFibonacci(N))