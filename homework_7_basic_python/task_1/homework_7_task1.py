# Знаю что можно было в 3 строки и выходит за рамки задания но чуть поэксперементировал
def sum_range(start_range=None, end_range=None):
    counter = 0

    def count_range(start_range, end_range):
        if start_range > end_range:
            start_range, end_range = end_range, start_range

        total = sum(range(start_range, end_range + 1))
        return total

    if start_range is None or end_range is None:
        while counter < 4:
            try:
                start_range = int(input("Enter first int: "))
                end_range = int(input("Enter second int: "))
            except ValueError:
                print("Incorrect int value")
                counter += 1
                continue
            else:
                return count_range(start_range, end_range)
    else:
        return count_range(start_range, end_range)


if __name__ == '__main__':
    print(sum_range(1, 5))
    print(sum_range(4, 6))
    print(sum_range())
