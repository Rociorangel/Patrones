from abc import ABC, abstractmethod

class Celulares (ABC):
    @abstractmethod
    def dispositivos(self):
        pass

class Samsung(Celulares):
    def dipositivo(self):
        print("Dipositivo de gama alta")

class Apple(Celulares):
    def dispositivo(self):
        print("Dispositivo de gama media")

class SamsungJ7(Samsung):
    def modelo(self):
        print("Modelo perteneciente a Samsung")
class SamsungA10(Samsung):
    def modelo(self):
        print("Modelo perteneciente a Samsung")

class Iphone7(Apple):
    def modelo(self):
        print("Modelo perteneciente a Apple")

class Iphone10(Apple):
    def modelo(self):
        print("Modelo perteneciente a Apple")
