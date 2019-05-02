# MyApp.py
# D. Thiebaut
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from views.mainwindow import Ui_MainWindow
from models.model import Model
from packages.importer import *
import sys

class MainWindowUIClass(Ui_MainWindow):
    def __init__(self):
        # Inicializar la superclase
        super().__init__()
        # Incializar los modelos
        self.model = Model()
        
    def setupUi(self, MW):
        # Se configura la interfaz gráfica y se adhiere la funcionalidad
        # Configuración de la interfaz gráfica sobre el marco de la ventana
        super().setupUi(MW)

        # Conexión de eventos con funciones
        self.browseButton.clicked.connect(self.browseSlot)
        self.classifyButton.clicked.connect(self.classifySlot)

    def debugPrint(self, msg):
        # Imprime un mensaje en la ventana de debug
        self.debugTextBrowser.append(msg)

    def setFile(self, fileName):
        # Verifica que el archivo sea valido y lo deja seleccionado. Caso contrario informa al usuario
        flag, msg = self.model.setModel(fileName)
        if not flag:
            self.warningBox(msg)
        self.debugPrint("Archivo seleccionado: {0}".format(fileName))
        self.trainingLineEdit(fileName)

    def warningBox(self, text):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(text)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec()

    # Slots del programa para el entrenamiento
    def browseSlot(self):
        # Llamado cuando el usuario presiona el Boton Examinar
        self.debugPrint("Botón examinar presionado")
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName()
        if fileName: 
            self.setFile(fileName)
        else:
            self.debugPrint("No se seleccionó ningún archivo")
    
    def classifySlot(self):
        # TODO: En este punto se llamaría al algoritmo de clasificación
        self.debugPrint("Botón clasificar presionado")
        problem = self.model.getProblem()
        for key in problem:
            self.debugPrint("{0}: ".format(key))
            self.debugPrint(str(problem[key]))
    
    # Slots del programa para la prueba
    def testBrowseSlot(self):
        # TODO
        pass
    def testTestSlot(self):
        # TODO
        pass

def main():
    # El punto de entrada del programa
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowUIClass()
    ui.setupUi(MainWindow)
    MainWindow.setFixedSize(MainWindow.geometry().width(), MainWindow.geometry().height())
    MainWindow.show()
    sys.exit(app.exec_())

main()