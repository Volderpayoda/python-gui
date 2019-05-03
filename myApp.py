# MyApp.py
# D. Thiebaut
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from views.mainwindow import Ui_MainWindow
from models.model import Model
from packages.importer import *
from packages.c45 import *
import packages.binaryTree as bt
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

        # Ajustar geometría de elementos de pantalla
        self.separator.setFixedWidth(65)
        self.lineTerminator.setFixedWidth(65)
        self.testPer.setFixedWidth(65)
        
        # Conexión de eventos con funciones
        self.browseButton.clicked.connect(self.browseSlot)
        self.classifyButton.clicked.connect(self.classifySlot)
        self.confirmButton.clicked.connect(self.confirmSlot)
        self.discardButton.clicked.connect(self.discardSlot)

    def debugPrint(self, msg):
        # Imprime un mensaje en la ventana de debug
        self.debugTextBrowser.append(msg)

    def setFile(self, fileName):
        # Verifica que el archivo sea valido y lo deja seleccionado. Caso contrario informa al usuario
        if not self.model.isValidFile(fileName):
            warningBox('El archivo seleccionado no existe o no se puede acceder.')
            return 
        if not self.model.isCsv(fileName):
            self.warningBox('El archivo seleccionado no es de tipo CSV.')
            return
        problem = import_csv(fileName)
        if not self.model.isValidProblem(problem):
            self.warningBox('El conjunto de datos seleccionado debe contener solo 2 atributos.')
            return
        self.debugPrint('Archivo seleccionado: {0}'.format(fileName))
        self.trainingLineEdit.setText(fileName)
        self.model.setFileName(fileName)
        self.model.setProblem(problem)
        self.classifyButton.setEnabled(True)

    def warningBox(self, text):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(text)
        msg.setWindowTitle('Advertencia')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec()

    # Slots del programa para el entrenamiento
    def browseSlot(self):
        # Llamado cuando el usuario presiona el Boton Examinar
        self.debugPrint('Botón examinar presionado')
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName()
        if fileName: 
            self.setFile(fileName)
        else:
            self.debugPrint("No se seleccionó ningún archivo")
    
    def classifySlot(self):
        # TODO: En este punto se llamaría al algoritmo de clasificación
        self.debugPrint("Botón clasificar presionado")
        problem = self.model.getProblem()
        tree = decisionTree(problem.data, problem.attributes, problem.classes, problem.classcolumn, bt.BinaryTree(), 0.1)
        self.debugPrint(str(tree))

    def confirmSlot(self):
        self.debugPrint('Boton confirmar presionado')
        # Controla que se haya ingresado el porcentaje de elementos para prueba
        if self.testPer.text() == '':
            self.warningBox('Debe indicar un porcentaje de elementos que serán usados para la prueba')
            return
        else:
            testPer = self.testPer.text()
        # Asigna los valores para el separador y el fin de línea 
        if self.separator.text() == '':
            separator = ','
        else:
            separator = self.separator.text()
        
        if self.lineTerminator.text() == '':
            lineTerminator = '\n'
        else:
            lineTerminator = self.lineTerminator.text()
        # self.debugPrint('Separador: {0} \n Fin de línea: {1} \n Porcentaje: {2}'.format(separator, lineTerminator, testPer)
        self.confirmButton.setEnabled(False)
        self.configurationFrame.setEnabled(False)
    
    def discardSlot(self):
        self.confirmButton.setEnabled(True)
        self.configurationFrame.setEnabled(True)     

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