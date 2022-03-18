from itertools import combinations
nums = [0,2,7,10,11,15]
target = -10
index_array =[]
for x,y in combinations(nums,2):
    if x+y ==target:
        index_array.append(nums.index(x))
        #같은 수가 두번 나올 때 index혼동방지
        #target의 값이 10^9범위안에서 놀기 때문에 값을 그 범위 밖의 수로 지정
        nums[nums.index(x)] = 9876543210
        index_array.append(nums.index(y))
print(index_array)
