import random
import heapq

class GridNode:
    def __init__(self, x: int, y: int, nodeVal: str):
        self.x=x
        self.y=y
        self.val=nodeVal
        self.neighbors=set()

class GridGraph:

    #todo, add remove
    def __init__(self):
        self.nodes=[]
    
    def addGridNode(self, x: int, y: int, nodeVal: str) -> None:
        self.nodes.append(GridNode(x,y,nodeVal))
    
    def addUndirectedEdge(self, first: GridNode, second: GridNode) -> None:
        if abs(abs(first.x)+abs(first.y)-abs(second.x)-abs(second.y))<2:
            if first not in second.neighbors:
                second.neighbors.add(first)
            if second not in first.neighbors:
                first.neighbors.add(second)
    
    def removeUndirectedEdge(self, first: GridNode, second: GridNode) -> None:
        if first in second.neighbors:
            second.neighbors.remove(first)
        if second in first.neighbors:
            first.neighbors.remove(second)
    
    def getAllNodes(self) -> set:
        return set(self.nodes)

    def getPointer(self, searchNode: str) -> object:
        for node in self.nodes:
            if node.val==searchNode:
                return node

def createRandomGridGraph(n: int) -> GridGraph:
    randomGraph=GridGraph()
    #directions say n*2 but it is actually (n+1)^2 based on the description.
    n+=1
    for y in range(n):
        for x in range(n):
            randomGraph.addGridNode(y,x,str(x)+","+str(y))
            probability=random.randint(0,1)
            if x!=0 and probability==1:
                randomGraph.addUndirectedEdge(randomGraph.getPointer(str(x-1)+","+str(y)),randomGraph.getPointer(str(x)+","+str(y)))

            probability=random.randint(0,1)
            if y!=0 and probability==1:
                randomGraph.addUndirectedEdge(randomGraph.getPointer(str(x)+","+str(y-1)),randomGraph.getPointer(str(x)+","+str(y)))
    return randomGraph

def astar(sourceNode: GridNode, destNode: GridNode) -> list:
    distance=0
    priorityQueue=[]
    heapq.heapify(priorityQueue)
    finalized=set()
    finalized.add(sourceNode)
    currNode=sourceNode
    
    nodes=dict()
    nodes[sourceNode.val]=sourceNode

    heuristic=abs(sourceNode.x-destNode.x)+abs(sourceNode.y-destNode.y)
    heapq.heappush(priorityQueue,(heuristic,distance,sourceNode.val))

    while currNode!=destNode:
        neighbors=currNode.neighbors-finalized
        if neighbors==set():
            if currNode==sourceNode:
                return float('inf')
            finalized.add(currNode)
        else:
            for neighbor in neighbors:
                    heuristic=abs(neighbor.x-destNode.x)+abs(neighbor.y-destNode.y)
                    finalized.add(neighbor)
                    nodes[neighbor.val]=neighbor
                    heapq.heappush(priorityQueue,(heuristic,distance+1,neighbor.val))
        
        heuristic,distance,currNodeVal=heapq.heappop(priorityQueue)
        currNode=nodes[currNodeVal]
    return distance

randGraph=createRandomGridGraph(100)
sourceNode=randGraph.nodes[0]
destNode=randGraph.nodes[-1]
print("101x101 graph result:",astar(sourceNode,destNode))

result={}

for i in range(150):
    randGraph=createRandomGridGraph(15)
    sourceNode=randGraph.nodes[0]
    destNode=randGraph.nodes[-1]
    answer=astar(sourceNode,destNode)
    result[answer]=result.get(answer,0)+1

print("\n150 Results in a 16x16 graph (result: frequency):")
print(result)

print("If you want to see more results, increase the probability of connected nodes!")