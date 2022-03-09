k = int(input())
answer = []
for _ in range(k):
    num = int(input())
    if num != 0:
        answer.append(num)
    else:
        #answer.pop()
        del answer[-1]
print(sum(answer))