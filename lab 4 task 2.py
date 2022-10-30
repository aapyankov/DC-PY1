def get_percentage(char_dict):
    sum = 0
    for v in char_dict.values():
        sum += v
    for key in char_dict.keys():
        char_dict[key] /= sum
    return char_dict

def get_count_char(str_):
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_
    char_dict = {}
    l = len(str_)
    for i in range(l):
        char = str_[i].lower()
        if char.isalpha() == True:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(get_percentage(get_count_char(main_str)))