from abc import ABC

class Vagon(ABC):
    def __init__(self, number):
        self._number = number

class SluzbaV(Vagon, ABC):
    pass

class PochtaV(SluzbaV):
    pass

class RestrountV(SluzbaV):
    pass

class BufetV(SluzbaV):
    pass

class PassengerV(Vagon, ABC):
    def __init__(self, number, countMest, zanitoMest, priceKM, TV, phone):
        super().__init__(number)
        self._countMest = countMest
        self._zanitoMest = zanitoMest
        self._priceKM = priceKM
        self._TV = TV
        self._phone = phone
        self._TVPrice = 100
        self._phonePrice = 60

    def setTVPrice(self, newPrice):
        self._TVPrice = newPrice

    def setPhonePrice(self, newPrice):
        self._phonePrice = newPrice

    def plusPlace(self):
        self._zanitoMest += 1

    def getZanitoMest(self):
        return self._zanitoMest

    def getNumber(self):
        return self._number

    def getCountPlaces(self):
        return self._countMest

class SitV(PassengerV):
    pass

class PlazkartV(PassengerV):
    pass

class CupeV(PassengerV):
    pass