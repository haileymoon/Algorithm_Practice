a, b = input().split()

a = list(a)
b = list(b)

a.reverse()
b.reverse()

a = "".join(a)
b = "".join(b)

if int(a) > int(b):
    print(int(a))
else:
    print(int(b))