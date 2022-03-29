n = int(input())
schedule = list()
results = []

for _ in range(n):
    time = tuple(map(int, input().split()))
    schedule.append(time)
schedule.sort(key = lambda x : (x[1],x[0]))

count = 1
temp_end = schedule[0][1]
for i in range(1, len(schedule)):
    if schedule[i][0] >= temp_end:
        count += 1
        temp_end = schedule[i][1]
print(count)