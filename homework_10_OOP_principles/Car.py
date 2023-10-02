from Vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, speed: int, fuel_type: str, left_side_wheel: bool, can_drive_off_road: bool):
        super().__init__(speed, fuel_type)
        self.left_side_wheel = left_side_wheel
        self.can_drive_off_road = can_drive_off_road

    # Полиморфизм
    def fuel_up(self):
        print(f"I am fueling up at the fuel station port with {self.fuel_type}")

    # Полиморфизм
    def move(self):
        print(f"I move by road with {self.speed}")

    def is_left_side_wheel(self):
        return self.left_side_wheel

    def can_use_for_safari(self):
        return self.can_drive_off_road


if __name__ == "__main__":
    car = Car(100, "Gas", True, False)
    car.move()
    car.fuel_up()
    print(car.can_use_for_safari())
    print(car.is_left_side_wheel())
