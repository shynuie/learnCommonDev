from abc import ABC, abstractmethod


class Staff(ABC):
    @abstractmethod
    def say_hi(self):
        pass
