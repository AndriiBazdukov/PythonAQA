import math


def square(side):
    square_perimeter = 4 * side
    square_area = side ** 2
    square_diagonal = side * math.sqrt(2)
    return square_perimeter, square_area, square_diagonal


if __name__ == '__main__':
    for side_length in range(10, 15):
        perimeter, area, diagonal = square(side_length)

        print("Периметр:", perimeter)
        print("Площадь:", area)
        print("Диоганаль:", diagonal, "\n")
