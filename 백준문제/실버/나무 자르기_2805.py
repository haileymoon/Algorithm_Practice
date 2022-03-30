n, target = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 1, max(trees)
answer = 0

while start <= end:
    mid = (start+end)//2
    result = 0
    for tree in trees:
        if tree > mid:
            result += (tree-mid)
    if result >= target:
        start = mid + 1
    else:
        end = mid - 1
print(end) # 사실 상 middle이 답인데 한번 더 수행됨에 따라 middle이 커지고, start는 더해짐, end는 -1이니까 오히려 정답