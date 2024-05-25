class Tree:
    def __init__(self, data, children=[]) -> None:
        self.data = data
        self.children = children

    def __str__(self, level=0) -> str:
        ret = " " * 5 * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    
    def add_child(self, treeNode):
        self.children.append(treeNode)


tree = Tree("drinks", [])
hot = Tree("hot", [])
cold = Tree("cold", [])
tree.add_child(hot)
tree.add_child(cold)

chai = Tree("chai", [])
coffee = Tree("coffee", [])
hot.add_child(chai)
cold.add_child(coffee)

print(tree)