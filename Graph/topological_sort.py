from collections import defaultdict

class TopologicalSort:
    def __init__(self, no_of_vertices) -> None:
        self.graph = defaultdict(list)
        self.no_of_vertices = no_of_vertices

    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topology_sort_util(self, v, visited, stack):
        visited.append(v)

        for i in self.graph[v]:
            if i not in visited:
                self.topology_sort_util(i, visited, stack)

        stack.insert(0, v)

    def topology_sort(self):
        visited = []
        stack = []
        for i in list(self.graph):
            if i not in visited:
                self.topology_sort_util(i, visited, stack)

        print(stack)


customGraph = TopologicalSort(8)
customGraph.add_edge("A", "C")
customGraph.add_edge("C", "E")
customGraph.add_edge("E", "H")
customGraph.add_edge("E", "F")
customGraph.add_edge("F", "G")
customGraph.add_edge("B", "D")
customGraph.add_edge("B", "C")
customGraph.add_edge("D", "F")

customGraph.topology_sort()

