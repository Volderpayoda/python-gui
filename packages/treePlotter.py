import time
from os import path
def plotTree(tree, libPath):
    f = open(path.abspath('./views/template.html'), 'r')
    s = f.read()
    s = s.replace('treeDataJson', tree)
    s = s.replace('libPath', libPath)
    temp = str(time.time()) + '.html'
    filePath = path.abspath(path.join('./temp', temp))
    o = open(filePath, 'a')
    o.write(s)
    o.close()
    return filePath
