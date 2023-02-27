#Генератор чисел Фибоначи

#Мой вариант

def gen_f_1(i,j):
    t=[i,j]
    while j<50:
        s=i+j
        t.append(s)
        i=j
        j=s
    return t

#Подсмотренные варианты


def gen_f(a,b):
    ans = []
    c = 0
    while c < 11:
        b, a = a, a+b
        c = c + 1
        ans.append(a)
    del ans[0]
    return (ans)

if __name__ == "__main__":
    print(gen_f(0,1))
    print(gen_f_1(0, 1))
