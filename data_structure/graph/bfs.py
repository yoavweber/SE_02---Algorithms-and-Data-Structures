from queue import Queue


def setInputToNodes():
    stringVertex = list(input('insert edge: ').split(" "))
    vertex = [int(stringVertex[0]),int(stringVertex[1])]
    return vertex


def addNodesToDict(vertex,nodeList):
    for i in range(2):
        try: 
            nodeList[vertex[i-1]].append(vertex[i]) 
        except KeyError:
            nodeList[vertex[i-1]] = [vertex[i]]


def setNodeDict():
    NodeList = {}
    inputAmount = int(input("Type the amount of connected nodes you would like to insert: "))
    for i in range(inputAmount):
        vertex = setInputToNodes()
        addNodesToDict(vertex,NodeList)
    return NodeList


def getConnectedNodesList(NodeList):
    connectedNodesList = []
    connectedNodes = set()
    for node in NodeList.keys():
        if node not in connectedNodes:
            bfsConnectedNodes = bfs(NodeList,node)
            connectedNodes.update(bfsConnectedNodes)
            connectedNodesList.append(bfsConnectedNodes)
    return connectedNodesList


def bfs(NodeList,node):
    queue = Queue(node)
    visitedNodes = set()

    while queue.isEmpty() == False:
        currentNode = queue.pop()
        visitedNodes.add(currentNode)
        for n in NodeList[currentNode]:
            if n not in visitedNodes and not queue.inQueue(n):
                queue.add(n)
    return visitedNodes


def getMaxSetLength(setList):
    maxSet = {}
    for i in setList:
        if len(i) > len(maxSet):
            maxSet = i
    return len(maxSet)


def getMinSetLength(setList):
    minSet = set(setList[0])
    for i in setList:
        if len(i) < len(minSet):
            minSet = i    
    return len(minSet)

def executeScript():
    nodeList = setNodeDict()
    res = getConnectedNodesList(nodeList)
    setMaxLength = getMaxSetLength(res) 
    setMinLength = getMinSetLength(res)
    print(f'min connected nodes: {setMinLength} , max connected nodes {setMaxLength}')
    return setMinLength , setMaxLength




executeScript()

