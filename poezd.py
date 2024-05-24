from vagons import *
class Poezd():
    def __init__(self, number, stationGo, stationCome, timeGo, timeCome):
        self.__number = number
        self.__stationGo = stationGo
        self.__stationCome = stationCome
        self.__timeGo = timeGo
        self.__timeCome = timeCome
        self.__listOfVagon = []

    def info(self):
        summ = 0
        massVagons = []
        for el in self.__listOfVagon:
            if isinstance(el, SitV):
                typeVagona = 'Сидячий'
            elif isinstance(el, PlazkartV):
                typeVagona = 'Плацкарт'
            elif isinstance(el, CupeV):
                typeVagona = 'Купе'
            elif isinstance(el, BufetV):
                typeVagona = 'Буфет'
            elif isinstance(el, RestrountV):
                typeVagona = 'Ресторан'
            elif isinstance(el, PochtaV):
                typeVagona = 'Почтовый'

            if isinstance(el, SluzbaV):
                massVagons.append(f'Тип вагона: {typeVagona}')
            else:
                massVagons.append(f'Тип вагона: {typeVagona}, занято мест в вагоне: {el.getZanitoMest()}')
                summ += el.getZanitoMest()
        return massVagons

    def appOneVagon(self, newVagon):
        self.__listOfVagon.append(newVagon)

    def appMassVagons(self, massVagons):
        for el in massVagons:
            self.__listOfVagon.append(el)

    def getNumber(self):
        return self.__number

    def getVagons(self):
        return self.__listOfVagon

    def getPassengerVagons(self):
        massPassengerVagons = []
        for vagon in self.__listOfVagon:
            if isinstance(vagon, PassengerV):
                massPassengerVagons.append(vagon)
        return massPassengerVagons

    def getStationGo(self):
        return self.__stationGo

    def getStationCome(self):
        return self.__stationCome