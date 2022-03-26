import sys
from collections import Counter
# count이라는 내장함수보다 counter이라는 외장함수가 더 강력하다

n = int(sys.stdin.readline())
sanggeun = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

counter = Counter(sanggeun)

for num in numbers:
    if num in counter:
        print(counter[num], end=" ")
    else:
        print(0,  end=" ")

