from os import path
# Modelo del patrón MVC generado para el manejo del archivo de datos
# Solamente se aceptan archivos CSV
class Model:
    def __init__(self):
        # Constructor del modelo, pone el nombre del archivo en nulo
        self.fileName = None

    def isValid(self, fileName):
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

    def setFileName(self, fileName):
        if self.isValid(fileName):
            self.fileName = fileName
        # Completar, ¿qué debería pasar si el archivo es inválido?
            
    def getFileName(self):
        # Retorna el nombre del archivo
        return self.fileName