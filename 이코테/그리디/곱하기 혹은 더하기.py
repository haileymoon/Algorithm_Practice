# 주어진 수를 왼쪽에서 오른쪽으로 연산하는데 *가 들어갈지 +가 들어갈지 정하기
# 대신 *가 +가 먼저 계산되는 법칙은 무시. 그냥 순서대로 연산
# 핵심 아이디어: 만들어질 수 있는 가장 큰 수는 0이나 1만 더해주고 나머지 수는 다 곱해주면 됨
# revised: 1이하인 수는 더하고, 2 이상인 수는 곱하기
s = list(map(int, input()))
sum = s[0]
add = [0,1]
for i in range(1, len(s)):
    if (s[i-1] not in add) and (s[i] not in add): # if s[i] <= 1 or sum <=1:
        sum *= s[i]
    else:
        sum += s[i]
print(sum)