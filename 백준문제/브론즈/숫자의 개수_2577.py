import collections

result = 1
answer = [0] * 10
for _ in range(3):
    result *= int(input())

result = str(result)
distinct = list(set(result))
counter = collections.Counter(result)
for num in distinct:
    answer[int(num)] = counter[num]
for a in answer:
    print(a)