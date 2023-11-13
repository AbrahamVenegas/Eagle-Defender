import json


class JSONAdapter:
    _instance = None
    data = {}

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def saveData(self):
        route = 'json/gameData.json'
        with open(route, 'w') as f:
            json.dump(self.data, f)
        print(str(self.data))

    def clear(self):
        self.data.clear()

    def getBlocksInfo(self, blocks, blockCounters):
        posList = []
        lifeList = []
        count = 0
        for List in blocks:
            for block in List:
                posList.append((block.BlockX, block.BlockY))
                lifeList.append(block.hp)
            if count == 0:
                self.data["wood"] = str(posList)
                self.data["woodLife"] = str(lifeList)
            elif count == 1:
                self.data["iron"] = str(posList)
                self.data["ironLife"] = str(lifeList)
            elif count == 2:
                self.data["concrete"] = str(posList)
                self.data["concreteLife"] = str(lifeList)
            posList.clear()
            lifeList.clear()
            count += 1
        self.data["woodCounter"] = blockCounters[0]
        self.data["ironCounter"] = blockCounters[1]
        self.data["concreteCounter"] = blockCounters[2]

    def getPlayersInfo(self, turn, time):
        self.data["turn"] = turn
        self.data["time"] = time

    def getTankInfo(self, tankX, tankY):
        self.data["Tank"] = [tankX, tankY]

    def getAmmoInfo(self, bomb, fire, water):
        self.data["Bullets"] = [bomb, fire, water]

