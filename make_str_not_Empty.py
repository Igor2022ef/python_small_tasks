'''
Make str. Is not longer than 140 points and is not empty. And so on...
'''

def make_str_not_Empty(s:str):
    if s != "" and s.isspace() is not True and len(s) <= 140:
        print (f"make_str_not_Empty: {('#' + s).title().replace(' ', '')}")
    else:
        print(f"make_str_not_Empty: {False}")
