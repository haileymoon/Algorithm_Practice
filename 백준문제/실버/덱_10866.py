from collections import deque
import sys
n = int(sys.stdin.readline())
deque_queue = deque([])
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "push_back":
        deque_queue.append(command[1])
    elif command[0] == "push_front":
        deque_queue.appendleft(command[1])
    elif command[0] == "pop_front":
        if deque_queue:
            print(deque_queue.popleft())
        else:
            print(-1)
    elif command[0] == "pop_back":
        if deque_queue:
            print(deque_queue.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(deque_queue))
    elif command[0] == "empty":
        if deque_queue:
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if deque_queue:
            print(deque_queue[0])
        else:
            print(-1)
    elif command[0] == "back":
        if deque_queue:
            print(deque_queue[-1])
        else:
            print(-1)