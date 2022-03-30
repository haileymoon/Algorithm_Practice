import sys
import heapq

n = int(sys.stdin.readline())
schedule =[]
count = 1

for _ in range(n):
    schedule.append(tuple(map(int, sys.stdin.readline().split())))

schedule.sort(key = lambda x : (x[0], x[1]))
heap = [schedule[0][1]]

for i in range(1, n):
    start, end = schedule[i]
    if start < heap[0]:
        count += 1
        heapq.heappush(heap, end)
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, end)
print(count)
