L = int(input())
S = input()
char = dict(zip(list('abcdefghijklmnopqrstuvwxyz'), range(1,27)))
def get_hash(S):
    hash_ = 0
    for i,s in enumerate(S):
        hash_ += char[s]*(31**i)
    return hash_%1234567891

print(get_hash(S))
