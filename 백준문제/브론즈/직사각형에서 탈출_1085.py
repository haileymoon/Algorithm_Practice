x, y, w, h = map(int, input().split())
size_from_x = x - 0 if w-x > x-0 else w-x
size_from_y = y - 0 if h-y > y-0 else h-y
print(min(size_from_y, size_from_x))

