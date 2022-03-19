#길이가 짧은 것부터
# 길이가 같으면 사전순으로
# 같은 단어가 입력된 경우는 한번씩만 출력
n = int(input())
word_list = set()
# sort 조건이 두개가 있으니 보기 편하게 element도 조건에 맞게 두개 저장
for _ in range(n):
    word = input()
    word_list.add((word, len(word)))

answer = list(word_list)
answer = sorted(answer, key = lambda x: (x[1], x[0]))

for ans, length in answer:
      print(ans)