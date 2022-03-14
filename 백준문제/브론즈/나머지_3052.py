divide_num = 42
answers = []
count = 0
for _ in range(10):
    num = int(input())
    result = num%divide_num
    if result not in answers:
        count += 1
        answers.append(result)
print(count)