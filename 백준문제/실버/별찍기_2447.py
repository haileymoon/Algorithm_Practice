def renew_star(star_list):
    temp = []
    # 밑에 있는 for문은 세로로 세었을때 총 몇줄을 배열로 넣을지라고 생각하면됨
    # 즉, 9는 아홉줄, list 3(listlen)*3, 27은 27줄 9(listlen)*3
    for i in range(3*len(star_list)):
        # 우리는 크게 칸을 봤을때를 기준으로 세로로 0,1,2 일때 1부분의 중간을 공백으로 냅둬야 한다.
        # 1일때를 어떻게 구하냐? -> list(몇개짜리 칸으로 둘러쌓여있냐)에 따라 그걸로 나눈 값이 1인 경우이다. (두번재로 반복될때의 값)
        # 27을 예로 들어 0~8의 인덱스까지 9로나누면 몫이 0이다.
        # 중간인 9~17의 중간 부분이 이제 공백이 들어가는 부분이다.
        if i//len(star_list) == 1:
            temp.append(star_list[i%len(star_list)]+ " " * len(star_list) + star_list[i%len(star_list)])
        else:
            temp.append(star_list[i%len(star_list)]*3) # 왜 얘는 3이냐 -> 27이여도 9개의 칸을 3번 붙히고, 9여도 3개칸을 3번 붙힌다. 3의 제곱이기 때문
    return temp



n = int(input())
star = ["***", "* *", "***"]
renew = 0
# star리스트를 그에 맞게 몇 번 바꿔줄지
# 3은 바로 출력하면되니까 0번, 9는 3으로 둘러쌓여있으니 1번, 27은 9로 둘러쌓여있으니 2번(3->9, 9->27)
while n != 3:
    n = n//3
    renew += 1
for _ in range(renew):
    star = renew_star(star)
for i in star:
    print(i)