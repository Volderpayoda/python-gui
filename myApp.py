# MyApp.py
# D. Thiebaut
from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtCore import QObject, pyqtSlot
from views.mainwindow import Ui_MainWindow
from models.model import Model
from packages.importer import *
from packages.c45 import *
from packages.plotter import *
from packages.treePlotter import *
from packages.worker import *
import packages.classifier as cf
import packages.binaryTree as bt
import sys
import webbrowser
import os

class MainWindowUIClass(Ui_MainWindow):
    def __init__(self):
        ''' Inicialización de la UI '''
        # Inicializar la superclase
        super().__init__()
        # Incializar los modelos
        self.threadPool = QtCore.QThreadPool()
        
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
        self.plotTreeButton.clicked.connect(self.plotTreeSlot)

        # Inicializar elementos de la interfaz.
        self.testPerEdit.setValidator(QtGui.QDoubleValidator(bottom = 0, top = 1))
        self.thresholdEdit.setValidator(QtGui.QDoubleValidator(bottom = 0, top = 1))
        self.disableItems([self.discardButton, self.fileBrowserFrame, self.thresholdFrame, self.buildTreeFrame, self.treeOptionsFrame])
        self.gainRadioButton.setChecked(True)
        self.thresholdEdit.setToolTip('Debe ser mayor o igual a cero\nUse "." como separador decimal\nEjemplo: 0.001')
        self.testPerEdit.setToolTip('Debe ser mayor a 0 y menor que 1\nUse "." como separador decimal\nEjemplo: 0.1')
        self.classificationButton.setToolTip('Ingrese dos atributos para la predicción')

    def setFile(self, fileName):
        self.model = Model()
        self.model.testPer = self.testPer
        # Verifica que el archivo sea valido y lo deja seleccionado. Caso contrario informa al usuario
        if not self.model.isValidFile(fileName):
            self.warningBox('El archivo seleccionado no existe o no se puede acceder.')
            return 
        if not self.model.isCsv(fileName):
            self.warningBox('El archivo seleccionado no es de tipo CSV.')
            return
        try:
            problem = import_csv(path = fileName, sep = self.separator, lineterminator = self.lineTerminator, testPer = self.testPer)
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
        self.debugPrint('Cantidad de datos para entrenamiento: ' + str(self.model.problem.data.shape[0]))
        self.debugPrint('Cantidad de datos para prueba: ' + str(self.model.problem.testData.shape[0]))
        self.treeOptionsFrame.setEnabled(False)
        self.buildTreeFrame.setEnabled(True)

    ''' Slots '''
    def confirmSlot(self):
        # Llamado cuando el usuario presiona el botón Confirmar
        self.debugPrint('Boton confirmar presionado')
        # Controla que se haya ingresado el porcentaje de elementos para prueba
        if self.testPerEdit.text() == '':
            self.warningBox('Debe indicar un porcentaje de elementos que serán usados para la prueba')
            return
        self.testPer = float(self.testPerEdit.text().replace(',', '.'))
        if self.testPer <= 0 or self.testPer >= 1:
            self.warningBox('El porcentaje de elementos para prueba debe ser un valor comprendido mayor que 0 y menor que 1')
            return
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
        self.trainingLineEdit.setText('')
        self.enableItems([self.confirmButton, self.configurationFrame])
        self.disableItems([self.fileBrowserFrame, self.discardButton, self.thresholdFrame, self.treeOptionsFrame, self.buildTreeFrame])
        self.model = None
    
    def browseSlot(self):
        # Llamado cuando el usuario presiona el Boton Examinar
        self.debugPrint('Botón Examinar presionado')
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName()
        if fileName: 
            self.setFile(fileName)
        else:
            self.debugPrint("No se seleccionó ningún archivo")
    
    def buildTreeSlot(self):
        self.debugPrint("Botón Construir árbol presionado")
        # Recuperar valor de umbral
        if self.thresholdEdit.text() == '':
            self.warningBox('Debe ingresar un valor de umbral para la clasificación.')
            return
        self.model.threshold = float(self.thresholdEdit.text().replace(',', '.'))
        # Recuperar función de ganancia
        if self.gainRadioButton.isChecked():
            self.model.gainFunc = 'gain'
        if self.gainRatioRadioButton.isChecked(): 
            self.model.gainFunc = 'gainRatio'
        # Construir el árbol
        problem = self.model.getProblem()
        threshold = self.model.threshold
        gainFunc = self.model.gainFunc
        # tree = decisionTree(problem.data, problem.attributes, problem.classes, problem.classcolumn, bt.BinaryTree(), threshold)
        worker = Worker(decisionTree, problem.data, problem.attributes, problem.classes, problem.classcolumn, bt.BinaryTree(), threshold, gainFunc)
        worker.signals.result.connect(self.treeResultSlot)
        worker.signals.finished.connect(self.treeFinishedSlot)
        self.disableItems([self.centralwidget])
        self.threadPool.start(worker)
        # Habilitar opciones del árbol

    def treeResultSlot(self, tree):
        self.model.tree = tree
    
    def treeFinishedSlot(self):
        self.debugPrint('Proceso de construcción finalizado')
        self.debugPrint('Iniciando cálculo de precisión')
        classifier = cf.Classifier(self.model.problem.attributes)
        worker = Worker(classifier.classifyDataFrame, self.model.tree, self.model.problem.testData)
        worker.signals.result.connect(self.accuracyResultSlot)
        worker.signals.result.connect(self.accuracyFinishedSlot)
        self.threadPool.start(worker)

    def accuracyResultSlot(self, acc):
        self.model.accuracy = acc

    def accuracyFinishedSlot(self):
        self.debugPrint('Precisión: ' + str(self.model.accuracy * 100) + '%')
        self.infoBox('Se ha terminado la construcción del modelo.\nLa precisión es: ' + str(self.model.accuracy * 100) + '%')
        self.enableItems([self.treeOptionsFrame, self.centralwidget])

    def classificationSlot(self):
        self.debugPrint('Botón Clasificar presionado')
        item, ok = QtWidgets.QInputDialog.getText(QtWidgets.QWidget(), 'Clasificar', 'Ingrese el dato a clasificar\nUse "." como separador decimal y "," como separador de campo\nEjemplo: 5.0, 3.4')
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
            self.infoBox('Los valores introducidos pertenecen a la clase: ' + prediction + '\nPrecisión de la estimación: ' + str(self.model.accuracy * 100) + '%')

    def plotDataSlot(self):
        plt = plotSolution(self.model.problem, self.model.tree)
        plt.show()
    
    def plotTreeSlot(self):
        libPath = '../packages/d3js/d3.v3.min.js'
        filePath = plotTree(self.model.tree.toJson(), libPath)
        webbrowser.open(filePath)

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
    # Limpiar archivos temporales de ejecuciones anteriores
    if os.path.exists('./temp'):
        files = os.listdir('./temp')
        for f in files:
            os.remove(os.path.join('./temp', f))
    else:
        os.mkdir('./temp')
    # Iniciar la aplicación
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