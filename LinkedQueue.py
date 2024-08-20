# Linked Queue Implementation
class Node():
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class Queue():
    def __init__(self):
        self.head = self.end = Node()
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
    
    def enqueue(self, item):
        pos = self.end
        pos.next = Node(item, pos.next)
        self.end = self.end.next
        self.size += 1
        return
    
    def dequeue(self):
        pos = self.head
        item = pos.next.item
        pos.next = pos.next.next
        self.size -= 1
        return item
        
    def display(self):
        pos = self.head
        while pos.next is not None:
            print(pos.next.item, end = "-")
            pos = pos.next
        return
    
# Driver Code
"""def main():
    q1 = Queue()
    q1.enqueue("Python")
    q1.enqueue("Java")
    q1.enqueue("C")
    q1.enqueue("Ruby")
    q1.enqueue("Swift")
    print("After Enqueue: ")
    q1.display()
    print()
    
    q1.dequeue()
    q1.display()
    print()
    q1.dequeue()
    q1.display()
    print()
    q1.dequeue()
    q1.display()
    print()
    q1.dequeue()
    q1.display()
    print()
    q1.dequeue()
    print("After Dequeue: ")
    q1.display()

main()"""
