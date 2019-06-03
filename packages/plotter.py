import matplotlib.cm as cm
import matplotlib.pyplot as plt

def plotSolution(problem, tree):
    # Reiniciar el gráfica
    plt.clf()
    # Obtener los nombres de los atributos
    axx, axy = getAxis(problem)
    # Obtener mínimox y máximos de cada columna atributo 
    xmin, xmax = getLimits(problem, axx)
    ymin, ymax = getLimits(problem, axy)
    # Realizar el particionado recursivo del conjunto de datos
    partitionPlot(tree, axx, axy, xmin, xmax, ymin, ymax)
    # Ajustar los puntos para que no se corten con la recta
    dataAdjust = adjustPoints(problem)
    # Graficar los puntos discriminando por clase
    plotData(problem, tree, dataAdjust)
    # Indicar titulo del gráfico
    plt.title('Visualización de datos')
    # Indicar nombres de los ejes
    plt.xlabel(problem.attributes[0])
    plt.ylabel(problem.attributes[1])
    # Activar la leyenda del gráfico
    plt.legend()
    # Retornar el gráfico
    return plt

def getAxis(problem):
    axx = problem.attributes[0]
    axy = problem.attributes[1]
    return axx, axy

def getLimits(problem, axis):
    min = problem.data[axis].min()
    max = problem.data[axis].max()
    return min, max

def adjustPoints(problem):
    dataAdjust = problem.data.copy()
    axx, axy = getAxis(problem)
    # Calcular la cantidad de decimales en X
    decx = problem.data[axx].apply(lambda x: len(str(x).split('.')[1]))
    decx = decx.max()
    # Calcular la cantidad de decimales en Y
    decy = problem.data[axy].apply(lambda x: len(str(x).split('.')[1]))
    decy = decy.max()
    # Calcular valores de desplazamiento
    despx = 7.0 * (10.0 ** (-(decx + 1)))
    despy = 7.0 * (10.0 ** (-(decy + 1)))
    dataAdjust[axx] = problem.data[axx].apply(lambda x: x - despx)
    dataAdjust[axy] = problem.data[axy].apply(lambda x: x - despy)
    return dataAdjust

def plotData(problem, tree, dataAdjust):
    color = cm.get_cmap(name = 'tab20')
    i = 0.0
    for c in problem.classes:
        dataTemp = dataAdjust.loc[dataAdjust[problem.classcolumn] == c]
        x = dataTemp[problem.attributes[0]]
        y = dataTemp[problem.attributes[1]]
        plt.scatter(x = x, y = y, marker = 'o', c = [color(i)], label = c)
        i = i + 0.05

def partitionPlot(tree, axx, axy, xmin, xmax, ymin, ymax):
    left = tree.left
    right = tree.right
    if tree.cargo.type == 'decision':
        attribute = tree.cargo.value
        if attribute == axx:
            plt.vlines(x = tree.cargo.limit, ymin = ymin, ymax = ymax)
            partitionPlot(left, axx, axy, xmin, tree.cargo.limit, ymin, ymax)
            partitionPlot(right, axx, axy, tree.cargo.limit, xmax, ymin, ymax)
        if attribute == axy:
            plt.hlines(y = tree.cargo.limit, xmin = xmin, xmax = xmax)
            partitionPlot(left, axx, axy, xmin, xmax, ymin, tree.cargo.limit)
            partitionPlot(right, axx, axy, xmin, xmax, tree.cargo.limit, ymax)
