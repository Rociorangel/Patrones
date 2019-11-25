class Director():
    def __init__(self, builder):
        self._builder = BebidaBuilder

    def construct_Bebida(self):
        self._builder.create_new_Bebida()
        self._builder.add_Colorante()
        self._builder.add_Azucar()

    def get_Bebida(self):
        return self._builder.Bebida

class BebidaBuilder():
    def __init__(self):
        self.Bebida = None

    
class RefrescoBuilder(BebidaBuilder):

    def add_Colorante(self):
        self.Bebida.Colorante = "Negro"

    def add_Azucar(self):
        self.Bebida.Azucar = "Azucar"

class Bebida(RefrescoBuilder):
    def __init__(self):
        self.Colorante = None
        self.Azucar = None

    def __str__(self):
        return '{} | {} | {} '.format(self.Colorante, self.Azucar)

builder = RefrescoBuilder()
Director = Director(builder)
Director.construct_Bebida
print(Bebida)

