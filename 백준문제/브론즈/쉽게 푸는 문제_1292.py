start, end = map(int, input().split())
idx_count = 0
array = []
for i in range(1,end+1):
    for _ in range(1, i+1):
        array.append(i)
        idx_count += 1
    if idx_count > end:
        break
# print(array)
print(sum(array[start-1:end]))
