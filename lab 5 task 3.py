import random

def get_unique_list_numbers() -> list[int]:
    ...  # TODO написать функцию для получения списка уникальных целых чисел
    random_list = list()
    random_start = -10
    random_end = 10
    while len(set(random_list)) < 15:
        random_list.append(random.randint(random_start, random_end))
    return list(set(random_list))

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
