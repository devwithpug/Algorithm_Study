# goorm / 기타 / 시침과 분침
# https://level.goorm.io/exam/43176/%EC%8B%9C%EC%B9%A8%EA%B3%BC-%EB%B6%84%EC%B9%A8/quiz/1

hour, minute = map(int, input().split(":"))

h_p = 30 * hour + minute * 0.5
h_p = 360.0 if h_p == 0 else h_p
m_p = minute * 6.0
m_p = 360.0 if m_p == 0 else m_p

print("{:.2f}".format(h_p - m_p if h_p > m_p else m_p - h_p))