n = 5
lost =[2, 3, 4]
reserve = [1, 2, 3]
answer = 0
#교집합
cross_result = set(reserve)&set(lost)
lost_count = len(lost) - len(cross_result)
diff_result = list(set(lost) - set(reserve))
for number in cross_result:
    reserve.remove(number)
#차집합


# lambda_result = [i for i in lost if i in reserve]
# print(lambda_result)
for lost_person in diff_result:
    if lost_person - 1 in reserve:  # 작은 수 부터 체크, 그래야 큰 수들을 최대로
        reserve.remove(lost_person - 1)
        lost_count-=1
    elif lost_person + 1 in reserve:
        reserve.remove(lost_person + 1)
        lost_count-=1
answer = n - lost_count
print(answer)
