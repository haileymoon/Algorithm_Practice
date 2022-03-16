n, m = map(int, input().split())
a = list(input().split())
b = list(input().split())
# 작은 배열부터 정렬끝내고 나머지 쭉 출력하면 됨

def combine(small, big):
    pointer_big = 0
    pointer_small = 0
    count = len(big)+len(small)

    while count != 0:
        if pointer_big == len(big):
            while pointer_small != len(small):
                print(small[pointer_small], end = " ")
                pointer_small += 1
                count -= 0
            break
        if pointer_small == len(small):
            while pointer_big != len(big):
                print(big[pointer_big], end = " ")
                pointer_big += 1
                count -= 0
            break

        if big[pointer_big] != small[pointer_small]:
            if big[pointer_big] > small[pointer_small]:
                print(small[pointer_small], end = " ")
                pointer_small +=1
            else:
                print(big[pointer_big], end = " ")
                pointer_big +=1
        else: # 같다면
            print(big[pointer_big], end = " ")
            pointer_small += 1
            pointer_big += 1

        count -= 1




if n<m:
    combine(a,b)
else:
    combine(b,a)