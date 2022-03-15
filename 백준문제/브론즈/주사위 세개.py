a, b, c = map(int, input().split())
if a != b and b != c and a != c: #세가지 다 같지 않을때
    print(max(max(a,b),c)*100)
elif a == b:
    if b == c: # 세가지 다 같을 때
        print(10000+a*1000)
    else: # a, b 두가지만 같을 때
        print(1000 + a * 100)
elif b == c or a == c: # b,c 나 a,c 두 가지만 같을 때
    print(1000 + c * 100)
else:
    pass
