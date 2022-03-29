size = int(input())
size_list = []
result = ["0"] * size
dict = {}
for i in range(size):
    w, h = map(int, input().split())
    size_list.append((w,h))
    if dict.get((w,h)) is None:
        dict[(w,h)] = [i]
    else:
        dict[(w, h)].append(i)

idx = 0
nxt_idx = 1
size_list.sort()
for m in range(size):
    x, y = size_list[m]
    count = 1
    for n in range(m+1,size):
        n_x, n_y = size_list[n]
        if n_x > x and n_y > y:
            count += 1
    result[dict[(x,y)][0]] = str(count)
    del dict[(x,y)][0]
print(" ".join(result))