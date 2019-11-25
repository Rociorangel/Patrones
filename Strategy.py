from abc import ABC, abstractmethod

class sistemaOperativo(ABC):
    @abstractmethod
    def actualizacionPeriodica():
        pass
    def SeguridadRobusta():
        pass
    def gamaAlta():
        pass
    
    
class Linux(sistemaOperativo):
    def ActualizacionPeriodica(self):
       print("sistema operativo es muy robusto en cuestion de seguridad")
class Windows(sistemaOperativo):
    def SeguridadPeriodica(self):
        print("es una sistema operativo que se actualiza constantemente")
class Mac (sistemaOperativo):
    def gamaAlta(self):
        print("es un sistema operativo de gama alta")


class SoftwarePrincipal:
    def __init__(self):
       self.tiposistemaoperativo = sistemaOperativo()
