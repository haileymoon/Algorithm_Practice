# 효율성 문제 통과하지 못함
# def solution(phone_book):
#     answer = True
#     phone_book.sort(key = len)
    
#     for i in range(len(phone_book)):
#         for j in range(i+1, len(phone_book)):
#             if phone_book[i] == phone_book[j][:len(phone_book[i])]:
#                 answer = False
#                 return answer
    
#     return answer
 
 
def solution(phone_book):
    answer = True
    phone_dict = set()
    for num in phone_book:
        phone_dict.add(num)
        
    for key in phone_dict:
        temp = ""
        for num in key:
            temp+= num
            if temp in phone_dict and temp != key:
                answer = False
    return answer
