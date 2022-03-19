answer = []
for _ in range(int(input())):
    a,b,c,d = map(int, input().split())
    #같은 눈 4개
    if a == b == c == d:
        answer.append(50000 + a * 5000)
    elif a == b:
        #다른 두 쌍 확인 = 경우의 수 ab cd, ac bd, bc ad
        if c == d and c != a:
            answer.append(2000+a*500+c*500)
        elif a == c or a == d:
            answer.append(10000+a*1000)
        else:
            answer.append(1000+a*100)
    elif a == c:
        if b == d and b != a:
            answer.append(2000+a*500+b*500)
        elif a == d or a == b:
            answer.append(10000+a*1000)
        else:
            answer.append(1000+a*100)
    elif a == d:
        if b == c and b != a:
            answer.append(2000+a*500+b*500)
        elif b == a or b == d:
            answer.append(10000+a*1000)
        else:
            answer.append(1000+a*100)
    elif b == c:
        if a == d and a != b:
            answer.append(2000+a*500+b*500)
        elif a == b or d == b:
            answer.append(10000+b*1000)
        else:
            answer.append(1000+b*100)
    elif b == d:
        if a == c and a != b:
            answer.append(2000+a*500+b*500)
        elif a == b or  c == b:
            answer.append(10000+b*1000)
        else:
            answer.append(1000+b*100)
    elif c == d:
        if a == b and a != c:
            answer.append(2000+a*500+c*500)
        elif a == c or b == c:
            answer.append(10000+c*1000)
        else:
            answer.append(1000+c*100)
    else:
        answer.append(max([a,b,c,d])*100)
    #같은 눈 2개씩 2쌍
    #같은 눈 2개
    #같은 눈 3개 (abc d acd b abd c), (bcd a)
    #다 다른 눈
print(max(answer))