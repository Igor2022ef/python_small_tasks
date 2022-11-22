'''
Всего 4 различные задачи
'''

'''
Write a function that takes in a string of one or more words, 
and returns the same string, but with all five or more letter words reversed 
(Just like the name of this Kata). Strings passed in will 
consist of only letters and spaces. Spaces will be included 
only when more than one word is present.
'''

def spin_words(sentence):
    res = []
    words = sentence.split()
    x = [res.append(i[::-1]) if len(i) >= 5 else res.append(i) for i in words] 
    return " ".join(res)

'''
Write a function that accepts an array of 10 integers (between 0 and 9), that returns
a string of those numbers in the form of a phone number.
'''
#Мой вариант

def create_phone_number(n:list):
    if len(n) < 10:
       c = [n.append(0) for i in range(10 - len(n))]
    p = ''.join(map(str, n))
    return f"({p[:3]}) {p[3:6]}-{p[6:10]}"


if __name__ == "__main__":
    sentence = 'Sally sells sea shells by the sea shore'
    print(spin_words(sentence))
    print(create_phone_number([0, 0, 1,3,4,5,6,7,8,9]))

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
    return ' '.join(d)

'''
Вариация кода Цезаря.
Принимаем на вход строку - латиница и любые символы.
Перекодируем только латиницу на 13 позиций по алфавиту, 
  любые символы оставляем, как есть. Замечание - литеры могут быть, как 
  строчными, так и заглавними.
Возвращаем строку
'''
def rot13(message):
    l_1 = list(map(str,message))
    al = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    x=list(map(str,al))
    i = -1
    res=[]
    while(i<len(message)-1):
        i+=1
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

def find_even_index(arr: list(int)):
    i = 0
    while i < (len(arr)):
        if sum(arr[:(i)]) != sum(arr[(i+1):]):
                i += 1
        else:
            return i
    return -1


if __name__ == '__main__':
    arr = [1,2,3,4,3,2,1]
    print(find_even_index(arr))