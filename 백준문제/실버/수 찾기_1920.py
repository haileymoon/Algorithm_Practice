# a_n = int(input())
# a_list = set(map(int, input().split()))
# b_n = int(input())
# b_list = list(map(int, input().split()))
# answer = [0 for _ in range(b_n)]
# for i in range(len(b_list)):
#     if b_list[i] in a_list:
#         print(1)
#     else: print(0)

# 이분탐색
a_n = int(input())
a_list = list(map(int, input().split()))
a_list.sort()
b_n = int(input())
b_list = list(map(int, input().split()))
#있는지 없는지 확인하는 탐색 함수
def binary_search(num):
    start = 0
    end = len(a_list)-1

    while start <= end:
        mid = (start + end) // 2
        if a_list[mid] == num:
            print(1)
            return True
        elif num > a_list[mid]:
            start = mid + 1
        elif num < a_list[mid]:
            end = mid -1
    print(0)

for i in b_list:
    binary_search(i)