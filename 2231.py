from itertools import permutations
N = input()

arr = [n for n in range(10)]
try:
    print(min(list(map(lambda x: int(''.join(list(map(str, x)))), list(filter(lambda x: sum(x) + int(''.join(list(map(str, x)))) == int(N) ,list(permutations(arr, len(N)))))))))
except ValueError:
    print(0)