up, down, v = map(int, input().split())
count = 0
limit = v - down
count = limit / (up-down)
if count == int(count): #정수라면
    print(count)
else:
    print(int(count) + 1)