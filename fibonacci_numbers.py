#Генератор чисел Фибоначи

#Мой вариант

def fibonacci_numbers(border, i,j):
    res=[i,j]
    while j<border:
        s=i+j
        res.append(s)
        i=j
        j=s
    print(f"fibonacci_numbers MY: {res}")

#Подсмотренные варианты


def fibonacci_numbers_1(border_1, a,b):
    ans = []
    for c in range(border_1):
        b, a = a, a+b
        ans.append(a)
    print (f"fibonacci_numbers NOT MY: {ans}")
    print(f"{50*'*'}")
