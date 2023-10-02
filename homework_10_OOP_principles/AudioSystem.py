class AudioSystem:
    def __init__(self, cd_reader: bool, aux: bool):
        self.__cd_reader = cd_reader        # Инкапсуляция
        self.__aux = aux                    # Инкапсуляция

    def play_music(self):
        if self.__cd_reader or self.__aux:
            print("la-la-la")
        else:
            print("No music")

    @staticmethod
    def turn_on_radio():
        print("Radio playing")
