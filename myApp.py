# MyApp.py
# D. Thiebaut
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from views.mainwindow import Ui_MainWindow
from models.model import Model
from packages.importer import *
from packages.c45 import *
from packages.plotter import *
import packages.binaryTree as bt
import sys

class MainWindowUIClass(Ui_MainWindow):
    def __init__(self):
        ''' Inicialización de la UI '''
        # Inicializar la superclase
        super().__init__()
        # Incializar los modelos
        self.model = Model()
        
    def setupUi(self, MW):
        # Se configura la interfaz gráfica y se adhiere la funcionalidad
        # Configuración de la interfaz gráfica sobre el marco de la ventana
        super().setupUi(MW)

        # Ajustar geometría de elementos de pantalla
        self.separatorEdit.setFixedWidth(65)
        self.lineTerminatorEdit.setFixedWidth(65)
        self.testPerEdit.setFixedWidth(65)
        self.separatorLabel.setFixedWidth(163)
        self.lineTerminatorLabel.setFixedWidth(163)
        self.testPerLabel.setFixedWidth(163)
        self.thresholdEdit.setFixedWidth(65)
        # Conexión de eventos con funciones
        self.browseButton.clicked.connect(self.browseSlot)
        self.classifyButton.clicked.connect(self.classifySlot)
        self.confirmButton.clicked.connect(self.confirmSlot)
        self.discardButton.clicked.connect(self.discardSlot)

        # Inicializar elementos de la interfaz
        doubleValidator = QtGui.QDoubleValidator(decimals = 2)
        self.testPerEdit.setValidator(doubleValidator)
        self.thresholdEdit.setValidator(doubleValidator)
        self.disableItems([self.discardButton, self.fileBrowserFrame, self.thresholdFrame, self.classifyFrame])

    def setFile(self, fileName):
        # Verifica que el archivo sea valido y lo deja seleccionado. Caso contrario informa al usuario
        if not self.model.isValidFile(fileName):
            self.warningBox('El archivo seleccionado no existe o no se puede acceder.')
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
        self.classifyFrame.setEnabled(True)

    ''' Slots '''
    def confirmSlot(self):
        # Llamado cuando el usuario presiona el botón Confirmar
        self.debugPrint('Boton confirmar presionado')
        # Controla que se haya ingresado el porcentaje de elementos para prueba
        if self.testPerEdit.text() == '':
            self.warningBox('Debe indicar un porcentaje de elementos que serán usados para la prueba')
            return
        else:
            self.testPer = self.testPerEdit.text()
        # Asigna los valores para el separador y el fin de línea 
        if self.separatorEdit.text() == '':
            self.separator = ','
            self.separatorEdit.setText(self.separator)
        else:
            self.separator = self.separatorEdit.text()
        
        if self.lineTerminatorEdit.text() == '':
            self.lineTerminator = '\n'
            self.lineTerminatorEdit.setText('\\n')
        else:
            self.lineTerminator = self.lineTerminatorEdit.text()
        self.debugPrint('Separador: {0} \nFin de línea: {1} \nPorcentaje: {2}'.format(repr(self.separator), repr(self.lineTerminator), self.testPer))
        self.disableItems([self.confirmButton, self.configurationFrame])
        self.enableItems([self.discardButton, self.fileBrowserFrame, self.thresholdFrame])
        self.discardButton.setEnabled(True)
    
    def discardSlot(self):
        # Llamado cuando el usuario presiona el Botón Descartar
        self.debugPrint('Botón descartar presionado')
        self.enableItems([self.confirmButton, self.configurationFrame])
        self.disableItems([self.fileBrowserFrame, self.discardButton])
    
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
        if self.thresholdEdit.text() == '':
            self.warningBox('Debe ingresar un valor de umbral para la clasificación.')
            return
        threshold = float(self.thresholdEdit.text())
        problem = self.model.getProblem()
        tree = decisionTree(problem.data, problem.attributes, problem.classes, problem.classcolumn, bt.BinaryTree(), threshold)
        plt = plotSolution(problem, tree)
        self.debugPrint(str(tree))
        plt.show()

    ''' Utilidades '''    
    def disableItems(self, items):
        for i in items:
            i.setEnabled(False)
        return

    def enableItems(self, items):
        for i in items:
            i.setEnabled(True)
        return

    def warningBox(self, text):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(text)
        msg.setWindowTitle('Advertencia')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec()

    def debugPrint(self, msg):
        # Imprime un mensaje en la ventana de debug
        self.debugTextBrowser.append(msg)

def main():
    # El punto de entrada del programa
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowUIClass()
    ui.setupUi(MainWindow)
    MainWindow.setFixedSize(MainWindow.geometry().width(), MainWindow.geometry().height())
    MainWindow.setWindowTitle('Árboles de decisión')
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()