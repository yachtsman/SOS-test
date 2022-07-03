# Task #2

def compress(inp:str)->str:
    ''' 
    Функция сжатия строки на основе счетчика повторяющихся символов.
    Например, строка aabcccccaaa должна превратиться в а2b1с5аЗ.
    Если «сжатая» строка оказывается длиннее исходной, метод должен вернуть исходную строку.
    '''
    # concatenating the output(answer), counting the occurrence of letters
    ans = ''
    count = 1
    for i in range(len(inp)-1):
        if inp[i] == inp[i+1]:
            count += 1
        else:
            ans += (inp[i] + str(count))
            count = 1
    ans += (inp[i+1] + str(count))
    if len(ans) > len(inp):
        return(inp)
    else:
        return(ans)

# testing 

f = 'aabcccccaaa'
print('')
print(f'Usual case \ninput: {f}')
print('output:', compress(f))

g = 'aab'
print('')
print(f'When «compressed» string is longer then input \ninput: {g}')
print('output:', compress(g))