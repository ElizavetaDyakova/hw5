# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.


import re
line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'
#решение с re
pattern = r"(?=([a-z]{1})[A-Z]+([a-z]{1}))"
result = re.findall(pattern, line)

print("Решение с re:")
print(result)


# решение без использования re
def circledChars(line):
       w = []
       lowers = [y for y in range(len(line)) if (line[y].islower())]  # позиции символов в нижнем регистре
       for i in range(0, len(lowers) - 1):
              if ((lowers[i + 1] - lowers[i]) > 1):
                     tup = (line[lowers[i]], line[lowers[i + 1]])
                     w.append(tup)
       return w


print("Решение без re:")
print(circledChars(line))



# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
     'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
     'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
     'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
     'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
     'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
     'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
     'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
     'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
     'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
     'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
     'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
     'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
     'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
     'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

#решение с re
patterni = r"(?=[a-z]{2}([A-Z]+)[A-Z]{2})"
r"(?=([a-z]{1})[A-Z]+([a-z]{1}))"
resulti = re.findall(patterni, line_2)

print("Решение с re:")
print(resulti)

#решение без re
symbol1 = list(map(lambda x: chr(x), list(range(65, 91))))  # Преобразуем в список букв A-Z
symbol2 = list(map(lambda x: chr(x), list(range(97, 123))))  # Преобразуем в список букв a-z
line_new = list(line_2)

lst = []
i = len(line_new) - 1
# Находим  символ в верхнем регистре после которого стоят еще два символа в верхнем регистре
while i >= 0:
    if line_new[i] in symbol2:
        lst.append(line_new[i])
    elif line_new[i] in symbol1 and i <= len(line_new) - 3 and line_new[i + 1] in symbol1 and line_new[
        i + 2] in symbol1:
        lst.append(line_new[i])
    else:
        lst.append(' ')
    i -= 1
lst.reverse()  # Переворачиваем список

i = 0
lst2 = []
registr = True  # Начальное условие поиска сортировки символов в верхнем регистре
# Фильтрация списка.
while i <= len(lst) - 1:
    if lst[i] in symbol2:
        registr = True
    if lst[i] in symbol1 and lst[i - 1] in symbol2 and lst[i - 2] in symbol2:
        lst2.append(lst[i])
        registr = False
    elif lst[i] in symbol1 and registr == False:
        lst2.append(lst[i])
    else:
        lst2.append(' ')
    i += 1
stroka = ''.join(lst2).split(' ')  # Преобразование в строку и разбиение по пробелам

line_str_3 = [i for i in stroka if i != '']  # Формирование выхрдного списка из строки
print('Список без использованием модуля re: \n', line_str_3)

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import random
import re
#запись чисел в файл
with open('file.txt', 'w') as f:
    for _ in range(2500):
        f.write(str(random.randint(0, 9)))
#поиск самой длинной последовательности одинаковых чисел
with open('file.txt', 'r') as f:
    long = list()
    number = f.read()
    print(number)
    for n in range(0, 10):
        if str(n) in number:
            lst = re.findall('[%s]+' % n, number)
            long.append(max(lst, key=len))
    result = max(long, key=len)
    print('max= ', result)