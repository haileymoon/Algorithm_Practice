n, m = map(int,input().split())
array = list(map(int, input().split()))
end = 0
summation = 0
count =0
for start in range(n):
    while summation < m and end < n:
        summation += array[end]
        end+=1
    if summation == m:
        count += 1
    summation -= array[start]
print(count)