"Implementation of binary search Tree for SDP"

class Node():
    def __init__(self, ticket):
        self.info = ticket
        self.ticketNum = ticket[0]
        self.priorityNum = int(ticket[1])
        self.left = None
        self.right = None
        self.parent = None
    
    def addleft(self, node):
        node.parent = self
        self.left = node
    
    def addright(self, node):
        node.parent = self
        self.right = node
        
    def Height(self, count = 0):
        if not self.parent:
            return count
        return self.parent.Height(count + 1)

class binarySearchTree():
    def __init__(self, data):
        self.root = Node(data[0])
        self.data = data[1:]
    
    def setElement(self, parent = None, index = 0):
        if parent is None:
            parent = self.root
        
        if index == len(self.data):
            return
        
        if self.data[index][1] < parent.priorityNum:
            if parent.left is None:
                parent.addleft(Node(self.data[index]))
                return self.setElement(index = index + 1)
            
            return self.setElement(parent.left, index)
        else:
            if parent.right is None:
                parent.addright(Node(self.data[index]))
                return self.setElement(index = index + 1)
                
            return self.setElement(parent.right, index)
        
    def displayTree(self, pos):
        if not pos:
            return
        spaces = " " * pos.Height() * 3 
        
        print(spaces + "|--" + str(pos.info))
        self.displayTree(pos.left)
        self.displayTree(pos.right)
    
    
    def descendingOrder(self, queue, pos = None):
        if not pos:
            return 
        
        self.descendingOrder(queue,pos.right)
        queue.enqueue(pos.info)
        self.descendingOrder(queue,pos.left)

"""def main():
    data = [(134,1),(135,2),(136,5),(137,9),(139,4),(140,3)]
    t = binarySearchTree(data)
    root = Node(data[0])
    t.root = root
    t.setElement()
    t.displayTree(root)
    t.descendingOrder(t.root)
main()"""
    

    
    
        
        