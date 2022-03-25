a, b = map(int, input().split())

#큰수를 a에다가 넣어줌
if a<b:
    temp = a
    a = b
    b = temp

# 최대공약수 - 유클리드 호제법 알고리즘 활용
def UCLD_GCD(x,y):
    gcd = 0
    while True:
        remainder = x % y

        if remainder == 0:
            gcd = y
            break

        x = y
        y = remainder
    return gcd

# 최소공배수
#두 수의 모든 소인수를 곱하면 최소공배수
def UCLD(x,y):
    gcd = UCLD_GCD(x,y)
    print(gcd)
    # LCM 두수를 곱한걸 최대공약수로 나누어주면 된다.
    # X = AB, Y=BC, 최대공약수는 B, 최소공배수는 ABC, X*Y = A*B^2*C 이걸 B로 나누면 ABC
    print((x*y)//gcd)

UCLD(a,b)