from problem3 import *

class NewNode():
    def __init__(self, val: int) -> None:
        self.val=val
        self.neighbors=dict()

    def __str__(self) -> str:
        neighs=self.neighbors
        res=""
        for node in neighs:
            res+=node+":"+str(self.neighbors[node])+","
        res=res[:-1]
        return "Val: "+self.val +", Neighbors:"+"["+res+"]"

class WeightedGraph(Graph):
    def addNode(self, nodeVal: str) -> None:
        self.nodes[nodeVal]=NewNode(nodeVal)

    def __str__(self) -> str:
        printable=dict()
        for node in self.nodes:
            temp=[]
            for key in self.nodes[node].neighbors.keys():
                temp.append((key,self.nodes[node].neighbors[key]))
            printable[node]=temp
        return str(printable)

    def addWeightedEdge(self, first: NewNode, second: NewNode, edgeWeight: int) -> None:
        firstNeighbors=[node for node in self.nodes[first.val].neighbors.keys()]
        if second.val not in firstNeighbors:
            self.nodes[first.val].neighbors[second.val]=edgeWeight
    
    def getTotalEdges(self) -> int:
        count=0
        for node in self.nodes:
            count+=len(self.nodes[node].neighbors)
        return count
    
def createRandomCompleteWeightedGraph(n: int) -> WeightedGraph:
    randomGraph=WeightedGraph()
    for i in range(n):
        randomGraph.addNode(str(i))
    for i in range(n):
        higherNode=i+1
        while higherNode<n:
            randomWeight=random.randint(1,100)
            randomGraph.addWeightedEdge(randomGraph.getPointer(str(i)),randomGraph.getPointer(str(higherNode)),randomWeight)
            higherNode+=1
        lowerNode=i-1
        while lowerNode!=-1:
            randomWeight=random.randint(1,100)
            randomGraph.addWeightedEdge(randomGraph.getPointer(str(i)),randomGraph.getPointer(str(lowerNode)),randomWeight)
            lowerNode-=1
    return randomGraph

def createALinkedList(n: int) -> WeightedGraph:
    linkedList=WeightedGraph()
    for i in range(n):
        linkedList.addNode(str(i))
        if i!=0:
            linkedList.addWeightedEdge(linkedList.getPointer(str(i)),linkedList.getPointer(str(i-1)),1)
            linkedList.addWeightedEdge(linkedList.getPointer(str(i-1)),linkedList.getPointer(str(i)),1)
    return linkedList

def dijkstras(start: NewNode) -> dict:
    paths=dict()
    visited=[]
    return start.neighbors
    for node in start.neighbors:
        pass
    return paths


#rand=createRandomCompleteWeightedGraph(10)
#print(rand)
#print("Total edges:",rand.getTotalEdges())

LL=createALinkedList(10)
#print(LL)
#print("Total edges:",LL.getTotalEdges())

print(dijkstras(LL.nodes['2']))