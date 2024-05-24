class Marshruti():
    def __init__(self, stationGo, stationCome, timeGo, timeCome, dates):
        self.__stationGo = stationGo
        self.__stationCome = stationCome
        self.__timeGo = timeGo
        self.__timeCome = timeCome
        self.__dates = dates

    def getInfo(self):
        return([self.__stationGo, self.__stationCome, self.__timeGo, self.__timeCome])

    def getStationGo(self):
        return self.__stationGo

    def getStationCome(self):
        return self.__stationCome

