# Составить список словарей. Каждый словарь должен содержать в себе следующие пары ключ-значение:
# "dec" - десятичное число
# "bin" - двоичное число
# "oct" - восьмеричное число
# "hex" - шестнадцатеричное число
# TODO решить с помощью list comprehension и распечатать список с помощью функции pprint

from pprint import pprint
list_of_dictionaries = [{'dec': num, 'bin': bin(num), 'oct': oct(num), 'hex': hex(num)} for num in range(16)]

pprint(list_of_dictionaries)

