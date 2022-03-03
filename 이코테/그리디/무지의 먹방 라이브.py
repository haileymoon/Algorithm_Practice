# 아 너무 아까운 문제, 아이디어가 답에 굉장히 근접해있었는데 이때까지 스킵해온 것들 때문에 정리가 잘 안됐음
# 내 아이디어를 정리시켜준 것은 바로 마지막 자리 인덱스!!!
# 배열에서 0이 아닌 것들을 카운트한게 바로 배열의 마지막 인덱스에 다다랐을때 초!
# 나는 0이 아닌 것들을 누적 카운트한게 K보다 크거나 같을 때 순환을 멈춘다 까진 생각했는데
# 순서를 이제 어디서부터 첫 시작을 해야하는지 몰랐음. 마지막 인덱스에 다다랐을때 초라는 걸 알았다면 정리되었을듯
# 힌트를 얻었던 사람의 풀이: https://onejunu.tistory.com/73

food_times = [5, 0, 3, 3, 1]
k = 9
repeat_times = 1 # 우선 한번 먹어줌 두번째부터 마이너스
skip_count = 0
last_index = 0
while True:
    last_index = repeat_times * len(food_times) - skip_count
    if last_index + len(food_times) > k:
        break
    repeat_times += 1
    for i in range(len(food_times)):
        food_times[i] = food_times[i]-1
        if food_times[i]<=0:
            skip_count += 1
count = 0
index = 0
while True: # k번째가 실행된 이후의 값을 원하기때문에 +1을 한번 더 해줌
    food_times[index] -= 1
    if food_times[index] <= 0:
        index += 1
        if index == len(food_times):
            index = 0
        continue
    else:
        # i에 +1 이유: 1) 답은 사실상 k번째까지 완료한 후 다음껄 재개하는걸 원하기 때문에 그 다음 인덱스를 찾아줌
        # answer에 +1 이유 2) ~번째를 뜻하기 위해 인덱스 +1
        answer = index+1
        count +=1
        index+=1
    if index == len(food_times):
        index = 0
    if (count == k-last_index+1):
        break
print(answer)