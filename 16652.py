import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
cnt = {}
for _ in range(k):
    email = sys.stdin.readline().rstrip()
    title = email.replace('Re: ', '')
    if cnt.get(title):
        if cnt[title] < email.split().count('Re:') + 1:
            cnt[title] = email.split().count('Re:') + 1
    else:
        cnt[title] = email.split().count('Re:') + 1

min_no = sum(cnt.values())

if n >= min_no:
    print('YES')
else:
    print('NO')