import time
'''
Напишите программу, печатающую числа от 1 до 100. 
Вместо чисел кратных трём, программа должна печатать 'Fizz'. 
Вместо чисел кратных пяти - 'Buzz'. 
Если число кратно и трём, и пяти, программа должна печатать 'FizzBuzz'.
'''

def time_make(func):
    def wrapper(*args,**kwargs):
            start_time = time.perf_counter_ns()
            res = func(*args,**kwargs)
            '''
                                                        ВОПРОС: Как вставить в строку ниже название текущей функции??????
            '''

            print(f'Время работы функции {func}: {time.perf_counter_ns() - start_time}')
            return res
    return wrapper

#Мой вариант

@time_make
def FizzBuzz():
    print ([
            'Fizz' if (i % 3 == 0 and i % 5 != 0) else i and
            'Buzz' if (i % 5 == 0 and i % 3 != 0) else i and
            'FizzBuzz' if (i % 3 == 0 and i % 5 == 0) else i
            for i in range(1, 101, 1)
        ])
'''
# Подсмотренные варианты
# '''
@time_make
def var_1():
        add = ([str('FizzBuzz') if i % 3 == 0 and i % 5 == 0 else str('Fizz') if i % 3 == 0
                                else str('Buzz') if i % 5 == 0 else i
                for i in range(1,101)])
        return add

@time_make
def var_2():
    return [('FizzBuzz'[4 if i%3 else 0:4 if i%5 else 8] or i) for i in range(1, 101)]


@time_make
def var_3():
        i=1
        while i < 10:
            print('FizzBuzz'[4 if i%3 else 0:4 if i%5 else 8] or i)
            i += 1



