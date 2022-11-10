# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

test = (input('Введите текст на русском языке: '))

def Find_ABC_in_text (text, index):
    for index in range(len(text)):
        if (text[index] == 'А') | (text[index] == 'а') | (text[index] == 'Б') | (text[index] == 'б') | (text[index] == 'В') | (text[index] == 'в'):
            return index
    return -1

def Find_indexes_of_word (index_letter, text):
    tmp = index_letter
    while (1072 <= ord(text[index_letter]) <= 1103) and (index_letter > 0):
        index_letter -= 1
    index_start = index_letter
    index_letter = tmp
    while (1072 <= ord(text[index_letter]) <= 1103) and (index_letter >= 0):
        index_letter += 1
    index_end = index_letter

    return [index_start, index_end]

def Clean_text (text, index):
    while index != -1:
        index = Find_ABC_in_text (text, index)
        tmp_list = Find_indexes_of_word(index, text)
        text = text[:tmp_list[0]] + text[tmp_list[1]:]
        index = tmp_list[0]
    return text

print('Текст, без слов с буквами а,б,в: ' + Clean_text(test, 0))



