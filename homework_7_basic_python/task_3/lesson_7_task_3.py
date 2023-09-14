def display_box(width: int, height: int, character="*"):
    if width <= 0 or height <= 0:
        print("Width and height must be more than 0")
        return

    print(character * width)

    for _ in range(height - 2):
        print(character + " " * (width - 2) + character)

    if height > 1:
        print(character * width)


if __name__ == '__main__':
    display_box(3, 3, 'x')
    display_box(1, 1, 'x')
    display_box(2, 2, 'x')
