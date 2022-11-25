from PyQt5.QtWidgets import (QApplication, QGridLayout, QToolButton, QHBoxLayout, QComboBox, QListWidget, QGroupBox, QTreeView, QInputDialog, QMessageBox,
                             QDialog, QFileDialog, QPushButton, QVBoxLayout, QWidget, QTabWidget, QFormLayout, QRadioButton, QLineEdit, QLabel, QCheckBox, QAbstractItemView)
from PyQt5 import (QtGui, QtCore)

from PyQt5.QtGui import (QStandardItemModel, QIcon)



class MainView(QWidget):
    
    def __init__(self, parent):
        super().__init__(parent)
        # set the controller
        self.__controller = None
        # cargamos el interfaz grafico
        self.initUI()
       
    def setController(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.__controller = controller
        
    def initUI(self): 
        """
        Crea el interfaz gráfico
        :param:
        :return:
        """   
        # Create a Layout instance
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        
         # Add widgets to the layout horizontal
        importarButton = QToolButton()
        self.importarButtonUI(importarButton)
        hbox.addWidget(importarButton)
        
        exportarButton = QToolButton()
        self.exportarButtonUI(exportarButton)
        hbox.addWidget(exportarButton)
                
        generarButton = QToolButton()
        self.generarButtonUI(generarButton)
        hbox.addWidget(generarButton)
        
        hbox.addStretch(1)
               
        # Add widgets to the layout
        vbox.addLayout(hbox)
        
        tabs = QTabWidget()
        tabDatos = QWidget()
        tabObjetos = QWidget()
        tabRelaciones = QWidget()
        		
        tabs.addTab(tabDatos, "Datos")
        tabs.addTab(tabObjetos,"Objetos")
        tabs.addTab(tabRelaciones,"Relaciones")
        self.tabDatosUI(tabDatos)
        self.tabObjetosUI(tabObjetos)
        self.tabRelacionesUI(tabRelaciones)
        
        vbox.addWidget(tabs)
        self.setLayout(vbox)

    def importarButtonUI(self, importarButton):
        importarButton.setText("&Importar")
        importarButton.setIcon(QtGui.QIcon("assets/images/importar.png")) #icon
        importarButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        importarButton.setShortcut('Ctrl+I')  #shortcut key
        importarButton.setToolTip("Importar Esquema") #Tool tip
        importarButton.setIconSize(QtCore.QSize(32,32))
        importarButton.clicked.connect(self.importar)

    def exportarButtonUI(self, exportarButton):
        exportarButton.setText("&Exportar")
        exportarButton.setIcon(QtGui.QIcon("assets/images/exportar.png")) #icon
        exportarButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        exportarButton.setShortcut('Ctrl+E')  #shortcut key
        exportarButton.setToolTip("Exportar Esquema") #Tool tip
        exportarButton.setIconSize(QtCore.QSize(32,32))
        exportarButton.clicked.connect(self.exportar)

    def generarButtonUI(self, generarButton):
        generarButton.setText("&Generar")
        generarButton.setIcon(QtGui.QIcon("assets/images/generar.png")) #icon
        generarButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        generarButton.setShortcut('Ctrl+G')  #shortcut key
        generarButton.setToolTip("Generar Código") #Tool tip
        generarButton.setIconSize(QtCore.QSize(32,32))
        generarButton.clicked.connect(self.generar)
		
    def tabDatosUI(self, tab):
        layout = QFormLayout()
        layout.addRow(" ", QWidget())
        self.editEmpresa = QLineEdit()
        self.editEmpresa.editingFinished.connect(self.actualizaEmpresa)
        layout.addRow("Empresa",self.editEmpresa)
        self.editAutor = QLineEdit()
        self.editAutor.editingFinished.connect(self.actualizaAutor)
        layout.addRow("Autor", self.editAutor)
        self.comboLenguaje = QComboBox()
        self.comboLenguaje.currentIndexChanged.connect(self.actualizaLenguaje)
        self.comboLenguaje.addItem(QtGui.QIcon("assets/images/none.png"), "")
        self.comboLenguaje.addItem(QtGui.QIcon("assets/images/django.png"), "Django")
        self.comboLenguaje.addItem(QtGui.QIcon("assets/images/laravel.png"), "Laravel")
        layout.addRow("Código",self.comboLenguaje)
        self.editNombreApp = QLineEdit()
        self.editNombreApp.editingFinished.connect(self.actualizaNombreApp)
        layout.addRow("Nombre App",self.editNombreApp)
        self.editVersion = QLineEdit()
        self.editVersion.editingFinished.connect(self.actualizaVersion)
        layout.addRow("Versión",self.editVersion)
        layout.addRow(" ", QWidget())
        tab.setLayout(layout)        
       
    def tabObjetosUiObjetos(self,hBox):
        # layout para los objetos
        labelObjetos = QLabel("Objetos")
        labelObjetos.setStyleSheet("font-weight: bold")
        self.listaObjetos = QListWidget()
        self.listaObjetos.setSelectionMode(QAbstractItemView.MultiSelection)
        vBoxObjetos = QVBoxLayout()
        buttonAddObjeto = QPushButton()
        buttonAddObjeto.setIcon(QtGui.QIcon("assets/images/add.png"))
        buttonAddObjeto.clicked.connect(self.addObjeto)
        buttonRemoveObjeto = QPushButton()
        buttonRemoveObjeto.setIcon(QtGui.QIcon("assets/images/remove.png"))
        buttonRemoveObjeto.clicked.connect(self.removeObjeto)
        buttonEditObjeto = QPushButton()
        buttonEditObjeto.setIcon(QtGui.QIcon("assets/images/edit.png"))
        buttonEditObjeto.clicked.connect(self.editObjeto)
        vBoxObjetos.addWidget(labelObjetos)
        vBoxObjetos.addWidget(self.listaObjetos)
        hBoxBotonesObjetos = QHBoxLayout()
        hBoxBotonesObjetos.addStretch(1)
        hBoxBotonesObjetos.addWidget(buttonAddObjeto)        
        hBoxBotonesObjetos.addWidget(buttonEditObjeto)
        hBoxBotonesObjetos.addWidget(buttonRemoveObjeto)
        vBoxObjetos.addLayout(hBoxBotonesObjetos)
        hBox.addLayout(vBoxObjetos)
    
    def tabObjetosUiMiembros(self,hBox):    
        # layout para lista de miembros de un objeto
        labelMiembros = QLabel("Miembros")
        labelMiembros.setStyleSheet("font-weight: bold")
        listaMiembros = QListWidget()
        vBoxMiembros = QVBoxLayout()
        buttonAddMiembro = QPushButton()
        buttonAddMiembro.setIcon(QtGui.QIcon("assets/images/add.png"))
        buttonAddMiembro.clicked.connect(self.addMiembro)
        buttonRemoveMiembro = QPushButton()
        buttonRemoveMiembro.setIcon(QtGui.QIcon("assets/images/remove.png"))
        buttonRemoveMiembro.clicked.connect(self.removeMiembro)
        buttonEditMiembro = QPushButton()
        buttonEditMiembro.setIcon(QtGui.QIcon("assets/images/edit.png"))
        buttonEditMiembro.clicked.connect(self.editMiembro)
        vBoxMiembros.addWidget(labelMiembros)
        vBoxMiembros.addWidget(listaMiembros)
        hBoxBotonesMiembros = QHBoxLayout()
        hBoxBotonesMiembros.addStretch(1)
        hBoxBotonesMiembros.addWidget(buttonAddMiembro)
        hBoxBotonesMiembros.addWidget(buttonEditMiembro)        
        hBoxBotonesMiembros.addWidget(buttonRemoveMiembro)
        vBoxMiembros.addLayout(hBoxBotonesMiembros)
        hBox.addLayout(vBoxMiembros)
                
    def tabObjetosUiPropiedades(self,hBox):       
        # layout con las propiedades de cada miembro    
        vBoxPropiedades = QVBoxLayout()
        labelPropiedades = QLabel("Propiedades Miembro")    
        labelPropiedades.setStyleSheet("font-weight: bold")
        vBoxPropiedades.addWidget(labelPropiedades)
        layoutPropiedades = QFormLayout()
        layoutPropiedades.addRow("Nombre",QLineEdit())
        comboTipo = QComboBox()
        comboTipo.addItem(QtGui.QIcon("assets/images/cadena.png"), "Cadena")
        comboTipo.addItem(QtGui.QIcon("assets/images/numero.png"), "Numérico")
        comboTipo.addItem(QtGui.QIcon("assets/images/float.png"), "Float")
        comboTipo.addItem(QtGui.QIcon("assets/images/boleano.png"), "Boleano")
        comboTipo.addItem(QtGui.QIcon("assets/images/enumerado.png"), "Enumerado")        
        layoutPropiedades.addRow("Tipo", comboTipo)   
        layoutPropiedades.addRow("Enumerados",QLineEdit())
        layoutPropiedades.addRow("Valor del tipo",QLineEdit())
        layoutPropiedades.addRow("Reglas",QLineEdit())  
        vBoxPropiedades.addLayout(layoutPropiedades) 
        vBoxPropiedades.addStretch(2)    
        hBox.addLayout(vBoxPropiedades)       
        
    def tabObjetosUI(self, tab):
        hBox = QHBoxLayout()
        self.tabObjetosUiObjetos(hBox) 
        self.tabObjetosUiMiembros(hBox)
        self.tabObjetosUiPropiedades(hBox)   
        tab.setLayout(hBox)
        
    def tabRelacionesUI(self, tab):
        OBJETO_1, RELACION, OBJETO_2 = range(3)
        
        vBoxRelaciones = QVBoxLayout()
        labelPropiedades = QLabel("Relaciones entre objetos")    
        labelPropiedades.setStyleSheet("font-weight: bold")
        dataView = QTreeView()
        dataView.setRootIsDecorated(False)
        dataView.setAlternatingRowColors(True)
        
        vBoxRelaciones.addWidget(labelPropiedades)
        vBoxRelaciones.addWidget(dataView)
        
        buttonAddRelacion = QPushButton("+")
        buttonRemoveRelacion = QPushButton("-")
        hBoxBotonesRelacion = QHBoxLayout()
        hBoxBotonesRelacion.addStretch(1)
        hBoxBotonesRelacion.addWidget(buttonRemoveRelacion)
        hBoxBotonesRelacion.addWidget(buttonAddRelacion)        
        vBoxRelaciones.addLayout(hBoxBotonesRelacion)
       
        
        model = QtGui.QStandardItemModel(0, 3, self)
        model.setHeaderData(OBJETO_1, QtCore.Qt.Horizontal, "Objeto-1")
        model.setHeaderData(RELACION, QtCore.Qt.Horizontal, "Relación")
        model.setHeaderData(OBJETO_2, QtCore.Qt.Horizontal, "Objeto-2")
        model.insertRow(0)
        model.setData(model.index(0, OBJETO_1), 'service@github.com')
        model.setData(model.index(0, RELACION), 'Your Github Donation')
        model.setData(model.index(0, OBJETO_2), '03/25/2017 02:05 PM')
        model.insertRow(1)
        model.setData(model.index(1, OBJETO_1), 'Objeto1')
        model.setData(model.index(1, RELACION), '1-M')
        model.setData(model.index(1, OBJETO_2), 'Objeto2')
        
        dataView.setModel(model)
        dataView.setColumnWidth(OBJETO_1,200)
        dataView.setColumnWidth(RELACION,200)
        dataView.setColumnWidth(OBJETO_2,200)

        tab.setLayout(vBoxRelaciones)
        
    def addMiembroDlgUI(self, objeto):
        qd = QDialog()
        qd.setWindowTitle(f'Objeto - {objeto}')
        qd.resize(300, 300)
        qd.setModal(True)

        # layout con las propiedades de cada miembro    
        vBoxPropiedades = QVBoxLayout()
        labelPropiedades = QLabel("Propiedades Miembro")    
        labelPropiedades.setStyleSheet("font-weight: bold")
        vBoxPropiedades.addWidget(labelPropiedades)
        layoutPropiedades = QFormLayout()
        layoutPropiedades.addRow("Nombre",QLineEdit())
        comboTipo = QComboBox()
        comboTipo.addItem(QtGui.QIcon("assets/images/cadena.png"), "Cadena")
        comboTipo.addItem(QtGui.QIcon("assets/images/numero.png"), "Numérico")
        comboTipo.addItem(QtGui.QIcon("assets/images/float.png"), "Float")
        comboTipo.addItem(QtGui.QIcon("assets/images/boleano.png"), "Boleano")
        comboTipo.addItem(QtGui.QIcon("assets/images/enumerado.png"), "Enumerado")        
        layoutPropiedades.addRow("Tipo", comboTipo)   
        layoutPropiedades.addRow("Enumerados",QLineEdit())
        layoutPropiedades.addRow("Valor del tipo",QLineEdit())
        layoutPropiedades.addRow("Reglas",QLineEdit())  
        vBoxPropiedades.addLayout(layoutPropiedades) 
        vBoxPropiedades.addStretch(2)    
        buttonAceptar = QPushButton("Aceptar")
        buttonAceptar.clicked.connect(self.aceptarAddMiembroDlg)
        buttonCancelar = QPushButton("Cancelar")
        buttonCancelar.clicked.connect(self.cancelarAddMiembroDlg)
        hBoxBotones = QHBoxLayout()
        hBoxBotones.addStretch(1)
        hBoxBotones.addWidget(buttonAceptar)        
        hBoxBotones.addWidget(buttonCancelar)
        vBoxPropiedades.addLayout(hBoxBotones)
        
        qd.setLayout(vBoxPropiedades)
        qd.setStandardButtons(QDialog.accept | QMessageBox.No)
        qd.setDefaultButton(QMessageBox.Yes)
        

        result = qd.exec_()
    
    
    def importar(self):
        # busco el archivo a importar y se lo paso el controlador
        archivo , check = QFileDialog.getOpenFileName(None, "Importar esquema de la App", "", "Archivos Json (*.json);;Todos los archivos (*)")
        if check:
            self.__controller.importar(archivo)
    
    def exportar(self):
        archivo , check = QFileDialog.getSaveFileName(None, "Exportar esquema de la App", self.__controller.getArchivoPorDefecto(), "Archivos Json (*.json)")
        if check:
            print(archivo)
            self.__controller.exportar(archivo)
    
    def generar(self):
        directorio = QFileDialog.getExistingDirectory(self, "Elija directorio para la App generada")
        print(directorio)
        self.__controller.generar(directorio)

    def actualizaEmpresa(self):
        self.__controller.setEmpresa(self.editEmpresa.text())

    def actualizaAutor(self):
        self.__controller.setAutor(self.editAutor.text())

    def actualizaLenguaje(self):
        if self.comboLenguaje.currentText():
            self.__controller.setLenguaje(self.comboLenguaje.currentText())
    
    def actualizaNombreApp(self):
        self.__controller.setNombreApp(self.editNombreApp.text())
    
    def actualizaVersion(self):
        self.__controller.setVersion(self.editVersion.text())

    def addObjeto(self):
        # abrimos un dialogo para escribir el nombre del objeto y lo añadimos a la lista
        nombre, ok = QInputDialog().getText(self, "Nuevo Objeto", "Nombre del OBJETO:")
        if ok and nombre:
            nombre = nombre.capitalize()
            self.__controller.addObjeto(nombre)            
            
    def removeObjeto(self):
        # si hay algún elemento seleccionado de la lista lo eliminamos
        for item in self.listaObjetos.selectedItems():
            msgBox = QMessageBox()
            msgBox.setMinimumWidth(400)
            msgBox.setText(" Eliminando " + item.text()+"!");
            msgBox.setInformativeText("¿Desea eliminar el objeto "+ item.text().upper() +"?")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDefaultButton(QMessageBox.Yes)
            msgBox.setIcon(QMessageBox.Question)
            respuesta = msgBox.exec()            
            if respuesta == QMessageBox.Yes:
                self.__controller.removeObjeto(item)
                
    def editObjeto(self):
        # abrimos un dialogo para modificar el nombre del objeto y lo actualizamos
        for item in self.listaObjetos.selectedItems():
            inputDialog = QInputDialog()
            inputDialog.setMinimumWidth(500)
            mensaje = f'Nombre ({item.text()}):'
            nombre, ok = inputDialog.getText(self, "Modificando Objeto", mensaje)
            if ok and nombre:
                nombre = nombre.capitalize()
                self.__controller.editObjeto(item, nombre)
    
    def addMiembro(self):
        if self.listaObjetos.count()>0:            
            items = self.listaObjetos.selectedItems()
            if items:
                print(f'Objeto seleccionado {items[0].text()}')
                # Hay un objeto selecionado al que añadiremos miembros
                datos = {}
                #self.__controller.addMiembro(items[0].text(), datos)
                self.addMiembroDlgUI(items[0].text())
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Para añadir un miembro a un Objeto")
                msg.setInformativeText("Debes de seleccionar primero un Objeto")
                msg.setWindowTitle("makeAA información")
                msg.setStandardButtons(QMessageBox.Ok)
                retval = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Para añadir un miembro a un Objeto")
            msg.setInformativeText("Debe de haber Objetos")
            msg.setWindowTitle("makeAA información")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
            
    def aceptarAddMiembroDlg(self):        
        pass
    
    def cancelarAddMiembroDlg(self):
        self.close()
    
            
    def removeMiembro(self):
        pass
    
    def editMiembro(self):
        pass    
         
   
        
                        
    

    def save_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            self.controller.save(self.email_var.get())

    def show_error(self, message):
        """
        Show an error message
        :param message:
        :return:
        """
        pass

    def show_success(self, message):
        """
        Show a success message
        :param message:
        :return:
        """
        pass
        

    def hide_message(self):
        """
        Hide the message
        :return:
        """
        pass    
