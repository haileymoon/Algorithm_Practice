word = list(input().upper())
count_array = []
distinct = []
for letter in word:
    if letter not in distinct:
        count_array.append(word.count(letter))
        distinct.append(letter)
    else:
        continue
max_count = max(count_array)
if count_array.count(max_count) > 1:
    print("?")
else:
    print(distinct[count_array.index(max_count)])
