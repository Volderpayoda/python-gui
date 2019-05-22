import matplotlib.cm as cm
import matplotlib.pyplot as plt

def plotSolution(problem, tree):
    # Graficar los puntos discriminando por clase
    plotData(problem, tree)
    # Obtener los nombres de los atributos
    axx, axy = getAxis(problem)
    # Obtener mínimox y máximos de cada columna atributo 
    xmin, xmax = getLimits(problem, axx)
    ymin, ymax = getLimits(problem, axy)
    # Realizar el particionado recursivo del conjunto de datos
    partitionPlot(tree, axx, axy, xmin, xmax, ymin, ymax)
    # Indicar titulo del gráfico
    plt.title('Visualización de datos')
    # Indicar nombres de los ejes
    plt.xlabel(problem.attributes[0])
    plt.ylabel(problem.attributes[1])
    # Activar la leyenda del gráfico
    plt.legend()
    # Desplazar el gráfico 
    mngr = plt.get_current_fig_manager()
    mngr.window.setGeometry(50,100,640, 545)
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

def plotData(problem, tree):
    color = cm.get_cmap(name = 'tab20')
    i = 0.0
    for c in problem.classes:
        dataTemp = problem.data.loc[problem.data[problem.classcolumn] == c]
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
