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

def create_phone_number(n: list):
    if len(n) < 10:
        c = [n.append(0) for i in range(10 - len(n))]
        return f"({(''.join(map(str, n[:3])))}) {(''.join(map(str, n[3:6])))}-{(''.join(map(str, n[6:10])))}"

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
    print(create_phone_number([0, 0, 1]))
#    print(create_phone_number1([0, 0, 1]))
    print(create_phone_number2([0, 0, 1]))
