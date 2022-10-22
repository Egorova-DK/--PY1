# ТЕКСТ ЗАДАНИЯ:
#    Определить, как часто встречается определенная буква в строке.
# 1. Создайте словарь, в который в качестве ключа будет использоваться символ,а в качестве значения, количество раз, сколько этот элемент встречался в строке.
# 2. Напишите функцию, которая будет принимать строку, а возвращать словарь с частотой каждого символа.
# 3. Чтобы не считать символы разного регистра два раза, с помощью метода строки lower перевести строку в нижний регистр
# 4. С помощью метода строки isalpha проверяем, что символ является буквой.
# 5. Напишите вторую функцию, которая принимает словарь символов. Функция должна вернуть новый словарь, где количество каждого элемента заменено на процентное отношение ко всем символам.

def get_count_char(proposal):
    char_count = {}
    DEFAULT_COUNT = 0
    proposal = proposal.lower()
    for char in proposal:
        if char.isalpha():
            char_count[char] = char_count.get(char, DEFAULT_COUNT) + 1
    return char_count

#Так как я не очень поняла условие 5 пункта,то решила сделать две функции: одна высчитывает процент символа ко всем, а другая находит долю символа.
def get_percentage_of_chars(chars_count: dict):
    dict_new = {}
    length = len(chars_count)
    for char in chars_count:
        dict_new[char] = (chars_count.get(char) / length) * 100
    return dict_new


def get_percentage_of_chars_2(chars_count: dict):
    dict_new = {}
    total = sum(chars_count.values())
    for char in chars_count:
        dict_new[char] = (chars_count.get(char) / total) * 100
    return dict_new


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(get_percentage_of_chars(get_count_char(main_str)))
print(get_percentage_of_chars_2(get_count_char(main_str)))
