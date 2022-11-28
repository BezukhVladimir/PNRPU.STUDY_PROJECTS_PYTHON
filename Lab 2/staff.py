class Person:
    def __init__(self):
        self.__fullname = ""
        self.__age = 0

    def print(self):
        print("Fullname:", self.__fullname)
        print("Age:", self.__age)


class Employee(Person):
    def __init__(self):
        super().__init__()
        self.__position = ""

    def print(self):
        super().print()
        print("Position:", self.__position)
