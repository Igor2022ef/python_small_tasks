'''
Мой вариант
'''
print([ str('Fizz') if (i % 3 == 0 and i % 5 != 0) else i and  str('Buzz')
 if (i % 5 == 0 and i % 3 != 0) else i and  str('FizzBuzz')
if (i % 3 == 0 and i % 5 == 0)  else i for i in range(1,101,1)])

'''
Подсмотренный вариант
'''
