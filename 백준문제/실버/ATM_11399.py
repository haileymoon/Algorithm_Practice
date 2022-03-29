n = int(input())
time = list(map(int, input().split()))
time.sort()
answer = 0
#prev_time = 0
# for i, person in enumerate(time):
#     answer += person + prev_time
#     prev_time += time[i]

# 인덱싱으로 sum 구할 수 있음
for i in range(len(time)):
    answer += sum(time[:i+1])
print(answer)