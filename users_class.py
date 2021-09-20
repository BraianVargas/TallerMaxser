class Users: 
    __name = None
    __dni = None
    __phone = None
    __machine = None
    __status = None
    
    def __init__(self,name,dni,phone):
        self.__name = name
        self.__dni = dni
        self.__phone = phone
        self.__status = "En espera"
        self.__machine = []

    def getName(self):
        return self.__name

    def getDNI(self):
        return self.__dni
    
    def getPhone(self):
        return self.__phone
    
    def getAddress(self):
        return self.__address

    def getStatus(self):
        return self.__status 
    
    def getMachine(self, idMachine): #ver como buscar el equipo segun su id...
        pass
    
    def addMachine(self, machine):
        self.__machine.append(machine)
    