#서로 다른 수니까 key로 지정가능
dict= {int(input()):i for i in range(3)}
max = max(list(dict.keys()))
print(max)
print(dict[max]+1)
