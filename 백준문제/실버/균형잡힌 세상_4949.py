#ps = parenthesis string

def check(sentence):
    open_list = []
    for i in range(len(sentence)):
        char = sentence[i]
        if char == "(" or char == "[":
            open_list.append(char)
        if char == ")":
            if open_list and open_list.pop()== "(":
                continue
            else:
                return False
        elif char == "]":
            if open_list and open_list.pop()== "[":
                continue
            else:
                return False
    if len(open_list) == 0:
        return True

answer = []
while True:
    sentence = list(input())
    if len(sentence) == 1 and sentence[-1] == ".":
        break
    if check(sentence):
        answer.append("yes")
    else:
        answer.append("no")
for i in answer:
    print(i)

