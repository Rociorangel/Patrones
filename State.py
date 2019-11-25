'''
Patron state
'''

from abc import ABC, abstractmethod



class EstatusEscolar(ABC):
    @abstractmethod
    def __init__(self):
         self._estudiante = Estudiante()
    def estudiarDuro(self):
       pass
    
class Estudiante(EstatusEscolar):
    def Yoaprobar(self):
        self._estatusescolar = EstatusEscolar()
        pass
    def Yoreprobar (self):
        pass
    def Estudiante(self):
        pass

class aprobado(EstatusEscolar):
     def estudiarDuro(self):
        print("Estudiar diariemanete para mejorar")
        
class reprobado(EstatusEscolar):
    def estudiarDuro(self):
        print("Estudiar diariemanete para mejorar")


    
