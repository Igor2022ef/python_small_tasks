'''
It returns the sum of all the multiples of 3 or 5 below the number passed in.
Additionally, if the number is negative, return 0.
'''


def sum_numbers(i):
    res = [i if (i>=0 and (i % 3 == 0 or i % 5 == 0)) else 0 for i in range(i,25,1)]
    print(f"{50 * '*'}")
    print (f"sum_numbers: {res}, 'sum(sum_numbers)': {sum(res)}")
    print(f"{50 * '*'}")

