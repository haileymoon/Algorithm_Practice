# 0과 1로만 된 문자열이 주어지고, 연속된 하나 이상의 숫자를 잡고 뒤집을 수 있음
# 다 같은 숫자로 만들려면 몇 번 뒤집어야 하는지
# 핵심 아이디어: 몇번부터 몇번까지 인지는 알 필요없고 몇 번 바뀌는지 알아야하는 듯
# 기준이 1일 때 몇번 바뀌고 0일 때 몇번 바뀌는지 비교

# 책답안
s = list(map(int, input()))
count0 = 0 #전부 0으로 바꾸는 경우
count1 = 0
#첫번째 원소 처리
if s[0] == 1:
    count0 += 1
else:
    count1 += 1
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == 1:
            count0 += 1
        else:
            count1 += 1
print(min(count0, count1))
 
# 내 첫 답안:
# 0과 1이 바뀔 때를 비교하려고 했는데 예시를 계속 들어보니까
# 바뀐 횟수/2, 짝수일때는 (횟수/2)+1 가 최소인 것 같아서 우선은 시도해봤음
# s = list(map(int, input()))
# point = s[0]
# count = 0
# for num in s:
#     if num != point:
#         count += 1
#         point = num
# if count%2 ==0:
#     print(int(count/2))
# else:
#     print(int(count/2+1))
