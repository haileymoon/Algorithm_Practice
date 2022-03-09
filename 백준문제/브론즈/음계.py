music = list(map(int, input().split()))
start = music[0]
ascending = False
descending = False
for i in range(1, len(music)):
    if music[i] == start+1:
        start += 1
    else:
        ascending = False
        break
    ascending = True
for i in range(1, len(music)):
    if music[i] == start-1:
        start-=1
    else:
        descending = False
        break
    descending = True
if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")