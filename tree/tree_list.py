class Binarytree:
    def __init__(self, size) -> None:
        self.custom_list = size * [None]
        self.last_index = 0
        self.max_size = size

    def insert_node(self, value):
        if self.last_index + 1 == self.max_size:
            return "Binary tree is full"
        self.custom_list[self.last_index + 1] = value
        self.last_index += 1
        return f"{value} is inserted"
    
    def search_node(self, value):
        for i in self.custom_list:
            if i == value:
                return "found element"
        return "Not found"
    
    def pre_order_traversal(self, index):
        if index > self.last_index:
            return
        print(self.custom_list[index])
        self.pre_order_traversal(index * 2)
        self.pre_order_traversal(index * 2 + 1)
    

    def post_order_traversal(self, index):
        if index > self.last_index:
            return
        self.pre_order_traversal(index * 2)
        self.pre_order_traversal(index * 2 + 1)
        print(self.custom_list[index])
        
        

    def in_order_traversal(self, index):
        if index > self.last_index:
            return
        self.pre_order_traversal(index * 2)
        print(self.custom_list[index])
        self.pre_order_traversal(index * 2 + 1)
        

    def level_order_traversal(self, index):
        for i in range(index, self.last_index+1):
            print(self.custom_list[i])

    def delete_node(self):
        self.custom_list = None
        self.last_index = 0


    def delete_single_node(self, value):
        if self.last_index == 0:
            return "no node to delete"
        for i in range(self.last_index+1):
            if self.custom_list[i] == value:
                self.custom_list[i] = self.custom_list[self.last_index]
                self.custom_list[self.last_index] =None
                self.last_index -= 1
                return "node deleted"
        return "node not found"
    

btree = Binarytree(8)
btree.insert_node("drinks")
btree.insert_node("hot")
btree.insert_node("cold")
btree.pre_order_traversal(1)
btree.in_order_traversal(1)
btree.post_order_traversal(1)
btree.level_order_traversal(1)
btree.delete_single_node("hot")
btree.delete_node()