# 다양한 수로 이루어진 배열이 있을 떄 주어진 수들을
# M번 더하여 가장 큰 수를 만드는 법칙
# 단, 특정 인덱스에 해당하는 수가 연속해서 k번을 초과해서 더해질 수 없음

# 핵심 아이디어: 가장 큰 수를 k번 반복하고 그 다음수 한번, 큰수 k번
# 핵심 아이디어 revised: 가장 큰 수와 두 번째로 큰수만 저장하고 반복되는 수열의 형태 파악
# ex) 34343 일때 M이 7, k가 2면 4+4+4+4+4+4+4
# 큰수와 값이 같은지 확인하면서 체크해주면 될듯


import sys

n, m ,k = list(map(int, sys.stdin.readline().split()))
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort(reverse = True)
sum = 0
first = numbers[0]
second = numbers[1]
# k가 2일 때 first, first, second 형식의 수열이 반복됨
# 즉, k+1만큼 반복되고 first를 몇번 더해주는지 찾아보면:
first_count = (m//(k+1) * k) + (m % (k+1))
second_count = m-first_count
sum += first_count * first
sum += second_count * second

print(sum)

#index = 0
#while True:
#    if m == 0:
#        break
#
#    elif numbers[index] == max(numbers):
#        for _ in range(k):
#            sum += numbers[index]
#            m -= 1
#            if m==0:
#                break
#        index += 1
#
#    else:
#        sum += numbers[index]
#        index -= 1
#        m -= 1
#print(sum)
#
