class Station():
    def __init__(self, name, chorX, chordY):
        self.__name = name
        self.__chordX = chorX
        self.__chordY = chordY
        self.__countClients = 0
        self.__countClientWantedDop = 0
        self.__listOfClients = []
        self.__listOfDeniedClients = []

    def getCountClients(self):
        return self.__countClients

    def appClientWantedDop(self):
        self.__countClientWantedDop += 1

    def getClientsWantedop(self):
        return self.__countClientWantedDop

    def appClient(self, newClient):
        self.__countClients += 1
        self.__listOfClients.append(newClient)

    def appDeniedClient(self, deniedClient, reason):
        self.__listOfDeniedClients.append([deniedClient, reason])

    def getClients(self):
        return self.__listOfClients + self.__listOfDeniedClients

    def getStation(self):
        #print(f'Название станции: {self.__name}, координаты: x - {self.__chordX}, y - {self.__chordY}')
        return self.__name

    def getChords(self):
        return([self.__chordX, self.__chordY])
