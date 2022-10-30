'''
It returns the sum of all the multiples of 3 or 5 below the number passed in.
Additionally, if the number is negative, return 0.
'''


def solution(number:int):
	if number > 0:
		return sum([i for i in range(number) if i%3 == 0 or i%5 == 0])
	else:
		return 0

if __name__ == '__main__':
	print(solution(10))