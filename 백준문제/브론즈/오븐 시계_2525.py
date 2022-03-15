# 시작하는 시간과 오븐에 필요한 시간, 끝나는 시간:?
h_now, m_now = map(int, input().split())
minutes = int(input())

h_later = (h_now+((m_now+minutes)//60)) % 24
m_later = (m_now+minutes) % 60
print(h_later, m_later)