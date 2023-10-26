from abc import ABC, abstractmethod


class Block(ABC):  # interface class

    @abstractmethod
    def SetPosition(self, mouseX, mouseY):
        pass

    @abstractmethod
    def DrawBlock(self):
        pass
