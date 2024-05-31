class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end_of_string = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for ch in word:
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.end_of_string = True
        print("successfully inserted")

    def search(self, word):
        current = self.root
        for ch in word:
            node = current.children.get(ch)
            if not node:
                return False
            current = node
        if not current.end_of_string:
            return False
        return True
    
def delete(root, word, index):
    ch = word[index]
    current_node = root.children.get(ch)
    can_this_be_deleted = False
    if len(current_node.children) > 1:
        delete(current_node, word, index+1)
        return False
    if index == len(word) - 1:
        if len(current_node.children) >= 1:
            current_node.end_of_string = False
            return False
        else:
            root.children.pop(ch)
            return True
    if current_node.end_of_string == True:
        delete(current_node, word, index+1)
        return False
    can_this_be_deleted = delete(current_node, word, index+1)
    if can_this_be_deleted == True:
        root.children.pop(ch)
        return True
    return False


trie = Trie()
trie.insert("API")
trie.insert("APPI")
trie.search("AP")
trie.search("API")
delete(trie.root, "API", 0)