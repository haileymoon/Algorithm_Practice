#원래 알람을 45분 앞서는 시간으로 바꾸기
#24시간 표현, 0:0은 자정, 끝은 23:59
extra_time = 45
h, m = map(int,input().split())
min = (m-extra_time)%60
hour = (h+(m-extra_time)//60)%24

print(hour, min)