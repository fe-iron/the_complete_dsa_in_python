class Graph:
    def __init__(self, vertices) -> None:
        self.v = vertices
        self.graph = []
        self.node = []

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    def add_node(self, value):
        self.node.append(value)

    def print_sol(self, dist):
        print("Distance from source")
        for key, item in dist.items():
            print(" ",key," : ",item)

    def belllman_ford(self, source):
        dist = {i: float("Inf") for i in self.node}
        dist[source] = 0
        for _ in range(self.v-1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph having negative cycle")
                return
        self.print_sol(dist)



graph = Graph(5)
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")
graph.add_edge("A", "C", 6)
graph.add_edge("A", "D", 6)
graph.add_edge("B", "A", 3)
graph.add_edge("C", "D", 1)
graph.add_edge("D", "C", 2)
graph.add_edge("D", "B", 1)
graph.add_edge("E", "B", 4)
graph.add_edge("E", "D", 2)
graph.belllman_ford("E")


