from Plane import Plane


class Boeing(Plane):
    def __init__(self, speed: int, fuel_type: str, max_flight_height: int, number_of_pilots: int, ticket_price: float,
                 number_of_passengers: int):
        super().__init__(speed, fuel_type, max_flight_height, number_of_pilots)
        self.number_of_passengers = number_of_passengers
        self.ticket_price = ticket_price

    def show_passengers_number(self):
        print(self.number_of_passengers)

    def show_ticket_price(self):
        print(self.ticket_price)


if __name__ == "__main__":
    boeing = Boeing(1000, "Jet fuel", 10000, 2, 600.50, 200)
    boeing.move()
    boeing.fuel_up()
    boeing.max_height_info()
    boeing.show_number_of_pilots()
    boeing.show_how_parrent_move()
    boeing.show_ticket_price()
    boeing.show_passengers_number()
