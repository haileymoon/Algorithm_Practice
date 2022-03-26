n = int(input())
numbers = []
for _ in range(n):
    numbers.append(tuple(map(int, input().split())))
sorted_num = sorted(numbers, key= lambda x: (x[1], x[0]))
for nums in sorted_num:
    print(nums[0], nums[1])