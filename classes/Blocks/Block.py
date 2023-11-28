from abc import ABC, abstractmethod


class Block(ABC):  # interface class

    @abstractmethod
    def SetPosition(self):
        pass

    @abstractmethod
    def DrawBlock(self):
        pass

    @abstractmethod
    def isCollision(self, Object):
        pass

    @abstractmethod
    def updateHP(self, damage):
        pass

    def ResetHP(self):
        pass

    @abstractmethod
    def playSound(self):
        pass
