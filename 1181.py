import sys

words = list({sys.stdin.readline().rstrip() for i in range (int(sys.stdin.readline()))})
for word in sorted(words, key=lambda x: (len(x), x)): print(word)