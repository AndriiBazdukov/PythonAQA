class Wagon:
    def __init__(self, number, max_passengers=10):
        self.number = number
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, passenger):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(passenger)
        else:
            print("Carriage is full.")

    def __len__(self):
        return len(self.passengers)

    def __str__(self):
        return f"[{self.number}]"
