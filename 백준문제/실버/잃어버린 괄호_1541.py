from collections import deque
# 숫자들을 작은->큰 순서로 나열, 작은 숫자들끼리 더해줌, 더하기를 다 쓴다음부터는 마이너스
equation = deque(input())
digit = []
count_plus = 0
count_minus = 0
answer = 0
while equation:
    element = equation.popleft()
    num = []
    print(element)
    while element.isdigit():
        num.append(element)
        if not equation:
            break
        element = equation.popleft()
    digit.append(int("".join(num)))
    num = 0
    if element == "+":
        count_plus += 1
        print("plus")
    elif element == "-":
        count_minus += 1
        print("minus")


digit.sort()
print(digit)
print(count_plus, count_minus)

for num in digit:
    if count_plus != 0:
        answer += num
        count_plus -= 1
    else:
        answer -= num
print(answer)