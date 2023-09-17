def print_function_name(func):
    def wrapper(a, b):
        result = func(a, b)
        print(f"Function name: {func.__name__}")
        return result

    return wrapper


@print_function_name
def add(a, b):
    return a + b


@print_function_name
def multiply(a, b):
    return a * b


if __name__ == '__main__':
    result1 = add(2, 3)
    print(result1)

    result2 = multiply(4, 5)
    print(result2)
