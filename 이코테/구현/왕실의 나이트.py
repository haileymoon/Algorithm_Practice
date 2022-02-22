# ascii ord(), chr()
# 핵심 아이디어: abcdefgh 라고 되어있는게 사실상 우리에겐 숫자, 좌표로 인식되어야하잖아
# 그럼 a는 1이여야하고 ~~
data = input()
row = int(data[1])
column = ord(data[0]) - ord("a") + 1

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
count = 0
for step in steps:
    new_r = row + step[0]
    new_c = column + step[1]
    if new_c >= 1 and new_c <= 8 and new_r >= 1 and new_r <= 8:
        count += 1
print(count)