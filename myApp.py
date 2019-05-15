# MyApp.py
# D. Thiebaut
from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtCore import QObject, pyqtSlot
from views.mainwindow import Ui_MainWindow
from models.model import Model
from packages.importer import *
from packages.c45 import *
from packages.plotter import *
import packages.classifier as cf
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
        self.confirmButton.clicked.connect(self.confirmSlot)
        self.discardButton.clicked.connect(self.discardSlot)
        self.browseButton.clicked.connect(self.browseSlot)
        self.buildTreeButton.clicked.connect(self.buildTreeSlot)
        self.classificationButton.clicked.connect(self.classificationSlot)
        self.plotDataButton.clicked.connect(self.plotDataSlot)

        # Inicializar elementos de la interfaz.
        doubleValidator = QtGui.QDoubleValidator(decimals = 2)
        self.testPerEdit.setValidator(doubleValidator)
        self.thresholdEdit.setValidator(doubleValidator)
        self.disableItems([self.discardButton, self.fileBrowserFrame, self.thresholdFrame, self.buildTreeFrame, self.treeOptionsFrame])
        self.gainRadioButton.setChecked(True)
        self.thresholdEdit.setToolTip('Umbral de ganancia de información')
        self.classificationButton.setToolTip('Ingrese dos atributos para la predicción')

    def setFile(self, fileName):
        # Verifica que el archivo sea valido y lo deja seleccionado. Caso contrario informa al usuario
        if not self.model.isValidFile(fileName):
            self.warningBox('El archivo seleccionado no existe o no se puede acceder.')
            return 
        if not self.model.isCsv(fileName):
            self.warningBox('El archivo seleccionado no es de tipo CSV.')
            return
        try:
            problem = import_csv(path = fileName, sep = self.separator, lineterminator = self.lineTerminator)
        except:
            self.warningBox('El archivo seleccionado no existe o no se puede acceder.')
            return
        if not self.model.isValidProblem(problem):
            self.warningBox('El conjunto de datos seleccionado debe contener solo 2 atributos.')
            return
        self.debugPrint('Archivo seleccionado: {0}'.format(fileName))
        self.trainingLineEdit.setText(fileName)
        self.model.setFileName(fileName)
        self.model.setProblem(problem)
        self.buildTreeFrame.setEnabled(True)

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
        self.debugPrint('Botón Descartar presionado')
        self.enableItems([self.confirmButton, self.configurationFrame])
        self.disableItems([self.fileBrowserFrame, self.discardButton, self.thresholdFrame])
    
    def browseSlot(self):
        # Llamado cuando el usuario presiona el Boton Examinar
        self.debugPrint('Botón Examinar presionado')
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName()
        if fileName: 
            self.setFile(fileName)
        else:
            self.debugPrint("No se seleccionó ningún archivo")
    
    def buildTreeSlot(self):
        # TODO: En este punto se llamaría al algoritmo de clasificación
        self.debugPrint("Botón Construir árbol presionado")
        if self.thresholdEdit.text() == '':
            self.warningBox('Debe ingresar un valor de umbral para la clasificación.')
            return
        threshold = float(self.thresholdEdit.text())
        problem = self.model.getProblem()
        tree = decisionTree(problem.data, problem.attributes, problem.classes, problem.classcolumn, bt.BinaryTree(), threshold)
        # plt = plotSolution(problem, tree)
        self.model.tree = tree
        self.enableItems([self.treeOptionsFrame])
        self.debugPrint(str(self.model.tree))
        # plt.show()

    def classificationSlot(self):
        self.debugPrint('Botón Clasificar presionado')
        item, ok = QtWidgets.QInputDialog.getText(QtWidgets.QWidget(), 'Clasificar', 'Ingrese el dato a clasificar\nFormato: atributo1, atributo2')
        if ok:
            item.replace(' ', '')
            data = item.split(',')
            try:
                data[0] = float(data[0])
                data[1] = float(data[1])
            except:
                self.warningBox('El formato de los datos introducidos es inválido')
                return
            if len(data) != 2:
                self.warningBox('Se deben introducir solamente dos parámetros separados por una coma')
                return
            classifier = cf.Classifier(self.model.problem.attributes)
            prediction = classifier.classifyData(self.model.tree, data)
            self.infoBox('Los valores introducidos pertenecen a la clase: ' + prediction)

    def plotDataSlot(self):
        plt = plotSolution(self.model.problem, self.model.tree)
        plt.title('Visualización de datos')
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

    def infoBox(self, text):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(text)
        msg.setWindowTitle('Resultado')
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