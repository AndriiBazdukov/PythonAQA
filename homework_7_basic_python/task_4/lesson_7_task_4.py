def printing_map(callback, iterable):
    for item in iterable:
        print(callback(item))


def print_type(x):
    return f"{x} type is {type(x)}"


def print_convertable_to_int(x):
    try:
        y = int(x)
        return y
    except Exception:
        return f"{x} can not be converted to int"


some_list = [1, "2", "asd", 3.4, None]

if __name__ == '__main__':
    printing_map(print_type, some_list)
    printing_map(print_convertable_to_int, some_list)
