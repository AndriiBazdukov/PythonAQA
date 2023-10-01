class Worker:
    """
        This class describing worker and his activities
    """

    __salary = 1000

    def __init__(self, name: str, experience: int, position: str):
        """
            Constructor to initialize class worker with basic attributes
        """
        self.__name = name
        self.__experience = experience
        self.__position = position
        if 1 <= experience < 3:
            self.__salary *= 2
        if experience >= 3:
            self.__salary *= 3

    def get_salary(self):
        """
            Classic getter for salary
        """
        return self.__salary

    def set_bigger_salary(self, rise_amount: str):
        """
            Classic setter with additional logic
        """
        if rise_amount.isdigit():
            self.__salary += int(rise_amount)
        else:
            raise TypeError("Please enter a valid amount")

    @property
    def position(self):
        """
            Property (short way to create a getter)
        """
        return self.__position

    @position.setter
    def position(self, new_position):
        """
             Setter (short way to create a setter)
        """
        self.__position = new_position

    @staticmethod
    def do_work():
        """
            Static method that can be called without class instance
        """
        print(f"I am worker a can do work")

    def show_user_info(self):
        """
            Method that shows class attributes and values
        """
        for attr, value in self.__dict__.items():
            print(f"{attr}, {value}")

    @classmethod
    def with_additional_skills(cls, name: str, experience: int, position: str, main_programming_language: str):
        """
        Classmethod to create call instance with additional attribute
        :param name:
        :param experience:
        :param position:
        :param main_programming_language: - additional attribute
        """
        inst = cls(name, experience, position)
        inst.main_programming_language = main_programming_language
        return inst

    def __str__(self):
        return f'(STR) My name is {self.__name} on position {self.__position} with years exp: {self.__experience}'

    def __repr__(self):
        return f'(REPR) My name is {self.__name} on position {self.__position} with years exp: {self.__experience})'


if __name__ == "__main__":
    mike = Worker("Mike", 2, "TAE")
    Worker.do_work()
    mike.show_user_info()
    mike.set_bigger_salary("500")
    print(mike.get_salary())
    mike.position = "Lead TAE"
    print(mike.position)
    print(str(mike))
    print(repr(mike))

    mike_extended = Worker.with_additional_skills("Mike", 2, "TAE", "python")
    mike_extended.show_user_info()
    print(str(mike_extended))
    print(repr(mike_extended))
