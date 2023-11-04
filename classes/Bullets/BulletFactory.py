from classes.Bullets.FireBullet import FireBullet
from classes.Bullets.WaterBullet import WaterBullet
from classes.Bullets.BombBullet import BombBullet


class BulletFactory:

    def CreateBullet(self, bulletType, tankX, tankY, direction, surface):
        if bulletType == "Fire":
            return FireBullet(tankX, tankY, direction, surface)
        elif bulletType == "Water":
            return WaterBullet(tankX, tankY, direction, surface)
        elif bulletType == "Bomb":
            return BombBullet(tankX, tankY, direction, surface)
