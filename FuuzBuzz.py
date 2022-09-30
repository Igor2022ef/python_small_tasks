'''
Много вариантов: https://habr.com/ru/post/593489/
Мой вариант
'''
# print([ str('Fizz') if (i % 3 == 0 and i % 5 != 0) else i and  str('Buzz')
#  if (i % 5 == 0 and i % 3 != 0) else i and  str('FizzBuzz')
# if (i % 3 == 0 and i % 5 == 0)  else i for i in range(1,101,1)])         # Как это красиво записать?

'''
Подсмотренный вариант
'''
print([str('FizzBuzz') if i % 3 == 0 and i % 5 == 0 else str('Fizz') if i % 3 == 0 else str('Buzz') if i % 5 == 0
       else i for i in range(1,101)])
#[print('FizzBuzz'[4 if i%3 else 0:4 if i%5 else 8] or i) for i in range(1, 101)]

i=1
while i < 10:
    print('МалоТонн'[4 if i%3 else 0:4 if i%5 else 8] or i) # Почему в этом варианте можно писать  i%3 без условий?
    i += 1









