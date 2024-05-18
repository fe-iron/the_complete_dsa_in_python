from LinkedList import LinkedList

def intersection(llA, llB):
    if llA.tail is not llB.tail:
        return None
    
    shorter = llA if len(llA) < len(llB) else llB
    longer = llB if len(llA) < len(llB) else llB
    diff = len(longer) - len(shorter)
    shorter_node = shorter.head
    longer_node = longer.head
    for _ in range(diff):
        longer_node = longer_node.next

    while longer_node is not shorter_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    return longer_node

    