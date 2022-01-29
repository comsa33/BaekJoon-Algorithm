import sys

stack = []

n = int(sys.stdin.readline())

def push(n):
    stack.append(n)

def pop():
    try:
        if stack[-1]:
            return stack.pop()
    except IndexError:
        return -1

def size():
    return len(stack)

def empty():
    if len(stack) == 0 :
        return 1
    else :
        return 0

def top():
    if len(stack) == 0:
        return -1
    else :
        print(stack[-1])

for i in range(n):
    comm = input().split()

    if comm[0] == 'push' :
        push(comm[1])
    elif comm[0] == 'pop':
        print(pop())
    elif comm[0] == 'size' :
        print(size())
    elif comm[0] == 'empty' :
        print(empty())
    else :
        top()