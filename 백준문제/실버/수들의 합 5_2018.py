n = int(input())
end = 1
summation = 0
count = 1  # 반만 계산해줄꺼라 마지막에 있는 자기 자신 미리 더해주기

for start in range(1, n//2+1):
    while summation < n and start < n//2+1:
        summation += end
        end+=1
    if summation == n:
        count += 1
    summation -= start
print(count)

# start = 0
# end = 1
# sum_value = 1
# answer = 0
# limit = n//2 + 1
# while start < limit:
#     if sum_value < n:
#         end += 1
#         sum_value += end
#     elif sum_value == n:
#         answer += 1
#         sum_value -= start
#         start += 1
#         end += 1
#         sum_value += end
#     else:
#         sum_value -= start
#         start += 1
# print(answer +1)