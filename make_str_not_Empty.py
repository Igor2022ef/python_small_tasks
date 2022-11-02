'''
Make str. Is not longer than 140 points and is not empty. And so on...
'''

def generate_hashtag(s:str):
    if s != "" and s.isspace() is not True and len(s) <= 140:
        return ("#" + s).title().replace(" ", "")
    else:
        return False


if __name__ == '__main__':
    print(generate_hashtag('oijgoeqh uhgqeih'))