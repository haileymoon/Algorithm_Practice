n = input()
people = list(map(int, input().split()))
people.sort()
count = 0
group = 0
for person in people:
    count += 1
    if count == person: # 이렇게 해도 문제는없지만 문제에서는 공포도 몇 이상~ 으로 되어있어서 count >= person 처리
        group += 1
        count = 0
print(group)