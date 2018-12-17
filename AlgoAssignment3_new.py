
#@author: Helena J Arpudaraj

import numpy as np
import matplotlib.pyplot as plt
import random
import time
    
class Node(object):
    def __init__(self, name):
        self.name=name;
        self.adjacentnode=[];
        self.numOfEdges=0;
        self.visited=False;
        self.visited1=False;
        self.dist=0;
        self.Dist=[];
        

def start():
    global i;
    global totaldegree;
    i=1;
    nodeList.append(Node(i));
    i=i+1;
    nodeList[0].adjacentnode.append(nodeList[0]);
    nodeList[0].numOfEdges=1;
    totaldegree=1;
    BProb.append(1);
    
def Birthnode(NodeSelect):
    global i;
    global totaldegree;
    node1=Node(i);
    nodeList.append(node1);
    node1.adjacentnode.append(NodeSelect);
    node1.numOfEdges=1;        
    NodeSelect.adjacentnode.append(node1);
    NodeSelect.numOfEdges=(NodeSelect.numOfEdges)+1; 
    i=i+1;
    totaldegree=totaldegree+2;    
    numOfNodes=len(nodeList);
    for k in range (len(nodeList)):
        BProb.append((nodeList[k].numOfEdges)/(totaldegree));
    
def CumulativeProb():
    Cumulative_BirthProb=0;
    for k in range (len(nodeList)):
        Cumulative_BirthProb=Cumulative_BirthProb+BProb[k];
        CumulativeBProb.append(Cumulative_BirthProb);
    y=random.randint(0, 10);
    y=y/10;
    for k in range (len(CumulativeBProb)):
        if CumulativeBProb[k]>=y:
            node=nodeList[k];
            return node;
        if k==(len(CumulativeBProb)-1):
            return nodeList[k];
        
def FindAllPathsUtil(startNode, endNode, path, Dist1, dist): 
        startNode.visited1= True;
        path.append(startNode); 
  
        if startNode == endNode:
            Dist1.append(dist); 
        else: 
            dist=dist+1;
            for i in startNode.adjacentnode: 
                if i.visited1==False: 
                    FindAllPathsUtil(i, endNode, path, Dist1, dist) 
                      
        path.pop(); 
        startNode.visited1= False;
        return Dist1;
    
def bruteforce(startNode, endNode): 
    Dist1=[];    
    dist=0;
    shortestlength=0;
    numOfShortestPaths=0;
    
    for n in nodeList:
        n.visited1 = False;
  
    path = []; 
  
    Dist1 = FindAllPathsUtil(startNode, endNode, path, Dist1, dist); 
    shortestlength=min(Dist1);
    numOfShortestPaths=Dist1.count(shortestlength);
    return numOfShortestPaths;
                
    

def bfs(startNode,endNode):
    queue=[];
    queue.append(startNode);
    shortestlength=0;
    numOfShortestPaths=0;
    count=0;
    for node1 in nodeList:
        node1.visited= False;
        node1.dist=0;
        node1.Dist=[];
    startNode.Dist.append(0);    
    startNode.visited=True;
    while queue:
        actualNode=queue.pop(0);
        for n in actualNode.adjacentnode:
            n.dist=actualNode.dist+1;
            n.Dist.append(n.dist);
            count=actualNode.Dist.count(actualNode.dist)
            if count>1:
                for k in range (2,count+1):
                    n.Dist.append(n.dist);
            
            if not n.visited:
                n.visited = True;
                queue.append(n);
                
            if n.dist>0:
                n.dist=min(n.Dist);
 
    shortestlength=min(endNode.Dist)
    numOfShortestPaths=endNode.Dist.count(shortestlength);
    print("shortest length from node ",nodeList.index(startNode)," to ",nodeList.index(endNode)," = ",shortestlength);
    return numOfShortestPaths;
                    
                

nodeList=[];
BProb=[];


# testing correctness using bfs and brute force for random network of 10 nodes
    
nodeList=[];
BProb=[];
numNodes=0;
numEdges=0;
totaldegree=0;
start();

for k in range (1,10):
    CumulativeBProb=[];
    NodeSelected=CumulativeProb();
    BProb=[];
    Birthnode(NodeSelected);
nodeList[0].adjacentnode.remove(nodeList[0]); 

for k in range (1,5):
    v=random.randint(0, 9);
    w=random.randint(0,9);
    if (v!=w) and (nodeList[w] not in nodeList[v].adjacentnode ):
        nodeList[v].adjacentnode.append(nodeList[w]);
        nodeList[w].adjacentnode.append(nodeList[v]);    


for j in range (0,10):
    print("The list of adjacent nodes to node ",j," is ");
    for n in nodeList[j].adjacentnode:
        print("Node ",nodeList.index(n));

# testing correctness using bfs force method for random network of 10 nodes

print("Validation for correctness for nodes 0-9 using bfs");    
v=0;
for w in range (1,10):    
    no_shortestPaths=bfs(nodeList[v],nodeList[w]);
    print("Number of shortest paths from node ",v," to node ",w," is: ",no_shortestPaths);


# testing correctness using brute force method for random network of 10 nodes

print("Validation for correctness for nodes 0-9 using brute force");    
v=0;
for w in range (1,10):    
    no_shortestPaths=bruteforce(nodeList[v],nodeList[w]);
    print("Number of shortest paths from node ",v," to node ",w," is: ",no_shortestPaths);
    

#Validation of performance
    
print("Validation for performance");    

numNodesEdgesList=[];
TimeComplexity=[];
a=[1,3000,6000,9000]     
for j in a:
    nodeList=[];
    BProb=[];
    numNodes=0;
    numEdges=0;
    totaldegree=0;
    start();

    for k in range (1,j+1):
        CumulativeBProb=[];
        NodeSelected=CumulativeProb(); 
        BProb=[];
        Birthnode(NodeSelected);
    
    nodeList[0].adjacentnode.remove(nodeList[0]); 
  #removing starting node's edge to itself  
    start_time=time.time();
    no_shortestPaths=bfs(nodeList[0],nodeList[j]);
    Timetaken=(time.time()) - start_time;
    TimeComplexity.append(Timetaken);
    numNodes=len(nodeList);
    numEdges=(totaldegree-1);
     #-1 in total degree is for removing starting node's edge to itself    
    numNodesEdgesList.append(numNodes+numEdges);

plt.plot(numNodesEdgesList,TimeComplexity)
plt.ylabel('Time Taken')
plt.xlabel('num of nodes + num of Edges (n+m)')
plt.title('Validation for performance')
plt.show()


