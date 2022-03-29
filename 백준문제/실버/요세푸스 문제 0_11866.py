n, target = map(int, input().split())
circle = [i for i in range(1, n+1)]
new_target = 0
result = []

while circle:
    new_target = (target - 1 + new_target) % len(circle)

    result.append(str(circle[new_target]))
    del circle[new_target]
    print(circle)
print("<"+", ".join(result)+">")