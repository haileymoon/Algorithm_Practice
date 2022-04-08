import sys
t = int(sys.stdin.readline())
for _ in range(t):
    answer = []
    n = int(sys.stdin.readline())
    cards = list(sys.stdin.readline().split())
    answer.append(cards[0])
    for i in range(1, n):
        if answer[0] >= cards[i]:
            answer.insert(0, cards[i])
        else:
            answer.append(cards[i])

    print("".join(answer))
