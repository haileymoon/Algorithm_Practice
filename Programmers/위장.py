#경우의 수 방법론!!!!
# 다만 '최소' 한 가지 의상이라 했으니
# 상의a, 상의b, 상의를 입지 않음 <- 입지 않은 경우의 수도 넣어야 한다. 따라서
# (상의의 수)+1(상의X) * (하의의 수)+하의X - 1(아무것도 입지 않은 경우) 이 답이 되는 셈

def solution(clothes):
    sum_all = 0
    c_dict = {}
    if not clothes:
        return 0
    for clothing in clothes:
        name, clothing_type = clothing[0], clothing[1]
        if clothing_type not in c_dict.keys():
            c_dict[clothing_type] = [name]
        else:
            c_dict[clothing_type].append(name)
    
    ways = 1
    for each in c_dict.keys():
        ways *= (len(c_dict[each])+1)
    return ways-1
