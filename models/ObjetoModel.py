import re


class ObjetoModel:
    def __init__(self):
        self.__nombre = ""
        self.__listaMiembros = []
        self.__relaciones = []
    
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__listaMiembros = []
        self.__relaciones = []
        
    @property
    def nombre(self):
        return self.__nombre

    @property
    def listaMiembros(self):
        return self.__listaMiembros

    @property
    def listaRelaciones(self):
        return self.__listaRelaciones

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @listaMiembros.setter
    def listaMiembros(self, value):
        self.__listaMiembros = value

    @listaRelaciones.setter
    def listaRelaciones(self, value):
        self.__listaRelaciones = value
        
    def __eq__(self, objeto):
        return self.nombre == objeto.nombre
        

    def addMiembro(self, miembro):
        self.__listaMiembros.append(miembro)        

    def removeMiembro(self, miembro):
        del self.__listaMiembros[0]


    