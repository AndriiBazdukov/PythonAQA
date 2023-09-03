names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
for name in names:
    if not isinstance(name, str) or not name.isalpha():
        continue
    print(name)