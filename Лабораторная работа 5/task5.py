#Написать функцию для генерации случайных паролей заданной длины n (по умолчанию 8 символов).
#В качестве алфавита следует использовать: буквы верхнего (A-Z) и нижнего регистра (a-z), цифры (0-9).
#Для того чтобы сгенерировать случайную выборку, следует использовать функцию sample из модуля random.

import string
from random import sample

def get_random_password(n=8) -> str:
    chars = sample(string.digits + string.ascii_lowercase + string.ascii_uppercase, n)
    return "".join(chars)

print(get_random_password())
