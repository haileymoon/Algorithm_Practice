from collections import deque

n = int(input())
cards = deque([i for i in range(1, n+1)])
while len(cards) != 1:
    pop_card = cards.popleft()
    if len(cards) == 1:
        break
    else:
        pop_card = cards.popleft()
        cards.append(pop_card)
print(cards[0])