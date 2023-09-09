import os

os.chdir("../..")
root_folder = os.getcwd()

file_names_sizes = {}
for folder_name, sub_folders, filenames in os.walk(root_folder):
    for file in filenames:
        file_path = os.path.join(folder_name, file)
        file_size = os.path.getsize(file_path)
        file_names_sizes[file] = file_size

with open("files_size.txt", "w") as file:
    for key, value in file_names_sizes.items():
        file.write(f"{key}: {value} bites\n")

pair_max_value = max(file_names_sizes.items())
print(pair_max_value)
