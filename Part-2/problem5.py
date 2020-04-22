import random
import heapq

class NewNode():
    def __init__(self, val: int) -> None:
        self.val=val
        self.neighbors=dict()

    def __str__(self) -> str:
        neighs=self.neighbors
        res=""
        for node in neighs:
            res+=node.val+":"+str(self.neighbors[node])+","
        res=res[:-1]
        return "Val: "+self.val +", Neighbors:"+"["+res+"]"

class WeightedGraph():
    def __init__(self):
        self.nodes=[]

    def __str__(self) -> str:
        printable=dict()
        for node in self.nodes:
            temp=[]
            for neighbor in node.neighbors:
                temp.append(neighbor.val+"|"+str(node.neighbors[neighbor]))
            printable[node.val]=temp
        return str(printable)
    
    def getPointer(self, searchNode: str) -> object:
        for node in self.nodes:
            if node.val==searchNode:
                return node

    def addNode(self, nodeVal: str) -> None:
        self.nodes.append(NewNode(nodeVal))
        
    def addWeightedEdge(self, first: NewNode, second: NewNode, edgeWeight: int) -> None:
        if second not in first.neighbors:
            first.neighbors[second]=edgeWeight
    
    def removeWeightedEdge(self, first: NewNode, second: NewNode, edgeWeight: int) -> None:
        if second in first.neighbors:
            first.neighbors[second]=edgeWeight

    def getTotalEdges(self) -> int:
        count=0
        for node in self.nodes:
            count+=len(node.neighbors)
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
    nodes=dict()
    visited,queue=[],[]
    heapq.heapify(queue)

    visited.append(start.val)
    paths[start.val]=0

    for neighbor in start.neighbors:
        weight=start.neighbors[neighbor]
        nodes[neighbor.val]=neighbor
        heapq.heappush(queue,(weight,neighbor.val))
        paths[neighbor.val]=min(paths.get(neighbor.val,float('inf')),weight)
    
    while queue:
        currNode=nodes[heapq.heappop(queue)[1]]
        if currNode.val not in visited:
            for neighbor in currNode.neighbors:
                weight=currNode.neighbors[neighbor]+paths[currNode.val]
                nodes[neighbor.val]=neighbor
                heapq.heappush(queue,(weight,neighbor.val))
                paths[neighbor.val]=min(paths.get(neighbor.val,float('inf')),weight)
                visited.append(currNode.val)

    return paths


print("Key: node|weight")

rand=createRandomCompleteWeightedGraph(4)
print(rand)

print("Starting at 0:")
print(dijkstras(rand.nodes[0]))
#LL=createALinkedList(10)
#print(LL)
#print("Total edges:",LL.getTotalEdges())

#print(dijkstras(LL.nodes[0]))
