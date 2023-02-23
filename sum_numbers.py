'''
It returns the sum of all the multiples of 3 or 5 below the number passed in.
Additionally, if the number is negative, return 0.
'''


def solution(i):
    res = [i if (i>=0 and (i % 3 == 0 or i % 5 == 0)) else 0 for i in range(i,25,1)]
    return res, sum(res)

if __name__ == '__main__':
	print(solution(-10))