camel_case_list = ["FirstItem", "FriendsList", "MyTuple"]
snake_case_list = []

for variable in camel_case_list:
    variable_snake_case = [variable[0].lower()]
    for char in variable[1:]:
        if char.isupper():
            variable_snake_case.append("_")
            variable_snake_case.append(char.lower())
        else:
            variable_snake_case.append(char)
    snake_case_list.append("".join(variable_snake_case))

print(snake_case_list)