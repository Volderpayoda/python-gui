from os import path
# Modelo del patrón MVC generado para el manejo del archivo de datos
# Solamente se aceptan archivos CSV
class Model:
    def __init__(self):
        # Constructor del modelo, pone el nombre del archivo en nulo
        self.fileName = None
        self.problem = None
        self.tree = None
        self.threshold = None

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
        return problem.attributes.size == 2

    # Setters y getters
    def setFileName(self, fileName):
        self.fileName = fileName
            
    def getFileName(self):
        return self.fileName

    def setProblem(self, problem):
        self.problem = problem
    
    def getProblem(self):
        return self.problem
