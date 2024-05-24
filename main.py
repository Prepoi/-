from abc import ABC
from station import *
from vagons import *
from poezd import *
from client import *
from station import *
from marshruti import *
from random import *
from tkinter import *

listOfStations = [Station('Барнаул', 80, 85), Station('Новосибирск', 280, 105),
               Station('Севастополь', 230, 450), Station('Керчь', 550, 280)
               ]

def onlyStationsName(listOfStations):
    nameList = []
    for el in listOfStations:
        nameList.append(el.getStation())
    return nameList
listOfStationsNames = onlyStationsName(listOfStations)
print(listOfStationsNames)

def unpackListOfStations(listOfStations):
    unpackedList = []
    for el in listOfStations:
        unpackedList.append([el.getStation(), el.getChords()[0], el.getChords()[1]])
    return unpackedList
unpackedList = unpackListOfStations(listOfStations)
print(unpackedList)

listOfMarshruti = [Marshruti('Новосибирск', 'Барнаул', '10:20', '13:10', 'Четные'),
                   Marshruti('Барнаул', 'Новосибирск', '4:40', '6:25', 'Нечетные'),
                   Marshruti('Севастополь', 'Керчь', '19:00', '22:15', 'Нечетные'),
                   Marshruti('Керчь', 'Севастополь', '00:00', '3:19', 'Четные'),
                   Marshruti('Барнаул', 'Керчь', '00:00', '13:00', 'Нечетные'),
                   Marshruti('Барнаул', 'Севастополь', '00:00', '15:00', 'Нечетные'),
                   ]


listPoezdov = [
    Poezd('P001', 'Барнаул', 'Новосибирск', '4:40', '6:25'),
    Poezd('P002', 'Новосибирск', 'Барнаул', '10:20', '13:10'),
    Poezd('P003', 'Севастополь', 'Керчь', '19:00', '22:15'),
    Poezd('P004', 'Керчь', 'Севастополь', '00:00', '3:19'),
    Poezd('P005', 'Барнаул', 'Керчь', '00:00', '13:00'),
    Poezd('P006', 'Барнаул', 'Севастополь', '00:00', '15:00')
]

def getNumbersPoezdov(list):
    newList = []
    for el in list:
        newList.append(el.getNumber())
    return newList

listOfNumbersPoezdov = getNumbersPoezdov(listPoezdov)

def selectRanomVagon(list):
    a = randint(0, len(list) - 1)
    vagon = list[a]
    list.pop(a)
    return vagon

listSitsVagons = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012']
listPlazkartVagons = ['PL001', 'PL003', 'PL004', 'PL005', 'PL006', 'PL007']
listBufetVagons = ['B001', 'B002', 'B003', 'B004', 'B005', 'B006']
listCupeVagons = ['C001', 'C002', 'C003', 'C004', 'C005', 'C006']

def standartPoezdVagons():
    global listPoezdov
    for el in range(len(listPoezdov)):
        massVagons = [
            SitV(selectRanomVagon(listSitsVagons), 150, 0, 3, False, False),
            PlazkartV(selectRanomVagon(listPlazkartVagons), 50, 0, 5, False, True),
            CupeV(selectRanomVagon(listCupeVagons), 50, 0, 7, True, True),
            BufetV(selectRanomVagon(listBufetVagons))
        ]
        listPoezdov[el].appMassVagons(massVagons)

standartPoezdVagons()

window = Tk()
window.title('Станции и поезда')
window.geometry('1600x900-100-100')

canvas = Canvas(bg='white',
                width=1200,
                height=600,
                )
#be n, ne, e, se, s, sw, w, nw, or center
canvas.pack(anchor='sw', pady=20, padx=30)
radiusOfStation = 40

for el in listOfStations:
    canvas.create_oval(el.getChords()[0]-radiusOfStation, el.getChords()[1]-radiusOfStation,
                       el.getChords()[0] + radiusOfStation, el.getChords()[1] + radiusOfStation,
                       )
    canvas.create_text(el.getChords()[0],
                       el.getChords()[1] - radiusOfStation - 10,
                       text=el.getStation(),
                       font=12)

for el in listOfMarshruti:
    chordXGo = None
    chordYGo = None
    chordXCome = None
    chordYCome = None
    for element in unpackedList:
        if element[0] == el.getStationGo():
            chordXGo = element[1]
            chordYGo = element[2]
        elif element[0] == el.getStationCome():
            chordXCome = element[1]
            chordYCome = element[2]
    canvas.create_line(
        chordXGo, chordYGo, chordXCome, chordYCome
)


entryClientName = Entry()
labelClientName = Label(text='Имя клиента')
#entryClientName.place(x=20, y=700)

entryClientPassport = Entry()
#entryClientPassport.place(x=160, y=700)
labelClientPassport = Label(text='Пасспорт клиента')

entryClientStationGo = Entry()
#entryClientStationGo.place(x=300, y=700)
labelClientStationGo = Label(text='Станция отправления')

entryClientStationCome = Entry()
#entryClientStationCome.place(x=440, y=700)
labelClientStationCome = Label(text='Станция прибытия')

entryClientPoezdNumber = Entry()
#entryClientPoezdNumber.place(x=580, y=700)
labelClientPoezdNumber = Label(text='Номер поезда')

entryClientDate = Entry()
#entryClientDate.place(x=720, y=700)
labelClientDate = Label(text='Дата отправления')

labelPolyaError = Label(text='Не все поля заполнены!')
labelClassVagonError = Label(text='Неверно введен тип вагона!')
labelPhoneError = Label(text='Неверно введено наличие телефона!')
labelTVError = Label(text='Неверно введено наличие телевизора!')
listOfTypeVagons = ['Купе', 'Сидячий', 'Плацкарт']
labelStationError = Label(text='Такой станции отправления/назначения не существует!')
labelNumberPoezdError = Label(text='Введен неверный номер поезда!')

def clearMainEntry():
    entryClientName.delete(0, END)
    entryClientPassport.delete(0, END)
    entryClientStationGo.delete(0, END)
    entryClientStationCome.delete(0, END)
    entryClientPoezdNumber.delete(0, END)
    entryClientDate.delete(0, END)

def clearDopEntry():
    entryClassVagon.delete(0, END)
    entryPhone.delete(0, END)
    entryTV.delete(0, END)

countClientsWantedDopAll = 0
def appClient():
    if '' in [entryClientName.get(), entryClientPassport.get(), entryClientStationGo.get(), entryClientStationCome.get(),\
           entryClientPoezdNumber.get(), entryClientDate.get()]:
        print('Не все поля заполнены!')
        labelPolyaError.place(x=1000, y=740)
    elif entryClientStationGo.get() not in listOfStationsNames or entryClientStationCome.get() not in listOfStationsNames:
        labelStationError.place(x=940, y=740)
        labelPolyaError.place_forget()
    elif entryClientPoezdNumber.get() not in listOfNumbersPoezdov:
        labelNumberPoezdError.place(x=940, y=740)
        labelPolyaError.place_forget()
        labelStationError.place_forget()
    else:
        labelPolyaError.place_forget()
        labelStationError.place_forget()
        labelNumberPoezdError.place_forget()
        newClient = Client(entryClientName.get(), entryClientPassport.get(), entryClientStationGo.get(), entryClientStationCome.get(),\
           entryClientPoezdNumber.get(), entryClientDate.get())

        if entryClassVagon.get() not in listOfTypeVagons:
            labelClassVagonError.place(x=20, y=840)
        else:
            labelClassVagonError.place_forget()
        if entryPhone.get() not in ['1', '0', 'T', 'F', 't', 'f', 'Да', 'Нет', 'да', 'нет', '']:
            labelPhoneError.place(x=180, y=840)
        else:
            labelPhoneError.place_forget()
        if entryTV.get() not in ['1', '0', 'T', 'F', 't', 'f', 'Да', 'Нет', 'да', 'нет', '']:
            labelTVError.place(x=390, y=840)
        else:
            labelTVError.place_forget()

        if entryClassVagon.get() in listOfTypeVagons or entryClassVagon.get() == '':
            if entryPhone.get() in ['1', '0', 'T', 'F', 't', 'f', 'Да', 'Нет', 'да', 'нет', '']:
                if entryTV.get() in ['1', '0', 'T', 'F', 't', 'f', 'Да', 'Нет', 'да', 'нет', '']:
                    print(newClient.getInfo())

                    for el in listOfStations:
                        if el.getStation() == entryClientStationGo.get():
                            listOfStations[listOfStations.index(el)].appClient(newClient)

                            if entryPhone.get() != '' or entryTV.get() != '':
                                listOfStations[listOfStations.index(el)].appClientWantedDop()
                                global countClientsWantedDopAll
                                countClientsWantedDopAll += 1

                            break
                    for el in listPoezdov:
                        if el.getNumber() == entryClientPoezdNumber.get():
                            for element in el.getVagons():
                                if 'SitV' in str(type(element)) and entryClientPoezdNumber.get() == 'Сидячий' and element.canPlusPlace:
                                    listPoezdov[listPoezdov.index(el)].getVagons()[el.getVagons().index(element)].plusPlace()


                    newClient.requestClassVagon(entryClassVagon.get())
                    entryClassVagon.delete(0, END)
                    labelClassVagonError.place_forget()

                    newClient.requestPhone(entryPhone.get())
                    entryPhone.delete(0, END)
                    labelPhoneError.place_forget()

                    newClient.requestTV(entryTV.get())
                    entryTV.delete(0, END)
                    labelTVError.place_forget()

                    clearMainEntry()
                    clearDopEntry()

def readFile():
    global listOfTypeVagons, listOfStations
    file = open('clients.txt', encoding='utf-8')
    massClients = file.readlines()
    for el in range(len(massClients)):
        massClients[el] = massClients[el].replace('\n', '')
    #print(massClients)
    for el in massClients:
        el = el.split(',')
        mainInfo = el[:6]
        dopInfo = el[6:]
        #print(mainInfo, dopInfo)
        newClient = Client(mainInfo[0], mainInfo[1], mainInfo[2], mainInfo[3], mainInfo[4], mainInfo[5])
        for element in dopInfo:
            if element in listOfTypeVagons:
                newClient.requestClassVagon(element)
            elif element in ['Буфет', 'Ресторан']:
                newClient.requestEatingVagon(element)
            elif element == 'Телефон':
                newClient.requestPhone()
            elif element == 'Телевизор':
                newClient.requestTV()
        #print(newClient.getFullInfo())
        for i in range(len(listOfStations)):
            if listOfStations[i].getStation() == mainInfo[2]:
                if newClient.getPhone() or newClient.getTV():
                    listOfStations[i].appClientWantedDop()
                listOfStations[i].appClient(newClient)
                break
        defaultTypeVagon = SitV
        if newClient.getClassVagon() is not None:
            if newClient.getClassVagon() == 'Купе':
                defaultTypeVagon = CupeV
            elif newClient.getClassVagon() == 'Плацкарт':
                defaultTypeVagon = PlazkartV
        for i in range(len(listPoezdov)):
            if listPoezdov[i].getNumber() == newClient.getPoezdNumber():
                for vagon in range(len(listPoezdov[i].getVagons())):
                    if isinstance(listPoezdov[i].getVagons()[vagon], defaultTypeVagon):
                        listPoezdov[i].getVagons()[vagon].plusPlace()


readFile()

labelClassVagon = Label(text='Класс вагона')
entryClassVagon = Entry()

labelPhone = Label(text='Наличие телефона')
entryPhone = Entry()

labelTV = Label(text='Наличие телевизора')
entryTV = Entry()

def sostPoezdov():
    windowSostPoezdov = Tk()
    windowSostPoezdov.geometry('400x650')
    for poezd in listPoezdov:
        Label(windowSostPoezdov, text=f'{poezd.getNumber()}').pack()
        for vagon in poezd.info():
            Label(windowSostPoezdov, text=f'{vagon}').pack()

def infoDop():
    windowInfoDop = Tk()
    windowInfoDop.geometry('600x200')
    for el in listOfStations:
        Label(windowInfoDop, text=f'На станции {el.getStation()} хотят доп оборудование {el.getClientsWantedop()}').pack()
    Label(windowInfoDop, text=f'Хотят всего {countClientsWantedDopAll}').pack()

def openDop():
    entryClassVagon.place(x=20, y=780)
    labelClassVagon.place(x=20, y=810)

    entryPhone.place(x=160, y=780)
    labelPhone.place(x=160, y=810)

    entryTV.place(x=300, y=780)
    labelTV.place(x=300, y=810)

    btnOpenDop.place_forget()
    btnCloseDop.place(x=1000, y=780)

def closeDop():
    entryClassVagon.place_forget()
    entryClassVagon.delete(0, END)
    labelClassVagon.place_forget()

    entryPhone.place_forget()
    entryPhone.delete(0, END)
    labelPhone.place_forget()

    entryTV.place_forget()
    entryTV.delete(0, END)
    labelTV.place_forget()

    btnOpenDop.place(x=1000, y=780)
    btnCloseDop.place_forget()

def showWorkWithClients():

    entryClientName.place(x=20, y=700)
    labelClientName.place(x=20, y=730)

    entryClientPassport.place(x=160, y=700)
    labelClientPassport.place(x=160, y=730)

    entryClientStationGo.place(x=300, y=700)
    labelClientStationGo.place(x=300, y=730)

    entryClientStationCome.place(x=440, y=700)
    labelClientStationCome.place(x=440, y=730)

    entryClientPoezdNumber.place(x=580, y=700)
    labelClientPoezdNumber.place(x=580, y=730)

    entryClientDate.place(x=720, y=700)
    labelClientDate.place(x=720, y=730)

    btnAppNewClient.place(x=1000, y=700)
    btnOpenDop.place(x=1000, y=780)
    btnStopWorkWithClients.place(x=1270, y=700)
    btnStartWorkWithClients.place_forget()

def unShowWorkWithClients():

    entryClientName.place_forget()
    labelClientName.place_forget()

    entryClientPassport.place_forget()
    labelClientPassport.place_forget()

    entryClientStationGo.place_forget()
    labelClientStationGo.place_forget()

    entryClientStationCome.place_forget()
    labelClientStationCome.place_forget()

    entryClientPoezdNumber.place_forget()
    labelClientPoezdNumber.place_forget()

    entryClientDate.place_forget()
    labelClientDate.place_forget()

    btnAppNewClient.place_forget()
    labelPolyaError.place_forget()

    entryClassVagon.place_forget()
    labelClassVagon.place_forget()

    entryPhone.place_forget()
    labelPhone.place_forget()

    entryTV.place_forget()
    labelTV.place_forget()

    btnCloseDop.place_forget()
    btnStopWorkWithClients.place_forget()
    btnOpenDop.place_forget()
    btnStartWorkWithClients.place(x=1270, y=30)

def getClientList():
    windowGetClientList = Tk()
    windowGetClientList.geometry('800x400')
    for el in listOfStations:
        Label(windowGetClientList, text=f'На станции {el.getStation()}:').pack()
        for client in el.getClients():
            Label(windowGetClientList, text=f'{client.getInfo()}').pack()

def zagruzVagons():
    windowZagruzVagons = Tk()
    windowZagruzVagons.geometry('400x500')
    massSitV = []
    massPlazkartV = []
    massCupeV = []
    for poezd in listPoezdov:
        for vagon in poezd.getVagons():
            if isinstance(vagon, SitV):
                massSitV.append(vagon)
            elif isinstance(vagon, PlazkartV):
                massPlazkartV.append(vagon)
            elif isinstance(vagon, CupeV):
                massCupeV.append(vagon)
    Label(windowZagruzVagons, text='Загруженность сидячих вагонов').pack()
    for vagon in massSitV:
        Label(windowZagruzVagons,
              text=f'Номер - {vagon.getNumber()}, занято {vagon.getZanitoMest()} из {vagon.getCountPlaces()}'
              ).pack()

    Label(windowZagruzVagons, text='Загруженность плацкартных вагонов').pack()
    for vagon in massPlazkartV:
        Label(windowZagruzVagons,
              text=f'Номер - {vagon.getNumber()}, занято {vagon.getZanitoMest()} из {vagon.getCountPlaces()}'
              ).pack()

    Label(windowZagruzVagons, text='Загруженность купейных вагонов').pack()
    for vagon in massCupeV:
        Label(windowZagruzVagons,
              text=f'Номер - {vagon.getNumber()}, занято {vagon.getZanitoMest()} из {vagon.getCountPlaces()}'
              ).pack()

def zagruzMarshrutov():
    windowZagruzMarshrutov = Tk()
    windowZagruzMarshrutov.geometry('400x400')

    for poezd in listPoezdov:
        zanitoPlace = 0
        countPlace = 0
        for vagon in poezd.getPassengerVagons():
            zanitoPlace += vagon.getZanitoMest()
            countPlace += vagon.getCountPlaces()
        Label(windowZagruzMarshrutov,
              text=f'На маршруте {poezd.getStationGo()} - {poezd.getStationCome()} загруженность {zanitoPlace} из {countPlace}'
              ).pack()

btnStartWorkWithClients = Button(
    text='Начать работу с клиентами',
    command=showWorkWithClients,
    padx=50,
    pady=20
)

btnAppNewClient = Button(
    text='Добавить Клиента',
    command=appClient
)

btnStopWorkWithClients = Button(
    text='Закончить работу с клиентами',
    command=unShowWorkWithClients,
    padx=50,
    pady=20
)

btnOpenDop = Button(
    text='Открыть доп услуги',
    command=openDop
)

btnCloseDop = Button(
    text='Закрыть доп услуги',
    command=closeDop
)

btnGetClientList = Button(
    text='Узнать список клиентов',
    command=getClientList,
    padx=60,
    pady=20
)

btnSostPoezdov = Button(
    text='Узнать состояние поездов',
    command=sostPoezdov,
    padx=54,
    pady=20
)

btnClientsReqDop = Button(
    text='Инфо по доп обородуванию',
    command=infoDop,
    padx=46,
    pady=20
)

btnReadFile = Button(
    text='Прочитать клиентов из файла',
    command=readFile,
    padx=42,
    pady=20
)

btnZagruzVagons = Button(
    text='Загруженность вагонов',
    command=zagruzVagons,
    padx=59,
    pady=20
)

btnZagruzMarshruti = Button(
    text='Загруженность маршрутов',
    command=zagruzMarshrutov,
    padx=49,
    pady=20
)

btnStartWorkWithClients.place(x=1270, y=30)
btnReadFile.place(x=1270, y=100)
btnSostPoezdov.place(x=1270, y=170)
btnClientsReqDop.place(x=1270, y=240)
btnGetClientList.place(x=1270, y=310)
btnZagruzVagons.place(x=1270, y=380)
btnZagruzMarshruti.place(x=1270, y=450)

window.mainloop()