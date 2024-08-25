import heapq

class Edge:
    def __init__(self, weight, start_v, target_v) -> None:
        self.weight = weight
        self.start_vertex = start_v
        self.target_vertex = target_v

class Node:
    def __init__(self, name) -> None:
        self.name = name
        self.visited = False
        self.predecessor = None
        self.neighbors = []
        self.min_distance = float("inf")

    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance
    
    def add_edge(self, weight, destination_vertex):
        edge = Edge(weight, self, destination_vertex)
        self.neighbors.append(edge)


class Djikstra:
    def __init__(self) -> None:
        self.heap = []

    def calculate(self, start_vertex):
        start_vertex.min_distance = 0
        heapq.heappush(self.heap, start_vertex)
        while self.heap:
            actual_vertex = heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue
            for edge in actual_vertex.neighbors:
                start = edge.start_vertex
                target = edge.target_vertex
                new_distance = start.min_distance + edge.weight
                if new_distance < target.min_distance:
                    target.min_distance = new_distance
                    target.predecessor = start
                    heapq.heappush(self.heap, target)
            actual_vertex.visited = True
    
    def get_shortest_path(self, vertex):
        print(f"the shortest path to vertex {vertex.name} is {vertex.min_distance}")
        actual_vertex = vertex
        while actual_vertex is not None:
            print(actual_vertex.name, end=" ")
            actual_vertex = actual_vertex.predecessor
        print()


# creating nodes
node_A = Node("A")
node_B = Node("B")
node_C = Node("C")
node_D = Node("D")
node_E = Node("E")
node_F = Node("F")
node_G = Node("G")
node_H = Node("H")


# creating edge

node_A.add_edge(6, node_B)
node_A.add_edge(10, node_C)
node_A.add_edge(9, node_D)

node_B.add_edge(5, node_D)
node_B.add_edge(16, node_E)
node_B.add_edge(13, node_F)

node_C.add_edge(6, node_D)
node_C.add_edge(5, node_H)
node_C.add_edge(21, node_G)

node_D.add_edge(8, node_F)
node_D.add_edge(7, node_H)

node_E.add_edge(10, node_G)

node_F.add_edge(4, node_E)
node_F.add_edge(12, node_G)

node_H.add_edge(2, node_F)
node_H.add_edge(14, node_G)

djikstra = Djikstra()
djikstra.calculate(node_A)
djikstra.get_shortest_path(node_F)


