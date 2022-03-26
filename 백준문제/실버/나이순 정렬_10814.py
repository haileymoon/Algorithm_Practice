n = int(input())
members = []
names = []
for i in range(n):
    age, name = input().split()
    members.append((i, int(age)))
    names.append(name)
members.sort(key= lambda x:(x[1], x[0]))
for person in members:
    print(person[1], names[person[0]])