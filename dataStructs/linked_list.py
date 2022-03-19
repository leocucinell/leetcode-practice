class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
    
    def __str__(self):
        return str(self.val)

class LinkedList: 
    def __init__(self):
        self.head = None

    def __str__(self):
        current_node = self.head
        if(current_node == None):
            return "Linked list empty"
        
        while current_node:
            print(current_node)
            current_node = current_node.next
        return "END"