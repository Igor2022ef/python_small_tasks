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


if __name__ == "__main__":
    sentence = 'Sally sells sea shells by the sea shore'
    print(spin_words(sentence))
