from collections import deque
import sys # 시간초과가 났었는데 input대신 sys.stdin.readline쓰니까 바로 통과;;
#push(x), pop, size, empty, front, back
input = sys.stdin.readline
n = int(input())
my_queue = deque()
#push(x), pop, size, empty, front, back
for _ in range(n):
    command = input().split()
    if command[0] == "push":
        my_queue.append(command[1])
    elif command[0] == "size":
        print(len(my_queue))
    elif command[0] == "empty":
        if my_queue:
            print(0)
        else:
            print(1)
    else:
        if not my_queue:
            print(-1)
        elif command[0] == "pop":
            print(my_queue.popleft())
        elif command[0] == "back":
            print(my_queue[-1])
        elif command[0] == "front":
            print(my_queue[0])