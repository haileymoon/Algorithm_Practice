# "JEROEN"	56
# 기본으로 A에서 시작, 한 문자가 끝나고 넘어갈때도 +1횟수
# 최소획수를 찾는거고 Z에서 A를 가는거면 A에서 한번 움직여도 됨. 반띵해서 밑으로 갈껀지 위로 갈껀지 체크
# a랑 z빼고는 원래대로하면 됨
name = "BABBAAAB"

def solution(name):
    count = 0
    move_count = len(name) - 1  # 마지막이 연속된 A로 끝나는 경우 처리가 필요
    
    while name[move_count] == "A" and move_count > 0:
        move_count -= 1
        
    if move_count == 0:
        return count
    

    for idx, letter in enumerate(name):
        count += min(ord(letter) - ord("A"), ord("Z") - ord(letter) + 1)
        next = idx + 1
        while next < len(name) and name[next] == "A":
            next += 1
        move_count = min(move_count, idx + idx + len(name) - next)
    count += move_count
    return count


if __name__ == "__main__":
    print(solution(name))

    
    
    

    
    
