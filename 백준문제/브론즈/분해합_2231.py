# n = int(input())
# flag = False
# for i in range(1, n+1):
#     str_i = list(map(int, str(i)))
#     result = i + sum(str_i)
#     if result == n:
#         print(i)
#         flag = True
#         break
#
# if flag == False:
#     print(0)

n = int(input())
constructor = 0
flag = False
for i in range(n):
    str_i = str(i)
    sum = i
    for j in str_i:
        sum += int(j)

    if sum == n:
        constructor = i
        flag = True
        break

if flag is False:
    print(0)
else:
    print(constructor)