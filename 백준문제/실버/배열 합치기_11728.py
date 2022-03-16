n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
# 작은 배열부터 정렬끝내고 나머지 쭉 출력하면 됨

pointer_a = 0
pointer_b = 0
while pointer_a < n and pointer_b < m:
    if a[pointer_a] < b[pointer_b]:
        print(a[pointer_a], end = " ")
        pointer_a += 1
    else:
        print(b[pointer_b], end = " ")
        pointer_b += 1
while pointer_a < n:
    print(a[pointer_a], end = " ")
    pointer_a += 1
while pointer_b < m:
    print(b[pointer_b], end = " ")
    pointer_b += 1
