while True:
    flag = False
    stack = []
    num = input()
    if num == "0": break
    half = len(num)//2
    for i in range(half):
        stack.append(num[i])
    if len(num)%2 == 0:
        start = half
    else:
        start = half+1
    for i in range(start,len(num)):
        if stack.pop() == num[i]:
            continue
        else:
            flag =True
            break
    if flag:
        print("no")
    else:
        print("yes")
