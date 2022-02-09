import sys

def fiv_count(num, dic=dict()):
    if num == 0:
        dic.setdefault(num, 0)
        dic[num] += 1
        return 0, dic
    if num == 1:
        dic.setdefault(num, 0)
        dic[num] += 1
        return 1, dic
    else:
        return fiv_count(num-2)[0] + fiv_count(num-1)[0], dic

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    for _ in range(N):
        dic = fiv_count(int(sys.stdin.readline()))[1]
        print(dic[0], dic[1])