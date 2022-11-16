'''
Всего 3 различные задачи
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
a string of those
numbers in the form of a phone number.
'''
#Мой вариант

def create_phone_number(n:list):
    if len(n) < 10:
       c = [n.append(0) for i in range(10 - len(n))]
    p = ''.join(map(str, n))
    return f"({p[:3]}) {p[3:6]}-{p[6:10]}"


   #Подсмотренные варианты

# def create_phone_number1(n1):
#     return "({}{}{}) {}{}{}-{}{}{}{}".format(*n1)

def create_phone_number2(n2):
    if len(n2) < 10:
        c = [n2.append(0) for i in range(10 - len(n2))]
    n2 = ''.join(map(str,n2))
    return "(%s) %s-%s" % (n2[:3], n2[3:6], n2[6:])


if __name__ == "__main__":
    sentence = 'Sally sells sea shells by the sea shore'
    print(spin_words(sentence))
    print(create_phone_number([0, 0, 1,3,4,5,6,7,8,9]))
#    print(create_phone_number1([0, 0, 1]))
    print(create_phone_number2([0, 0, 1,3,4,5,6,7,8,9]))

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