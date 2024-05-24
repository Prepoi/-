class Client():
    #Переделать по заданию
    def __init__(self, name, passport, stationGo, stationCome, poezNumber, date):
        self.__name = name
        self.__passport = passport
        self.__stationGo = stationGo
        self.__stationCome = stationCome
        self.__poezdNumber = poezNumber
        self.__date = date
        self.__classVagon = None
        self.__reqPhone = False
        self.__reqTV = False
        self.__reqEatingVagon = None


    def getName(self):
        return self.__name

    def getInfo(self):
        return f'Имя - {self.__name}, пасспорт - {self.__passport}, станция отправления - {self.__stationGo}, '\
               f'станция назначения - {self.__stationCome}, номер поезда - {self.__poezdNumber}'

    def getPoezdNumber(self):
        return self.__poezdNumber

    def getClassVagon(self):
        return self.__classVagon

    def requestClassVagon(self, classVagon):
        self.__classVagon = classVagon

    def requestEatingVagon(self, eatingVagon):
        self.__reqEatingVagon = eatingVagon

    def requestPhone(self):
        self.__reqPhone = True

    def requestTV(self):
        self.__reqTV = True

    def getPhone(self):
        return self.__reqPhone

    def getTV(self):
        return self.__reqTV