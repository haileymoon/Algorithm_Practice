import sys
m, n = map(int, sys.stdin.readline().split())

def checkPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5) +1): #제곱근까지만 확인!
            if n % i == 0:
                return False
        return True

for i in range(m, n+1):
    if checkPrime(i):
        print(i)

# 나는 너무 있는 그대로 에라토스테네스의 체를 만들었음 (그럴필요X)
# -> 원리는 n의 제곱근까지만 확인하면 되는것!
# numbers = []
# answers = []
# visited = [False for _ in range(n+1)]
# for i in range(2, n+1):
#     numbers.append(i)
#
# for num in numbers:
#     if visited[num] == False:
#         answers.append(num)
#         for j in range(2, n+1):
#             if num*j > n:
#                 break
#             elif visited[num*j] == False:
#                 visited[num*j] = True
#     visited[num] == True
#
# for i in range(len(answers)):
#     if m <= answers[i] <= n:
#         print(answers[i])