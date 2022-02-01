def draw_pattern(n):
    if n == 1:
        return '*'
    else:
        pattern = draw_pattern(n//3)
        return pattern*n+'\n'+pattern+' '*(n//3)+pattern+'\n'+pattern*n

if __name__ == '__main__':
    N = int(input())
    print(draw_pattern(N))
