from abc import ABC, abstractmethod


class Bullet(ABC):  # interface class
    @abstractmethod
    def RotateSprite(self):
        pass

    @abstractmethod
    def is_Collision(self, blockX, blockY):
        pass

    @abstractmethod
    def BorderCollision(self):
        pass

    @abstractmethod
    def Trajectory(self):
        pass

    @abstractmethod
    def DrawBullet(self):
        pass
