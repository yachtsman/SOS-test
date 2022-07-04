# Task #3

# Cкрипт, который генерирует текстовый файл и наполняет его случайными числами.
# Количество строк передается из командной строки.

import random

file = open("Random_num.txt", "w" )

num_lines = int(input('How many lines would you like to generate?: '))
for i in range(num_lines):
    numbers = random.sample(range(1, 50), 10) # let it be 10 numbers per line
    lines = ' '.join([str(num) for num in numbers]) + '\n'
    file.write(lines)
    # print(lines) # to check the lines

file.close()

# Cкрипт, принимающий из командной строки число, 
# количество последних строчек, которые нужно прочесть из файла и вывести в консоль.

file_r = open("Random_num.txt", "r")

lines_read = int(input('How many last lines would you like to read?: '))
last_lines = file_r.readlines()
last_lines = last_lines[-lines_read:]
last_lines = '\n'.join([str(line) for line in last_lines])
print(last_lines)
file_r.close()