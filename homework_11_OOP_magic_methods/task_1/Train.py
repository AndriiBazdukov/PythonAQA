from Wagon import Wagon
from homework_11_OOP_magic_methods.task_2.CustomIterator import CustomIterator


class Train:
    def __init__(self):
        self.wagons = []

    def add_wagon(self, wagon):
        self.wagons.append(wagon)

    def __len__(self):
        return len(self.wagons)

    def __str__(self):
        my_iter = CustomIterator(self.wagons, 0, 4)
        wagon_numbers = "-".join(str(wagon) for wagon in my_iter)
        return f"<=[HEAD]-{wagon_numbers}"


if __name__ == "__main__":
    train = Train()

    wagon1 = Wagon(1)
    wagon2 = Wagon(2)
    wagon3 = Wagon(3)
    wagon4 = Wagon(4)
    wagon5 = Wagon(5)

    train.add_wagon(wagon1)
    train.add_wagon(wagon2)
    train.add_wagon(wagon3)
    train.add_wagon(wagon4)
    train.add_wagon(wagon5)

    wagon1.add_passenger("Passenger 1")
    wagon1.add_passenger("Passenger 2")
    wagon2.add_passenger("Passenger 3")
    wagon3.add_passenger("Passenger 4")
    wagon4.add_passenger("Passenger 5")
    wagon4.add_passenger("Passenger 6")
    wagon5.add_passenger("Passenger 7")

    print(train)
    print(wagon4)
    print(len(train))
    print(len(wagon4))
