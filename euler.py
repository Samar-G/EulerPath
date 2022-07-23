def getAdjacencyList(graph):
    nodes=graph['nodes']
    edges=graph['edges']
    adjList={}
    
    for node in nodes:
        nodeAdj = []
        for edge in edges:
            if node == edge[0]:
#                print(node)
#                print(edge[0])
                 nodeAdj.append(edge[1])
            adjList[node] = nodeAdj     
    return adjList

v = []
adjList = {}
def DFS(currentNode):
    global v
#    print(type(adjList[currentNode]))
    while len(adjList[currentNode]) != 0:
        u = adjList[currentNode][0]
        adjList[currentNode] = adjList[currentNode][1:]
        DFS(u)
    v.append(currentNode) 

def pathList(graph, stNode):
    global adjList
    adjList = getAdjacencyList(graph)
   
    DFS(stNode)
    print(v)
    seq = v[0]
    for path in v[1:]:
        seq += path[0]
    return seq

read = ['TTACGTT', 'CCGTTA', 'GTTAC', 'GTTCGA', 'CGTTC']
graph={'nodes':['TAC','ACA','CAC'],'edges':[['TAC','ACA'],['ACA','CAC'],['ACA','CAC'],['CAC','ACA']]}

seq = pathList(graph, "TAC")
print(seq)
