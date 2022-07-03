# Task #1

def is_palindrome(string:str)->bool:
    ''' 
    Функция, определяющая, является ли одна строка перестановкой другой (полиндром).
    Под перестановкой понимаем любое изменение порядка символов.
    Регистр учитывается, пробелы являются существенными
    '''
    # creating a dictionary with an occurrence of letters from the input string
    allowed = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ' #in case of special charachters
    dic = {}
    for letter in string:
        if letter in dic.keys():
            dic[letter] += 1
        elif letter in allowed:
            dic[letter] = 1

    # counting letters in dictionary
    mid = ''
    for letter in dic:
        if mid and dic[letter] % 2 == 1:
            return False  
        elif dic[letter] % 2 == 1:
            mid = letter
    return True

# testing

p = 'eve'
print(is_palindrome(p))

o = 'eve '
print(is_palindrome(o))

n = 'evE'
print(is_palindrome(n))

m = 'Able was elbA, I swa'
print(is_palindrome(m))

l = 'Able was Elba, I saw'
print(is_palindrome(l))