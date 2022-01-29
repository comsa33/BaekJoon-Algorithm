def fiv(n):
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 1 + fiv(n-1)

if __name__ == '__main__':
    n = 4
    print(fiv(n))