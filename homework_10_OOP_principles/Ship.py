from Vehicle import Vehicle


class Ship(Vehicle):

    def __init__(self, speed: int, fuel_type: str, main_port: str, year_build: int):
        super().__init__(speed, fuel_type)
        self.main_port = main_port
        self.year_build = year_build

    def fuel_up(self):
        print(f"I fuel up in the port with {self.fuel_type}")

    def show_main_port_info(self):
        print(f"main port {self.main_port}")

    def show_year_buid(self):
        print(f"I was build in {self.year_build}")


if __name__ == "__main__":
    ship = Ship(50, "Disel", "Odessa", 2000)
    ship.move()
    ship.fuel_up()
    ship.show_main_port_info()
    ship.show_year_buid()