# goorm / 기타 / Palindrome
# https://level.goorm.io/exam/43233/거꾸로-해도-이효리-palindrome/quiz/1

def is_palindrome(line):
	line = list(line)
	
	for i in range(int(len(line)/2)):
		if line[i] != line[-(i+1)]:
			return False
	
	return True


line = input()

print("Palindrome" if is_palindrome(line) else "Not Palindrome")