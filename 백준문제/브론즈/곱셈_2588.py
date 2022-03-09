first_num = int(input())
second_num = input()
for i in range(len(second_num),0,-1):
    print(first_num*int(second_num[i-1]))
print(first_num*int(second_num))