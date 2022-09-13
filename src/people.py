from abc import ABC, abstractmethod


class Staff(ABC):
    @abstractmethod
    def say_hi(self):
        pass


class Marvin(Staff):
    def say_hi(self):
        print("Hello, I'm Marvin.")

class Chane(Staff):
    def say_hi(self):
        print('hello, my name is chane > <')

        