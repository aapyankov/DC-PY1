def delete(list_, index =None):
    # TODO реализовать функцию удаления элемента из списка по индексу
    list_1 = []
    list_2 = []
    if index == None:
        index = len(list_)
        list_1 = list_[0:index - 1]
    else:
        list_1 = list_[0:index]
        list_2 = list_[index + 1:]
    return list_1 + list_2
print(delete([0, 0, 1, 2], index=0))
print(delete([0, 1, 1, 2, 3], index=1))
print(delete([0, 1, 2, 3, 4, 4]))
