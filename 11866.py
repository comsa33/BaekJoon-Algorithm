import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

group = list(range(1, N+1))
ans = []
i = 0
while len(group) > 1:
    i += K-1
    if len(group)-1 < i:
        while i >= len(group):
            i -= len(group)
        ans.append(str(group.pop(i)))
    else:
        ans.append(str(group.pop(i)))
ans.append(str(group[0]))
print(f"<{', '.join(ans)}>")