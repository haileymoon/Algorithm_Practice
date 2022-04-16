import sys
from collections import deque

n = int(sys.stdin.readline())
for _ in range(n):
    left = deque()
    right = deque()
    pwd = list(sys.stdin.readline().rstrip())
    for i in range(len(pwd)):
        if pwd[i] == "<":
            if left:
                right.append(left.pop())

        if pwd[i] == ">":
            if right:
                left.append(right.pop())

        if pwd[i] == "-":
            if left:
                left.pop()

        if pwd[i].isalnum():
            left.append(pwd[i])

    for r in range(len(right)):
        left.append(right.pop())

    print("".join(left))

# ` ss시간초과
# n = int(input())
# answer = []
#
# for _ in range(n):
#     cursor = 0
#     pwd = input()
#     word = []
#     for i in range(len(pwd)):
#         if pwd[i] == "<":
#             if cursor-1 >= 0:
#                 cursor -= 1
#                 continue
#
#         if pwd[i] == ">":
#             if cursor+1 <= len(word):
#                 cursor += 1
#                 continue
#
#         if pwd[i] == "-":
#             try:
#                 if word[cursor-1].isalpha():
#                     del word[cursor-1]
#                     cursor -= 1
#             except:
#                 pass
#         if pwd[i].isalnum():
#             if cursor == len(word):
#                 word.append(pwd[i])
#                 cursor += 1
#             else:
#                 word.insert(cursor, pwd[i])
#                 cursor += 1
#     print("".join(word))
