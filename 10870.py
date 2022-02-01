def fiv(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fiv(n-2)+fiv(n-1)

if __name__ == '__main__':
    N = int(input())
    print(fiv(N))