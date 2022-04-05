# min * n = x
n = int(input())
rope = [int(input()) for _ in range(n)]
rope.sort()
answers = []
for i in range(len(rope)):
    weight = rope[i] * (len(rope) - i)
    answers.append(weight)
print(max(answers))