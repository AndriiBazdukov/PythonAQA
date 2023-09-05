input_string = input("Enter a string: ")
dictionary = {}
for char in input_string:
    if char == " ":
        continue
    dictionary[char] = dictionary.get(char, 0) + 1

pairs_as_string_list = [f"{char}, {count}" for char, count in dictionary.items()]
result = " ".join(pairs_as_string_list)

print(result)
