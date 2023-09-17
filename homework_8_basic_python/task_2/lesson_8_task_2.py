def squares_for_even_numbers(start=0, end=1000000000):
    even = start if start % 2 == 0 else start + 1
    while even <= end:
        yield even ** 2
        even += 2


if __name__ == '__main__':
    for square in squares_for_even_numbers():
        print(square)
