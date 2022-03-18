word = list(input())
answer = []
for alphabet in range(ord("a"), ord("z")+1):
    check = chr(alphabet)
    if check in word:
        answer.append(word.index(check))
    else:
        answer.append(-1)
for a in answer:
    print(a, end = " ")
