# 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수
# 하루는 86,400초로 000000부터 235959까지 모든 경우의 수는 86400가지밖에 존재하지 않아 3중 반복분으로 해도 충분히 시간 굳
N = input()
count = 0
for i in range (int(N)+1):
    for j in range(60):
        for k in range(60):
            result = str(i)+str(j)+str(k)
            if "3" in result:
                count+=1
print(count)

