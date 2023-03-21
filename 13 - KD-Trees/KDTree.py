#This script is an implementation of a Kd-tree, used to quickly search the point among a scatter plot closer to a given position .
#Reference : https://youtu.be/BK5x7IUTIyU

#A lot of things would be nicer if I had the dimension each point divides as an attribute of the Node it's in : no need to pass it down the recursive call.
#I might change the code to do that some day but I don't really have time for now, just ideas.

import matplotlib.pyplot as plt

class Point :
    def __init__(self, coordinates:tuple[float], dimensions=2) :
        #You can add stuff here for your own use for what you'll use the KD tree, this is the minimum needed.
        self.C = coordinates
        self.d = dimensions
    
    def __str__(self) :
        return str(self.C)
    
    def draw(self, col:str, mark:str, label="") :
        plt.scatter(self.C[0], self.C[1], c=col, marker=mark, label=label)
    
    def dist(self, point) :
        return sum([(self.C[i]-point.C[i])**2 for i in range(self.d)])**(1/2)


class Scatter :
    def __init__(self, name:str, dimensions=2) :
        self.name = name
        self.d = dimensions
        self.points = set()
        self.kdt = KdTree()

    def addPoint(self, point:Point) :
        if point.d == self.d :
            self.points.add(point)
        else :
            print("error : point is in the wrong dimension")
    
    def buildKDT(self) :
        if self.kdt.root is not None :
            self.kdt.clean()
        self.kdt.build(self)

    def draw(self) :
        plt.figure(self.name)
        for point in self.points :
            plt.scatter(point.C[0], point.C[1], c='b', marker='s')
    
    def closest(self, point:tuple[float]) :
        mindist = float('inf')
        point = Point(point, len(point))
        closePoint = None
        
        for p in self.points :
            dist = point.dist(p)
            if dist < mindist :
                closePoint = p
                mindist = dist
        return closePoint
    
    def closest_kdt(self, coords:tuple[float]) :
        #First call of a recursive function
        if self.kdt.root is not None :
            self.kdt.root.clean()
        start = self.kdt.root
        closestNode = self.kdt.root
        point = Point(coords, len(coords))
        closeNode, min_dist = self.search_down(point, start, 0, closestNode, point.dist(start.info))
        return closeNode, min_dist

    def search_down(self, point:Point, deeperNode, dim, closeNode, min_dist) :
        deeperNode.searched = True

        #Going down the tree :
        while deeperNode.hasChildren() :
            prev = deeperNode
            if point.C[dim] <= deeperNode.info.C[dim] and deeperNode.lowChild is not None :
                deeperNode = deeperNode.lowChild
            else :
                deeperNode = deeperNode.highChild

            dist = point.dist(deeperNode.info)
            deeperNode.searched = True
            if dist < min_dist :
                min_dist = dist
                closeNode = deeperNode
            
            dim = (dim+1)%self.d
        
        closeNode, min_dist = self.search_up(point, deeperNode, dim, closeNode, min_dist)
        return closeNode, min_dist
    
    def search_up(self, point:Point, deeperNode, dim, closeNode, min_dist):
        #Going up the tree :
        toCheck = deeperNode.p
        dim = (dim-1)%self.d
        while toCheck is not None :
            if abs(point.C[dim]-toCheck.info.C[dim]) < min_dist :
                #Check on the other side of the line if it's closer than the current minDist
                if toCheck.lowChild is not None and not toCheck.lowChild.searched :
                    closeNode, min_dist = self.search_down(point, toCheck.lowChild, (dim+1)%self.d, closeNode, min_dist)
                elif toCheck.highChild is not None and not toCheck.highChild.searched :
                    closeNode, min_dist = self.search_down(point, toCheck.highChild, (dim+1)%self.d, closeNode, min_dist)

            #Continue going up the tree
            toCheck = toCheck.p
            dim = (dim-1)%self.d
        return closeNode, min_dist


class Node :
    def __init__(self, point:Point) :
        self.info = point
        self.p = None
        self.lowChild = None
        self.highChild = None
        self.searched = False
    
    def __str__(self) :
        return f'{self.info} [{self.lowChild}, {self.highChild}]'
    
    def makeChildren(self, lower:list[Point], higher:list[Point], dim:int) :
        nextDim = (dim+1)%self.info.d

        if len(lower) != 0 :
            lowlower, lowMed, lowhigher = find_ith(lower, (len(lower)-1)//2, dim)
            self.lowChild = Node(lowMed)
            self.lowChild.p = self
            self.lowChild.makeChildren(lowlower, lowhigher, nextDim)

        if len(higher) != 0 :
            highlower, highMed, highhigher = find_ith(higher, (len(higher)-1)//2, dim)
            self.highChild = Node(highMed)
            self.highChild.p = self
            self.highChild.makeChildren(highlower, highhigher, nextDim)
    
    def hasChildren(self) :
        return (self.highChild is not None or self.lowChild is not None)
    
    def clean(self) :
        self.searched = False
        if self.lowChild is not None :
            self.lowChild.clean()
        if self.highChild is not None :
            self.highChild.clean()
    
    def delete(self) :
        if self.lowChild is not None :
            self.lowChild.delete()
            self.lowChild = None
        if self.highChild is not None :
            self.highChild.delete()
            self.highChild = None


class KdTree :
    def __init__(self) :
        self.root = None

    def __str__(self):
        return str(self.root)

    def build(self, scatter:Scatter) :
        #Build an optimal tree using a scatter, as described in the video linked line 2.
        points = list(scatter.points)
        lower, median, higher = find_ith(points, (len(points)-1)//2, 0)
        self.root = Node(median)
        self.root.makeChildren(lower, higher, 1%scatter.d)

#Recursive function used to build the KD tree.
def find_ith(points:list[Point], i, dim) -> tuple[list[Point], Point, list[Point]] :
    #Find which point is in the ith position on the dimension dim.
    #Returns the list on lower points, the searched point and the list of higher points.
    pivot = points[i]
    lower = []
    higher = []
    for point in points[:i]+points[i+1:] :
        if point.C[dim] <= pivot.C[dim] :
            lower.append(point)
        else :
            higher.append(point)
    if len(lower) < i :
        reclow, ith, rechigh = find_ith(higher, i-len(lower)-1, dim)
        return lower+[pivot]+reclow, ith, rechigh
    elif len(lower) == i :
        return lower, pivot, higher
    else :
        reclow, ith, rechigh = find_ith(lower, i, dim)
        return reclow, ith, rechigh+[pivot]+higher