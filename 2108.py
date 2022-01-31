import sys
from collections import Counter

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
arr.sort()
cnt = Counter(arr)
cnt_ = cnt.most_common()
most_freq = [x[0] for x in cnt_ if x[1] == cnt_[0][1]]

print(round(sum(arr)/N))
print(arr[(len(arr))//2])
if len(most_freq) == 1:
    print(most_freq[0])
else:
    print(sorted(most_freq)[1])
print(arr[-1]-arr[0])