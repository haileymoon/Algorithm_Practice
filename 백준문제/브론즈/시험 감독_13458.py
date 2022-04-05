# 감독관 두명, 총->B, 부-> C명 감시 가능
# 필요한 감독관 수의 최솟값 -> 동전 문제와 유사
n = int(input())
numbers_of_students = list(map(int, input().split()))
directors = list(map(int, input().split()))
count = 0


for i in range(n):
    director2 = 0
    numbers_of_students[i] -= directors[0]
    if numbers_of_students[i] > 0:
        director2 = numbers_of_students[i] // directors[1]
        numbers_of_students[i] %= directors[1]
        if numbers_of_students[i] != 0:
            count += 1

    count += (1 + director2)

print(count)