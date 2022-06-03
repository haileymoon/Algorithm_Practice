# from itertools import combinations
# while True:
#     input_list = list(map(int, input().split()))
#     if input_list[0] == 0:
#         break
#     k = input_list[0]
#     lotto = input_list[1:]
#     for i in combinations(lotto, 6):
#         print(*i)
#     print()

#dfs 풀이
def dfs(start, depth):
    if depth == 6:
        for num in range(6):
            print(array[num], end =" ")
        print()
        return
    for i in range(start, len(lotto)):
        array[depth] = lotto[i]
        dfs(i+1, depth+1)
array = [0 for i in range(13)]

while True:
    input_list = list(map(int, input().split()))
    if input_list[0] == 0:
        break
    k = input_list[0]
    lotto = input_list[1:]
    dfs(0,0)
    print()

#https://intrepidgeeks.com/tutorial/bojun-python-lottery-6603
