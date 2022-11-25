import re
from models.ObjetoModel import ObjetoModel

class MainModel:
    def __init__(self):
        self.__listaObjetos = []
        self.__empresa = ""
        self.__autor = ""
        self.__nombreApp = ""
        self.__version = ""
        self.__lenguaje = ""
        

    @property
    def listaObjetos(self):
        return self.__listaObjetos

    @listaObjetos.setter
    def listaObjetos(self, value):
        """
        :param value:
        :return:
        """
        self.__listaObjetos = value

    @property
    def empresa(self):
        return self.__empresa

    @empresa.setter
    def empresa(self, value):
        """
        :param value:
        :return:
        """
        self.__empresa = value

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, value):
        """
        :param value:
        :return:
        """
        self.__autor = value

    @property
    def lenguaje(self):
        return self.__lenguaje

    @lenguaje.setter
    def lenguaje(self, value):
        """
        :param value:
        :return:
        """
        self.__lenguaje = value

    @property
    def nombreApp(self):
        return self.__nombreApp

    @nombreApp.setter
    def nombreApp(self, value):
        """
        :param value:
        :return:
        """
        self.__nombreApp = value
        
    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, value):
        """
        :param value:
        :return:
        """
        self.__version = value

    def __str__(self):
        version = self.__version.replace('.','_')
        return self.__nombreApp+"-"+version+"-"+self.__empresa
    
    def has(self, objeto):
        existe = True
        indice = 0
        while ((indice < self.__listaObjetos.__len__()) and 
               (self.__listaObjetos[indice]!=objeto)):
            indice += 1
        return (indice < self.__listaObjetos.__len__())

    def getObjeto(self, nombre):
        indice = 0
        objeto = ObjetoModel(nombre)
        while ((indice<self.__listaObjetos.__len__()) and 
               (self.__listaObjetos[indice]!=objeto)):
            indice += 1
        if (indice<self.__listaObjetos.__len__()):
            objeto = self.__listaObjetos[indice]
        return objeto
    
    def getIndexObjeto(self, objeto):
        """
        :param value: objeto
        :return: devuelve el indice en la lista de objetos si se encuentra o -1 si no existe
        """
        indice = 0
        while ((indice<self.__listaObjetos.__len__()) and 
               (self.__listaObjetos[indice]!=objeto)):
            indice += 1
        if (indice<self.__listaObjetos.__len__()):
            return indice
        else:
            return -1
    
    def addObjeto(self, objeto):
        self.__listaObjetos.append(objeto)
        
    def removeObjeto(self, objeto):
        indice = self.getIndexObjeto(objeto)
        if (indice!=-1):
            del self.__listaObjetos[indice]
    
    def editObjeto(self, objeto, nombre):
        objeto.nombre = nombre

    

    