string = input()
sum = 0
string = sorted(string) # result list를 따로 만들어서 알파벳만 모아놓은 다음 sort하면 더 빠를듯

for letter in string:
    if letter.isdigit():
        sum += int(letter)
    else:
        print(letter, end = "")
print(sum)