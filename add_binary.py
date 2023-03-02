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
    print(f"add_binary MY: {result}")

#Подсмотренные варианты

def add_binary_1(a,b):
    print(f"add_binary_2 NOT MY: {bin(a + b)[2:]}")

def add_binary_2(a,b):
    print(f"add_binary_2 NOT MY: {'{0:b}'.format(a + b)}")

def add_binary_3(a,b):
    print(f"add_binary_3 NOT MY: {a + b:b}")
    print(f"{50 * '*'}")


