n = int(input())
start = 0
end = 1
sum_value = 1
answer = 0
limit = n//2 + 1
while start < limit:
    if sum_value < n:
        end += 1
        sum_value += end
    elif sum_value == n:
        answer += 1
        sum_value -= start
        start += 1
        end += 1
        sum_value += end
    else:
        sum_value -= start
        start += 1
print(answer +1)