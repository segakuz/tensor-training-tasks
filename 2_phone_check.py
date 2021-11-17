'''Проверить, что номера телефонов состоят только из цифр. Они могут начинаться с «+», цифры
могут быть разделены пробелами и дефисами «-»
Например: 8-999-777-1111, +7 999 333 2222, +7 999-555-11-11'''

import re


def phone_check(phone):

    return True if re.search('^(8|\\+?7)[- ]?\\d{3}[- ]?\\d{3}[- ]?\\d{2}[- ]?\\d{2}$', phone) else False


print(phone_check('8-999-777-1111'))
print(phone_check('+7 999 333 2222'))
print(phone_check('+7 999-555-11-11'))
print(phone_check(' 999-555-11-11'))
print(phone_check('999-abc'))
