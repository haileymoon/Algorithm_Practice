n = int(input())

for _ in range(n):
    r, s = input().split()
    text = ""
    for letter in s:
        text += letter * int(r)
    print(text)