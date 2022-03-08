# import sys
# from collections import deque
# import copy

from itertools import combinations

n = int(input())
teachers = []
blanks = []
graph = []

for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        #선생님 위치저장
        if graph[i][j] == "T":
            teachers.append((i,j))
        #장애물 설치가능한 빈공간 저장
        if graph[i][j] == "X":
            blanks.append((i,j))

# 특정 방향으로 감시 진행(학생 발견 true, 미발견 false)
def watch(x, y, direction):
    #왼쪽감시 (방향을 숫자로 임의로 정함 왼쪽:0, 오른쪽:1, 위쪽:2, 아래쪽:3)
    if direction == 0:
        while y >= 0: #왼쪽 범위 벗어나지 않을때까지
            if graph[x][y] == "S":
                return True
            if graph[x][y] == "O": # 장애물을 먼저 만난 경우 학생을 만날 수 없기 때문에 False
                return False
            y -= 1
    #오른쪽 감시
    if direction == 1:
        while y < n: # 0부터 시작하니까 실질적으론 N-1
            if graph[x][y] == "S":
                return True
            if graph[x][y] == "O":  # 장애물을 먼저 만난 경우 학생을 만날 수 없기 때문에 False
                return False
            y += 1
    #위로 감시(위면 제일 윗부분이 0임)
    if direction == 2:
        while x >=0:
            if graph[x][y] == "S":
                return True
            if graph[x][y] == "O":  # 장애물을 먼저 만난 경우 학생을 만날 수 없기 때문에 False
                return False
            x -= 1
    #아래로 감시
    if direction == 3:
        while x < n:
            if graph[x][y] == "S":
                return True
            if graph[x][y] == "O":  # 장애물을 먼저 만난 경우 학생을 만날 수 없기 때문에 False
                return False
            x += 1
    #만약 이 4가지 direction에서 빠져나가지 못했다면 False 리턴해줌
    return False

# 장애물을 조합으로 설치해본 이후에 검사해줄 함수
def find_students_after_placing_object():
    for x,y in teachers: #튜플 전체
        for j in range(4):
            if watch(x,y,j): # 학생이 발견되었을때
                return True
            #else return False해버리면 나머지 for문 돌지 못함
    #for 문이 끝나고도 빠져나오지 못했다면:
    return False

# 학생이 아무도 감지되지 않았는가?에 대한 Flag
nobody = False

# 장애물을 조합으로 놓아보고 확인
# combinations는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우 계산.
# combinations는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용
# 결과 프린트할때는 이렇게 list(combinations(blanks,3))
for data in combinations(blanks,3):
    for tuple in data:
        graph[tuple[0]][tuple[1]] = "O"
        if not find_students_after_placing_object():
            nobody = True
            break
    for tuple in data:
        # 설치한 장애물 다시 없애기
        graph[tuple[0]][tuple[1]] = "X"
if nobody:
    print("YES")
else:
    print("NO")


    #for x,y in data:
    #    print(x,y)
#graph = [list(sys.stdin.readline().split()) for _ in range(n)]
# for i, line in enumerate(graph):
#     if "T" in line:
#         teacher.append([i,line.index("T")])
#
# queue = deque()
# queue.append(teacher[0])
#
# def bfs(x,y):
#     dx = [0,0,1,-1]
#     dy = [1,-1,0,0]
#     while queue:
#         T_now = queue.popleft()
#         T_next = copy.deepcopy(T_now)
#         for i in range(len(dx)):
#             T_next[0] = T_now[0] + dx[i]
#             T_next[1] = T_now[1] + dy[i]
#             print(T_next)
#
# bfs(0,0)