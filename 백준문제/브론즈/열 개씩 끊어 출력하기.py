word = input()
num_of_ten = len(word)//10
remainder = len(word)%10
print(remainder)
start = 0
end = 10

for i in range(num_of_ten):
    print(word[start:end])
    start += 10
    end += 10
if remainder != 0:
    print(word[-remainder:])