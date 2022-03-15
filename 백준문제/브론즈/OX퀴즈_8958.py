n = int(input())
answers = []
for _ in range(n):
    answer = 0
    count =0

    test = list(input())

    for letter in test:
        if letter == "X":
            count = 0
        if letter == "O":
            count += 1
        answer += count
    answers.append(answer)
for ans in answers:
    print(ans)
