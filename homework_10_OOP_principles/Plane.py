from Vehicle import Vehicle


class Plane(Vehicle):
    def __init__(self, speed: int, fuel_type: str, max_flight_height: int, number_of_pilots: int):
        super().__init__(speed, fuel_type)
        self.number_of_pilots = number_of_pilots
        self.max_flight_height = max_flight_height

    # Полиморфизм
    def fuel_up(self):
        print(f"I am fueling up at the air port with {self.fuel_type}")

    # Полиморфизм
    def move(self):
        print(f"I move by air with {self.speed}")

    def max_height_info(self):
        print(f"I can fly on {self.max_flight_height} height")

    def show_number_of_pilots(self):
        print(f"I need {self.number_of_pilots} pilots to fly")
        
    def show_how_parrent_move(self):
        super().move()


if __name__ == "__main__":
    plane = Plane(1000, "Jet fuel", 10000, 2)
    plane.move()
    plane.fuel_up()
    plane.max_height_info()
    plane.show_number_of_pilots()
    plane.show_how_parrent_move()
