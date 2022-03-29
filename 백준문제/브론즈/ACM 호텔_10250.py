case = int(input())
for _ in range(case):
    h, w, n = map(int, input().split())
    q = n // h
    r = n % h
    floor = 0
    if r == 0:
        r = h
        floor = q
    else:
        floor = q+1
    if floor < 10:
        print(str(r)+"0"+str(floor))
    else:
        print(str(r)+str(floor))