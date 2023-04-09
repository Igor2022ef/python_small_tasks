#Генератор чисел Фибоначи

#Мой вариант

def fibonacci_numbers(i,j):
    t=[i,j]
    while j<50:
        s=i+j
        t.append(s)
        i=j
        j=s
    print(f"fibonacci_numbers MY: {t}")

#Подсмотренные варианты


def fibonacci_numbers_1(a,b):
    ans = []
    c = 0
    while c < 11:
        b, a = a, a+b
        c = c + 1
        ans.append(a)
    del ans[0]
    print (f"fibonacci_numbers NOT MY: {ans}")
    print(f"{50*'*'}")
