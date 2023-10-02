from Restaurant import Restaurant
from Ship import Ship


class CruiseShip(Ship, Restaurant):
    def __init__(self, speed: int, fuel_type: str, main_port: str, year_build: int, restaurant_cuisine: str,
                 number_of_tables: int, crew_number: int, capitan_name: str):
        Ship.__init__(self, speed, fuel_type, main_port, year_build)
        Restaurant.__init__(self, restaurant_cuisine, number_of_tables)
        self.crew_number = crew_number
        self.capitan_name = capitan_name

    def show_capitan_name(self):
        print(f"Capitan is {self.capitan_name}")

    def show_crew_number(self):
        print(f"Crew number: {self.crew_number}")


if __name__ == "__main__":
    cruise_ship = CruiseShip(50, "Diesel", "Odessa", 2000, "France",
                             50, 100, "Silver")
    cruise_ship.move()
    cruise_ship.fuel_up()
    cruise_ship.show_capitan_name()
    cruise_ship.show_year_buid()
    cruise_ship.show_main_port_info()
    cruise_ship.show_crew_number()
    cruise_ship.show_number_of_tables()
    cruise_ship.show_restaurant_cuisine()