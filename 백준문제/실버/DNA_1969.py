from collections import Counter
n, m = map(int, input().split())
dna = []
answer = []
count = 0

for _ in range(n):
    dna.append(input())

for i in range(m):
    dna_letter = []
    for j in range(n):
        dna_letter.append(dna[j][i])
    counter = Counter(dna_letter)
    # sort까지 해줌
    max_count = counter.most_common()
    freq = max_count[0][1]
    keys = []
    for num in max_count:
        if num[1] == freq:
            keys.append(num[0])
    keys.sort()
    answer.append(keys[0])
    counter.pop(keys[0])
    for item in counter.values():
        count += item

answer = "".join(answer)

print(answer)
print(count)