#ps = parenthesis string

def check(ps):
    check_list = []
    for i in range(len(ps)):
        if ps[i] == "(":
            check_list.append(ps[i])
        elif ps[i] == ")" and check_list:
            check_list.pop()
        else:
            return False
    if not check_list:
        return True

n = int(input())
answers = []
for i in range(n):
    ps = input()
    if check(ps):
        answers.append("YES")
    else:
        answers.append("NO")
for i in answers:
    print(i)
