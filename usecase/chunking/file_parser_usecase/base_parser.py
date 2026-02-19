from abc import ABC, abstractmethod

class ParserStratergy(ABC):
    @abstractmethod
    def parse(self, file:bytes)->str:
        pass