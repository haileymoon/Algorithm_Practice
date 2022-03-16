n = int(input())
count = 0

def check_wrong_diff(string_num):
    diff = 987654321
    flag = False
    for i in range(len(string_num), 1, -1):
        value = int(string_num[i-1]) - int(string_num[i - 2])
        if diff == 987654321:
            diff = value
        else:
            if diff != value:
                flag = True
    return flag

if n < 10:
    count += n
else:
    count += 9
    for i in range(10,n+1):
        str_i = str(i)
        if check_wrong_diff(str_i):
            continue
        else:
            count+=1
print(count)


