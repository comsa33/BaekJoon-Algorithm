from collections import deque

cards = deque(range(1, int(input())+1))

i = 0
while len(cards) > 1:
    draw = cards.popleft()
    if i%2 != 0:
        cards.append(draw)
    i += 1
print(cards[0])