# В строке удалить все буквы "а"  и подсчитать количество удаленных символов

def remove_and_count_letter(text, letter='a'):
    return text.count(letter), text.replace(letter, '')


print(remove_and_count_letter('a string with three a letters for example'))
