import sys
from collections import deque

n = int(sys.stdin.readline())
for _ in range(n):
    count = 0
    num, target_idx = map(int, sys.stdin.readline().split())
    documents = list(map(int, sys.stdin.readline().rstrip().split()))
    queue = deque()
    for i, doc in enumerate(documents):
        queue.append(doc)

    while True:
        max_num = max(queue)
        num_now = queue.popleft()
        target_idx -= 1

        if num_now != max_num:
            queue.append(num_now)
            if target_idx == -1:
                target_idx = len(queue) - 1
        else:
            count += 1
            if target_idx == -1 and num_now == max_num:
                print(count)
                break
