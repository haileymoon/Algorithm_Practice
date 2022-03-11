n = int(input())
goal = [int(input()) for _ in range(n)]
stack_list = []
answer = []
print_sign = []
count = 1


def not_empty(array):
    if array:
        return True
    return False


def pop_char(array):
    num = array.pop()
    print_sign.append("-")
    return num


def push_char(array, x):
    array.append(x)
    print_sign.append("+")


def stack(num):
    global count
    global stack_list
    global answer
    if num > count:
        while count != num and count <= n:
            count += 1
            push_char(stack_list, count)

    if not_empty(stack_list) and stack_list[-1] == num:
        answer.append(pop_char(stack_list))
    else:
        while count != num and not_empty(stack_list):
            if not stack_list:
                return False
            else:
                char = pop_char(stack_list)
                if char != num and char in goal:
                    return False
                elif char == num:
                    answer.append(char)


push_char(stack_list, count)
flag = True
for i in range(n):
    num = goal[i]
    flag = stack(num)

if len(goal) != len(answer) or flag == False:
    print("NO")
else:
    for i in print_sign:
        print(i)
