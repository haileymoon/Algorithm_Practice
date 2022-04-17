n = int(input())
cards = list(map(int, input().split()))
max_card = max(cards)
cards.remove(max_card)
answer = 0
for card in cards:
    answer = answer + card + max_card
print(answer)