from itertools import permutations
import sys
input = sys.stdin.readline
sign_dict = {0:"+",1:"-", 2:"*",3:"/"}
n = int(input())
num_list = list(map(int, input().split()))
sign_array = list(map(int, input().split()))
signs = ""
max_result, min_result = -987654321, 987654321

for i in range(len(sign_dict)):
    signs += (sign_dict[i] * sign_array[i])
signs = list(signs)

for sign in set(permutations(list(signs))):
    result = num_list[0]
    for i, each in enumerate(sign):
        if each == "+":
            result += num_list[i+1]
        elif each == "-":
            result -= num_list[i+1]
        elif each == "*":
            result *= num_list[i+1]
        else:
            if result < 0:
                result = -((-result)//num_list[i+1])
            else:
                result //= num_list[i+1]
    max_result = max(max_result, result)
    min_result = min(min_result, result)
print(max_result)
print(min_result)

# 시간초과, 중복제거 문제
# permutations를 쓴다면 ++-에서 첫번째 두번째가 바뀐것이 ++-임. 중복제거를 해야 시간초과가 안남
# permutation이 된거에 set을 해야지 그냥 연산자에다 set해버리면 결과값자체가 달라짐 주의
# https://www.acmicpc.net/board/view/86187
