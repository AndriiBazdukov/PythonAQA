from Car import Car
from AudioSystem import AudioSystem


class Audi(Car, AudioSystem):
    def __init__(self, speed: int, fuel_type: str, left_side_wheel: bool, can_drive_off_road: bool, aux: bool,
                 cd_reader: bool, price: int, model: str):
        Car.__init__(self, speed, fuel_type, left_side_wheel, can_drive_off_road)
        AudioSystem.__init__(self, cd_reader, aux)
        self.price = price
        self.model = model

    def show_model(self):
        print(f"Audi {self.model}")

    def show_price(self):
        print(f"Price: {self.price}")


if __name__ == "__main__":
    audi = Audi(200, "Gas", True, False, True, False, 20000,
                "A6")
    audi.show_model()
    audi.show_price()
    print(audi.is_left_side_wheel())
    print(audi.can_use_for_safari())
    audi.move()
    audi.fuel_up()
    audi.play_music()
    audi.turn_on_radio()
