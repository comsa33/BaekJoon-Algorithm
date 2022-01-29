import sys

members = [[i]+sys.stdin.readline().rstrip().split() for i in range(int(sys.stdin.readline()))]
for _, age, name in sorted(members, key=lambda x: (int(x[1]), x[0])):
    print(f'{age} {name}')