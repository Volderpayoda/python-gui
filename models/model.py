from os import path
from ..packages.importer import *
# Modelo del patrón MVC generado para el manejo del archivo de datos
# Solamente se aceptan archivos CSV
class Model:
    def __init__(self):
        # Constructor del modelo, pone el nombre del archivo en nulo
        self.fileName = None
        self.problem = None

    def isValid(self, fileName):
        if not isValidFile(fileName):
            return False, "El archivo seleccionado no existe o no puede abrirse"
        if not isCsv(fileName):
            return False, "El archivo seleccionado no es un CSV"        
        return True, ""

    def isValidFile(self, fileName):
        # Retorna verdadero si el archivo existe y puede ser abierto
        try:
            file = open(fileName, 'r')
            file.close()
            return True
        except:
            return False
    
    def isCsv(self, fileName):
        # Retorna verdadero si el archivo es un CSV
        _, ext = path.splitext(fileName)
        if ext.lower() == '.csv':
            return True
        return False
    
    def isValidProblem(self, problem):
        if problem.attributes.size != 2:
            return False, "El modelo debe contener obligatoriamente 2 atributos"
        return True, ""

    def setModel(self, fileName):
        # Valida que el archivo seleccionado sea válido
        flag, msg = self.isValid(fileName)
        if not flag:
            return False, msg
        problem = import_csv(fileName)
        # Valida que el problema de clasificación sea válido
        flag = msg = self.isValidProblem(problem)
        if not flag:
            return False, msg
        # Configurar el modelo
        self.setFileName(fileName)
        self.setProblem(problem)
        return True, ""

    # Setters y getters
    def setFileName(self, fileName):
        self.fileName = fileName
            
    def getFileName(self):
        return self.fileName

    def setProblem(self, problem):
        self.problem = problem
    
    def getProblem(self):
        return self.problem
