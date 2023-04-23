'''
У нас есть список с чередованием строк и чисел. Необходимо из списка создать
 словарь, где ключами будут строки, а значениями - списки из чисел.
'''



def dictionary_maker(example_1):
    d = dict()
    empty = None
    bufer = []
    for i in example_1:
        if isinstance(i, str):
            d[i] = []
            empty = i
            d[i] = bufer
            bufer = []
        else:
            if len(d) == 0:
                bufer.append(i)
            else:
                d[empty].append(i)
    if len(d) == 0:
        d[''] = bufer
    print(d)


# if __name__ == '__main__':
#     example_1 = [54, 10, 23, 'condition', 5, 18, 'start', 3, 6, 'second', 8, 'foo']
#     example_2 = [54, 10, 23, 8]
#
#     print(dictionary_maker(example_1))
#     print(dictionary_maker(example_2))
