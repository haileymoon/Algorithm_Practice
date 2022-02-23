
import sys
N = int(sys.stdin.readline())
plan = list(sys.stdin.readline().split())
x,y = 1,1
#LRUD순으로
dict = {"L":0, "R":1, "U":2, "D":3}
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for direction in plan:
    index = dict[direction]
    if x+dx[index]>0:
        x = x + dx[index]
    else:
        continue
    if y+dy[index]>0:
        y = y+dy[index]
    else:
        continue
print(x,y)