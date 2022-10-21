'''
Implement a function that adds two numbers together and returns 
their sum in binary. The conversion can be done before, or after the addition.
The binary number returned should be a string.

'''
def add_binary(a,b):
    result = ''
    numb = a+b
    while numb > 0:
        result = str(numb % 2) + result
        numb = numb // 2
    return result

#Подсмотренные варианты

def add_binary_1(a,b):
    return bin(a+b)[2:]       #Такой синтаксис работает только с bin?

def add_binary_2(a,b):
    return '{0:b}'.format(a + b)   #Этот код и следующий не понимаю

def add_binary_3(a,b):
    return f"{a + b:b}"


if __name__ == '__main__':
    print(add_binary(1,9))
    print(add_binary_1(1,9))
    print(add_binary_2(1,9))
    print(add_binary_3(1,9))
