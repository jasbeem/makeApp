import json
import os
import shutil
import datetime
from PyQt5.QtWidgets import  (QLineEdit)
from models.ObjetoModel import ObjetoModel


class MainController:
    def __init__(self, model, view):
        self.__model = model
        self.__view = view

    def getArchivoPorDefecto(self):
        archivo = self.__model.__str__()+".json"
        return archivo

    def importar(self, archivo):
        """
        Importa la estructura de la app desde un archivo json
        :param email:
        :return:
        """
        with open(archivo, "r") as read_file:
            info = json.load(read_file)
        # cargo los datos en el modelo
        self.__model.empresa = info['empresa']
        self.__model.autor = info['autor']
        self.__model.lenguaje = info['lenguaje']
        self.__model.nombreApp = info['nombreApp']
        self.__model.version = info['version']

        # actualizo la vista con los datos importados
        self.__view.editEmpresa.setText(info['empresa'])
        self.__view.editAutor.setText(info['autor'])
        lenguaje = info['lenguaje']
        index = self.__view.comboLenguaje.findText(lenguaje)
        self.__view.comboLenguaje.setCurrentIndex(index)
        self.__view.editNombreApp.setText(info['nombreApp'])
        self.__view.editVersion.setText(info['version'])

    def exportar(self, archivo):
        """
        Exporta la estructura de la app a un archivo json
        :param email:
        :return:
        """
        info = {}
        
        # cargamos los datos del modelo
        empresa = self.__model.empresa
        autor = self.__model.autor
        lenguaje = self.__model.lenguaje
        mobreApp = self.__model.nombreApp 
        version = self.__model.version
        
        # creamos la estructura de la exportacion json
        info['empresa'] = empresa
        info['autor'] = autor
        info['lenguaje'] = lenguaje
        info['mobreApp'] = mobreApp
        info['version'] = version
        info['empresa'] = empresa
        info['empresa'] = empresa
                
        datos_json = json.dumps(info)
        print(f' Datos que exportamos {datos_json} al archivo {archivo}')
        
        with open(archivo, 'w') as json_file:
            json_file.write(datos_json)
        
    def generar(self, directorio):
        """
        Genera el codigo fuente dentro de una carpeta
        :param email:
        :return:
        """
        print(self.__model.listaObjetos)
    
    def setEmpresa(self, empresa):
        print(f'Empresa: {empresa} se ha actualizado el modelo')
        self.__model.empresa = empresa

    def setAutor(self, autor):
        print(f'Autor: {autor} se ha actualizado el modelo')
        self.__model.autor = autor

    def setNombreApp(self, nombreApp):
        print(f'Nombre App: {nombreApp} se ha actualizado el modelo')
        self.__model.nombreApp = nombreApp

    def setLenguaje(self, lenguaje):
        print(f'Lenguaje: {lenguaje} se ha actualizado el modelo')
        self.__model.lenguaje = lenguaje

    def setVersion(self, version):
        print(f'Versión: {version} se ha actualizado el modelo')
        self.__model.version = version

    def addObjeto(self, nombre):
        """
        Añade un objeto
        :param email:
        :return:
        """
        objeto = ObjetoModel(nombre)
        if not(self.__model.has(objeto)):
            self.__model.addObjeto(objeto)
            self.__view.listaObjetos.addItem(nombre)

    def removeObjeto(self, item):
        """
        Elimina un objeto
        :param email:
        :return:
        """
        objeto = self.__model.getObjeto(item.text())
        self.__model.removeObjeto(objeto)
        self.__view.listaObjetos.takeItem(self.__view.listaObjetos.row(item))

    def editObjeto(self, item, nombre):
        """
        modifica el nombre de un objeto
        :param nombre:
        :return:
        """
        objeto = self.__model.getObjeto(item.text())
        self.__model.editObjeto(objeto, nombre)
        item.setText(nombre)