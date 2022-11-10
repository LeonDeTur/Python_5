# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

test = 'Попал в просак баклан в будний день, что не был солнечным тогда.'

def Find_ABC_in_text (text, index):
    for index in range(len(text)):
        if (text[index] == 'А') | (text[index] == 'а') | (text[index] == 'Б') | (text[index] == 'б') | (text[index] == 'В') | (text[index] == 'в'):
            return index
    return -1
def Find_indexes_of_word (index_letter, text):
    while (text[index_letter].isalpha()) and (index_letter > 0):
        index_letter -= 1
    index_start = index_letter
    index_letter += 1
    while text[index_letter].isalpha() & index_letter >= 0:
        index_letter += 1
    index_end = index_letter

    return [index_start, index_end]

def Fill_with_empty (text, indexes_list):
    text_list = list(text)
    _ = indexes_list[1]
    while _ in range(indexes_list[1], indexes_list[0]):
        text_list.pop(_)
        indexes_list[0] -= 1
    text = ''.join(text_list)
    return text

def Clean_text (text, index):
    if index != len(text) - 1:
        index = Find_ABC_in_text (text, 0)
        if index == -1:
            return text
        tmp_list = Find_indexes_of_word(index, text)
        Fill_with_empty(text, tmp_list)
        index = tmp_list[0]
        Clean_text(text, index)
    return text

print(Clean_text(test, 0))
print(test[0])



