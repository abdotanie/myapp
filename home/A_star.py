cityes=[]
heuristics={}
# Add a connect from A and B in arry
def add(c1,d2,f3): 
  r=[c1,d2,int(f3)]  
  cityes.append(r)
  print(cityes)
# Add a string line   
def addHeuristics(c,n):
    heuristics[c]=int(n)
class Graph:
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.undirected()
    # Add a link from A and B of given distance, and also add the inverse link if the graph is undirected
    def connections(self, A, B, d=1):
        self.graph_dict.setdefault(A, {})[B] = d
        if not self.directed:
            self.graph_dict.setdefault(B, {})[A] = d
    # Get neighbors or a neighbor
    def get(self, a, x=None):
        link = self.graph_dict.setdefault(a, {})
        if x is None:
            return link
        else:
            return link.get(x)
    # Create an undirected graph by adding symmetric edges
    def undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.graph_dict.setdefault(b, {})[a] = dist        
    # Return a list of nodes in the graph
    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)
class Node:
    # Initialize the class
    def __init__(self, name:str, parent:str):
        self.name = name
        self.parent = parent
        self.s = 0 # Distance to start node
        self.h = 0 # Distance to goal node
        self.f = 0 # Total cost
    # Compare nodes
    def __eq__(self, other):
        return self.name == other.name
    # Sort nodes
    def __lt__(self, other):
         return self.f < other.f
    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.name, self.f))
# A* search
def astar_search(graph, heuristics, start, end):
    # Create lists for open nodes and closed nodes
    open,close = [],[]
    # start node and an end node
    start_node = Node(start, None)
    end_node = Node(end, None)
    # Add the start node
    open.append(start_node)
    # Loop until the open list is empty
    while len(open) > 0:
        # Sort the open list to get the node with the lowest cost first
        open.sort()
        # Get the node with the lowest cost
        current_node = open.pop(0)
        # Add the current node to the close list
        close.append(current_node)
        # Check if we have reached the end, return the path
        if current_node == end_node:
            path = []
            while current_node != start_node:
                path.append(current_node.name)
                current_node = current_node.parent
            path.append(start_node.name )
            # Return reversed path
            return path[::-1]
        neighbors = graph.get(current_node.name)
        # Loop neighbors
        for key in neighbors.items():
            # Create a neighbor node
            neighbor = Node(key, current_node)
            # Check if the neighbor is in the closed list
            if(neighbor in close):
                continue
            # Calculate full path cost
            neighbor.s = current_node.s + graph.get(current_node.name, neighbor.name)
            neighbor.h = heuristics.get(neighbor.name)
            neighbor.f = neighbor.s + neighbor.h
            # Check if neighbor is in open list and if it has a lower f value
            if(cheak_neighbor(open, neighbor) == True):
                # Everything is green, add neighbor to open list
                open.append(neighbor)
    # Return None, no path is found
    return None
def cheak_neighbor(open, neighbor):
# Check if a neighbor should be added to open list    
    for node in open:
        if (neighbor == node and neighbor.f > node.f):
            return False
    return True
def main(start,end):
    graph=Graph()
    for g in cityes:
        graph.connections(g[0],g[1],g[2])
    # Make graph undirected, create symmetric connection
    graph.undirected()
    pp= astar_search(graph, heuristics, start, end)
    path=''
    for p in pp:
        path =path +' -> '+p
    print(path)
    return path

