import sys
from itertools import combinations
n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
answers = []
for i in combinations(cards, 3):
    if sum(i) <= m:
        answers.append(sum(i))
answers.sort()
print(answers[-1])