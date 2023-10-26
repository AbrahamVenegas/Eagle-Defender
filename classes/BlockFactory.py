from classes.WoodBlock import WoodBlock
from classes.ConcreteBlock import ConcreteBlock
from classes.IronBlock import IronBlock


class BlockFactory:

    def CreateBlock(self, BlockType, blockX, blockY, surface):
        if BlockType == "Wood":
            return WoodBlock(blockX, blockY, surface)
        if BlockType == "Concrete":
            return ConcreteBlock(blockX, blockY, surface)
        if BlockType == "Iron":
            return IronBlock(blockX, blockY, surface)
