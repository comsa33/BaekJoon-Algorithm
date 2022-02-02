import sys

schedules = sorted([list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(int(sys.stdin.readline()))], key=lambda x: (x[0], x[1]))
min_e = 2**31
count = 0
for s, e in schedules:
    if count == 0:
        min_e = e
        count += 1
    elif e < min_e:
        min_e = e
    elif s >= min_e:
        min_e = e
        count += 1
print(count)