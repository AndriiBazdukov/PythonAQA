str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

list_of_squares = list(map(lambda x: int(x) ** 2, str_list))
list_of_ints = list(map(lambda x: int(x), str_list))
zipped_lists = dict(zip(list_of_ints, list_of_squares))

print(zipped_lists)
