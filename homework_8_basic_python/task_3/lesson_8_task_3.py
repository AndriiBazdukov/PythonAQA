import time


def timeit_decorator(func):
    def wrapper():
        start_time = time.time()
        func_result = func()
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.4f}")
        return func_result

    return wrapper


@timeit_decorator
def sum_numbers_squares():
    total = 0
    for i in range(1000000):
        total += i ** 2
    return total


if __name__ == '__main__':
    result = sum_numbers_squares()
    print(f"Result: {result}")
