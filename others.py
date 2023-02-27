'''
Всего 11 различных задачи
'''

'''
Write a function that takes in a string of one or more words, 
and returns the same string, but with all five or more letter words reversed 
(Just like the name of this Kata). Strings passed in will 
consist of only letters and spaces. Spaces will be included 
only when more than one word is present.
'''

def spin_words_more_5_letters(sentence):
    res = []
    words = sentence.split()
    x = [res.append(i[::-1]) if len(i) >= 5 else res.append(i) for i in words] 
    print( " ".join(res))

'''
Write a function that accepts an array of 10 integers (between 0 and 9), that returns
a string of those numbers in the form of a phone number.
'''
#Мой вариант

def create_phone_number(n:list):
    if len(n) < 10:
       c = [n.append(0) for i in range(10 - len(n))]
    p = ''.join(map(str, n))
    print( f"({p[:3]}) {p[3:6]}-{p[6:10]}")


'''
Функция получает строку и возвращает строку в которой четные знаки в словах
стали - Заглавными, нечетные - сторочными.
Нулевой индекс четный, и вам нужно начинать заново для каждого слова.

Передаваемая строка будет состоять только из букв алфавита и пробелов (' '). 
Пробелы будут присутствовать только в том случае, если слов несколько. 
Слова будут разделены одним пробелом (' ').
'''

def to_weird_case(words):
    d=[]
    y = words.split()
    for i in y:
        j=list(map(str, str(i)))
        c=[j[n].title() if n==0 or n%2==0 else j[n].lower() for n in range(len(j))]
        d.append(''.join(c))
    print( ' '.join(d))

'''
Вариация кода Цезаря.
Принимаем на вход строку - латиница и любые символы.
Перекодируем только латиницу на 13 позиций по алфавиту, 
  любые символы оставляем, как есть. Замечание - литеры могут быть, как 
  строчными, так и заглавними.
Возвращаем строку
'''
def caesar_code(message):
    l_1 = list(map(str,message))
    al = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    x=list(map(str,al))
    res=[]
    for i in range(len(message)):
        match (l_1[i] in al):
            case False:
                res.append(l_1[i])
            case True:
                tr=x.index(l_1[i])
                res.append(x[tr+26]) if (tr+26)<=51 else res.append(x[(tr+25)-51])

    return "".join(res)

'''
Получаем массив точных чисел. 
Возвращаем номер числа такого, что сумма всех чисел слева от него равна сумме всех чисел справа от него.
Если такого числа нет в исходном списке, то возвращается -1
'''

def find_even_index(arr):
    i = 0
    while i < (len(arr)):
        if sum(arr[:(i)]) != sum(arr[(i+1):]):
                i += 1
        else:
            return i
    return -1

'''
Принимаем на вход строку латиницы со знаками препинания.
Возвращаем строку латиницы изменив каждое слово, так что первая буква 
становится последней и после нее добавляется ay
Замечание: знаки препинания на входе, отделены от слов пробелом. Знаки 
препинания возвращаются "как есть" без добавлений.
'''
def pig_it(text):
    return " ".join(i[1:]+i[:1]+"ay" if i.isalnum() else i for i in text.split())

'''
Получаем список, возвращаем список в котором все нули убраны после всех 
чисел. Порядок чисел не изменен
'''
#Мой вариант:

def move_zeros(lst):
    x=[]
    y=[]
    res=[y.append(i) if i==0 else x.append(i) for i in lst]
    return x+y


#Не мой вариант, но красивый:

    return [x for x in lst if x] + [0] * lst.count(0)

'''
В этом примере вы должны проверить, является ли строка ввода пользователя 
буквенно-цифровой. Данная строка не является nil/null/NULL/None, поэтому 
вам не нужно это проверять.

Строка должна быть буквенно-цифровой при соблюдении следующих условий:

Хотя бы один символ ("" недействителен)
Допустимые символы: прописные/строчные латинские буквы и цифры от 0 до 9.
Без пробелов/подчеркивания
'''
'''
Для этой задачи есть не мой вариант с подключением бибилотеки
import string
Решение под комментами

'''

def alphanumeric(password):
    al = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789"
    return (False if list(password)==[] else all([True if i in al else False for i in list(password)]))
    # return (False if list(password)==[] else all([True if i in (string.ascii_letters+digits) else False for i in list(password)]))

'''
Перекодировка массива rgb. Дан массив из трех десятичных чисел. Каждое из чисел перекодировать в шестнадцатиричную систему
исчисления и результат представить в виде единой строки.
'''

def recoding_10_16(r,g,b):
    y=[r,g,b]
    x = ['A', 'B', 'C', 'D', 'E', 'F']
    res = []
    for i in y:
        if i<0:
            i=0
        if i>255:
            i=255
        c=i//16
        if 0<=c<=9:
            res.append(c)
        elif 10 <=c<= 15:
            res.append(x[c - 10])
        if 0 <= (i - (c * 16)) <= 9:
            res.append(i-(c*16))
        elif 10<=(i-c*16)<=15:
            res.append(x[((i-c*16)-10)])
    return "".join(map(str, res))

# Ниже вариант красивый, но не мой. Со строкой-формат разбираться не стал.

# def limit(num):
#     if num < 0:
#         return 0
#     if num > 255:
#         return 255
#     return num
#
# def rgb(r, g, b):
#     return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))

'''
Нахождение локальных максимумов списка. Ответ: массив из номеров позиций максимумов в исходном списке и соответственно
самих значений максимумов {'pos': [...], 'peaks': [...]}. Первый и последний элементы массива не будут считаться пиками.
Также проблемма-плато. [1, 2, 2, 2, 1] имеет пик, а [1, 2, 2, 2, 3] и [1, 2, 2, 2, 2] — нет. 
В случае плато-пика, возвращается только положение и значение начала плато.
'''
def pick_peaks(arr):
    pos = []
    peaks = []
    res={'pos':pos, 'peaks':peaks}
    i=0
    while i<(len(arr)-2):
        i+=1
        if arr[i-1]<arr[i] and arr[i+1]<arr[i]:
            pos.append(i)
            peaks.append(arr[i])
        elif arr[i+1]==arr[i]:
            j=i
            while arr[i+1]==arr[i] and i!=len(arr)-2:
                i+=1
            if arr[i+1]<arr[i] and arr[j-1]<arr[j]:
                pos.append(j)
                peaks.append(arr[j])
    return res

'''
Формат для выражения упорядоченного списка целых чисел заключается в использовании:

Списка, разделенного запятыми, либо
Дтдельные целые числа
Диапазон целых чисел, обозначенный начальным целым числом, отделенным от конечного целого числа в диапазоне дефисом «-».
 Диапазон включает все целые числа в интервале, включая обе конечные точки. Он не считается диапазоном,
 если он не охватывает как минимум 3 числа. Например "12,13,15-17"

Завершите решение так, чтобы оно принимало список целых чисел в порядке возрастания и возвращало правильно
 отформатированную строку в формате диапазона.

Пример:

раствор([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# возвращает "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
'''
def list_ordering(args):
    l_2 = []
    l_res=[]
    l_res1 = []
    l_3 = ''
    for i in range(len(args)):
        if i<(len(args)-1) and (abs(args[i]-args[i+1])==1):
            l_2.append(args[i])
            continue
        elif i<(len(args)-1) and abs(args[i] - args[i+1])!=1 and abs(args[i] - args[i-1])==1:
            l_2.append(args[i])
        elif i==(len(args)-1) and abs(args[i] - args[i-1])==1:
            l_2.append(args[i])
        if len(l_2) > 2:
            l_3 = f"{l_2[0]}-{l_2[len(l_2) - 1]}"
            l_res.append(l_3)
            l_2=[]
            l_3=''
        elif len(l_2)==2:
                l_res=(l_res+l_2)
                l_2 = []
        elif len(l_2)==0:
            l_res.append(args[i])
    return "".join([str(_)+"," for _ in l_res])[:-1]