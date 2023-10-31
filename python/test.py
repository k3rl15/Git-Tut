def convert_to_set(list1):
    set1 = set(list1)
    return set1


def convert_to_list(set1):
    list1 = [item for item in set1]
    return list1


my_list = [1, 2, 3, 4, 5]
new_set = convert_to_set(my_list)
new_list = convert_to_list(new_set)
print(new_set)
print(new_list)
