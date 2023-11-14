from REST_API import REST_API


class Loader:
    _instance = None
    data = []
    email = ""
    date = []
    slot = 0

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def getJSON(self, email):
        info = REST_API.get_player_saves(email, 0)
        for i, (emailStr, jsonStr, date) in enumerate(info[:3]):
            self.email = emailStr
            self.data.append(eval(jsonStr))
            self.date.append(date)

    def loadGame(self):
        if self.slot == 1 and self.data:
            return self.data[0]
        elif self.slot == 2 and len(self.data) > 1:
            return self.data[1]
        elif self.slot == 3 and len(self.data) > 2:
            return self.data[2]
