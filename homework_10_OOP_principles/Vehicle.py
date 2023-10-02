from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, speed: int, fuel_type: str):
        self.speed = speed
        self.fuel_type = fuel_type

    def move(self):
        print(f"I can move with {self.speed}")

    @abstractmethod
    def fuel_up(self):
        pass
