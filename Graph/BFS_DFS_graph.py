class Graph:
    def __init__(self, gdict=None) -> None:
        if not gdict:
            gdict = {}
        self.gdict = gdict

    def add_vertex_with_edge(self, vertex, edge):
        if vertex not in self.gdict.keys():
            self.gdict[vertex] = [edge]
        else:
            self.gdict[vertex].append(edge)
    def add_vertex(self, vertex):
        if vertex not in self.gdict.keys():
            self.gdict[vertex] = []
            return True
        return False

    def print_graph(self):
        for vertex in self.gdict:
            print(vertex, " : ", self.gdict[vertex])

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            self.gdict[vertex1].append(vertex2)
            self.gdict[vertex2].append(vertex1)
            return True
        return False

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            self.gdict[vertex1].remove(vertex2)
            self.gdict[vertex2].remove(vertex1)
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.gdict.keys():
            for vert in self.gdict.keys():
                if vertex in self.gdict[vert]:
                    self.gdict[vert].remove(vertex)
            del self.gdict[vertex]
            return True
        return False
    
    def bfs_traversal(self, vertex):
        visited = set()
        visited.add(vertex)
        queue = [vertex]
        while queue:
            curr_vertex = queue.pop(0)
            for item in self.gdict[curr_vertex]:
                if item not in visited:
                    visited.add(item)
                    queue.append(item)
        return visited
                
    def dfs_traversal(self, vertex):
        visited = set()
        stack = [vertex]
        while stack:
            curr_vertex = stack.pop()
            if curr_vertex not in visited:
                print(curr_vertex)
                visited.add(curr_vertex)
            for item in self.gdict[curr_vertex]:
                if item not in visited:
                    stack.append(item)

cust_dict = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "E"],
    "D": ["B", "E", "F"],
    "E": ["D", "F", "C"],
    "F": ["D", "E"] 
}

graph = Graph(cust_dict)
graph.add_vertex_with_edge("Z", "A")
graph.add_edge("Z", "A")
graph.print_graph()
graph.bfs_traversal("A")
graph.dfs_traversal("A")