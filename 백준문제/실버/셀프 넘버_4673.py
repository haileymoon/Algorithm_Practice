numbers = set(range(1,10001))
generated = set()

for num in range(1,10001):
    sum = num
    for i in str(num):
        sum += int(i)
    generated.add(sum)

for element in (sorted(numbers-generated)):
    print(element)