n = input()
if int(n) < 10:
    n = "0"+n
number = [n[0],n[1]]
answer = ""
count = 0
while True:
    add = str(int(number[0])+int(number[1]))
    if  int(add) < 10:
        add = "0"+add
    number[0] = number[1]
    number[1] = add[1]
    count+=1
    if answer.join(number) == str(n):
        break
print(count)