def delete(list_, index =None):
    # TODO реализовать функцию удаления элемента из списка по индексу
    list_1 = []
    list_2 = []
    if index == None:
        return list_[0:len(list_) - 1]
    elif abs(index) > len(list_):
        return list_
    else:
        if index < 0:
            index += len(list_)
        list_1 = list_[0:index]
        list_2 = list_[index + 1:]
        return list_1 + list_2

print(delete([0, 0, 1, 2], index=0)) # [0, 1, 2]
print(delete([0, 1, 1, 2, 3], index=1)) # [0, 1, 2, 3]
print(delete([0, 1, 2, 3, 4, 4])) # [0, 1, 2, 3, 4]
print(delete([0, 0, 1, 2], index=0)) # [0, 1, 2]
# дополнительные тесты
print(delete([0, 1, 2, 3], index=6)) # [0, 1, 2, 3]
print(delete([0, 1, 2, 3, 4], index=-1)) # [0, 1, 2, 3]
print(delete([0, 1, 2, 3, 4], index=-6)) #[0, 1, 2, 3, 4]
print(delete([0, 1, 2, 3, 4], index=-3)) #[0, 1, 3, 4]
print(delete([0, 1, 2, 3, 4], index=-2)) #[0, 1, 2, 4]
print(delete([0, 1, 2, 3, 4, 5])) # [0, 1, 2, 3, 4]



