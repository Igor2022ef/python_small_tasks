from FuuzBuzz import *
from sum_numbers import sum_numbers
from fibonacci_numbers import *
from is_prime import is_prime
from add_binary import *
from make_str_not_Empty import make_str_not_Empty
from others import *
from dictionaries_tasks import *

def main():

# From single scripts
    FizzBuzz()
    var_1()
    var_2()
    sum_numbers(-10)
    fibonacci_numbers(0, 1)
    fibonacci_numbers_1(0, 1)
    is_prime(73)
    add_binary(1, 9)
    add_binary_1(1, 9)
    add_binary_2(1, 9)
    add_binary_3(1, 9)
    make_str_not_Empty('oijgoeqh uhgqeih')

# From others
    spin_words_more_5_letters("Just liked the name of this Kata")
    create_phone_number([4939586871])
    to_weird_case('Stay with me')
    caesar_code('Do not forget the material')
    find_even_index([5,4,3,2,3,4,5])
    line_reversal('Just liked the name, as Kata')
    move_zeros([0,200,0,15,0,0,23,12,0,0,5])
    alphanumeric('p1as4sWoR9d')
    recoding_10_16(9, 14, 178)
    pick_peaks([2,4,78,11,27,12,5,34,35,38,5])
    list_ordering([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])

# From dictionaries_tasks
    dictionary_maker([54, 10, 23, 'condition', 5, 18, 'start', 3, 6, 'second', 8, 'foo'])

if __name__ == '__main__':
    main()