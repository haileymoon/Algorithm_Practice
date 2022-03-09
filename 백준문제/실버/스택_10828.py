class stack:
    def __init__(self):
        self.container = []
    def push(self, x):
        self.container.append(x)
    def pop(self):
        if len(self.container) == 0:
            return -1
        else:
            return self.container.pop()
    def size(self):
        return len(self.container)
    def empty(self):
        if len(self.container) == 0:
            return 1
        else: return 0
    def top(self):
        if not self.empty():
            return self.container[-1]
        else:
            return -1

n = int(input())
main_stack = stack()
answer = []
for _ in range(n):
    command = input().split()
    if command[0] == "top":
        answer.append(main_stack.top())
        continue
    if command[0]  == "size":
        answer.append(main_stack.size())
        continue
    if command[0] == "empty":
        answer.append(main_stack.empty())
        continue
    if command[0] == "pop":
        answer.append(main_stack.pop())
        continue
    if command[0] == "push":
        main_stack.push(command[1])
        continue
for i in answer:
    print(i)