while True:
    numbers = list(map(int, input().split()))
    flag = False
    if sum(numbers) == 0:
        break
    else:
        long = max(numbers)
        numbers.remove(long)
        if long**2 == (numbers[0]**2)+(numbers[1]**2):
            flag = True
    if flag:
        print("right")
    else:
        print("wrong")