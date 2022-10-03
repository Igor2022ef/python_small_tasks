import time
'''
Вопросы:
1. Постоянно вылезает None при реализации кода, как отыскать откуда
2. Если реализовать код в моем методе иначе т.е.       
            if a == 1:
                b = Функция расчета
            else:
                print("Не знаю, что")
    то начинает выдавать иное время работы, (вроде не верное), как проверить?
2.1 Мой вариант основной функции, который под комментами тоже дает не верное время, как проверить?
2.2 Варианты с print дают время медленнее чем с return - почему?
3. В моем варианте в основной функции строка else не понятно зачем?
4. Не знаю, как в основной функции задать условие начала работы функции.
'''


#Много вариантов: https://habr.com/ru/post/593489/

def time_make(func):
    def wrapper(a):
        if a == 1:
            start_time = time.perf_counter_ns()
            res = func(a)
            print(f'Время работы функции: {time.perf_counter_ns() - start_time}')
            return res
        else:
            print("Не вышло")
    return wrapper

#Мой вариант

@time_make
def FizzBuzz(a):
    if a > 0:
        print(([str('Fizz') if (i % 3 == 0 and i % 5 != 0) else i and str('Buzz')
        if (i % 5 == 0 and i % 3 != 0) else i and str('FizzBuzz')
        if (i % 3 == 0 and i % 5 == 0) else i for i in range(1, 101, 1)]))
#        return b

        # return (([str('Fizz') if (i % 3 == 0 and i % 5 != 0) else i and str('Buzz')
        # if (i % 5 == 0 and i % 3 != 0) else i and str('FizzBuzz')
        # if (i % 3 == 0 and i % 5 == 0) else i for i in range(1, 101, 1)]))

    else:
        print("Не знаю, что")

'''
# Подсмотренные варианты
# '''
@time_make
def var_1(a):
    if a > 0:
        add = ([str('FizzBuzz') if i % 3 == 0 and i % 5 == 0 else str('Fizz') if i % 3 == 0 else str('Buzz') if i % 5 == 0
            else i for i in range(1,101)])
        return add
    else:
        print("Не знаю, что")

@time_make
def var_2(a):
    if a > 0:
        [print('FizzBuzz'[4 if i%3 else 0:4 if i%5 else 8] or i) for i in range(1, 101)]
    else:
        print("Не знаю, что")

@time_make
def var_3(a):
    if a > 0:
        i=1
        while i < 10:
            print('FizzBuzz'[4 if i%3 else 0:4 if i%5 else 8] or i) # Почему в этом варианте можно писать  i%3 без условий?
            i += 1
    else:
        print("Не знаю, что")

if __name__ == '__main__':
    print(FizzBuzz(1))
    var_1(1)
    var_2(1)
    var_3(1)

