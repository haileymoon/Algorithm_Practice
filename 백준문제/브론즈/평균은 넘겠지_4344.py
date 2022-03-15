n = int(input())
#평균이 넘는 학생들의 비율
answer = []
for _ in range(n):
    scores = list(map(int,input().split()))
    number = scores[0]
    del scores[0]
    average = sum(scores)/number
    count = 0
    for score in scores:
        if score> average:
            count += 1
    print("{:.3f}".format((count/number*100))+"%")
