"Implementing Binary Search Tree to show the Tickets in descending Order"
ticketList = [['501', 'Sneha', 'electrical', 'captain america', 'Yet to be viewed', '1'], ['502', 'Sneha', 'electrical', 'Iron Man', 'pending', '3'], ['503', 'Sneha', 'electrical', 'Thanos', 'completed', '2'], ['504', 'Sneha', 'electrical', 'Thor', 'pending', '4'], ['505', 'Sneha', 'electrical', 'spiderman', 'completed', '0'], ['506', 'Sneha', 'electrical', 'captain marvel', 'pending', '3'], ['507', 'Sneha', 'electrical', 'Hulk', 'pending', '1']]

"""
1. Create a new dictionary of tickets which are not complted 
   [(ticketNum, PriorityNum)] = [Ticket(as a list)]
2. Using dict.keys() access the keys and make it as a list
    [(TN1, PN1), (TN2, PN2)]
3. Insert the tuples in a BST 
4. Retreieve the tuples in a descending order
    4.a Enqueue the tickets in the Queue
5. Dequeue the Queue and print the tickets
"""
""""Step1:Create a new dictionary of tickets which are not complted
    [(ticketNum, PriorityNum)] = [Ticket(as a list)]
"""
pendingTickets = {(ticket[0], int(ticket[-1])): ticket for ticket in ticketList if ticket[4] != "completed"}

#print(pendingTickets)

"Step 2: Insert each key in a BST"
import BSTtickets as BST
import LinkedQueue as Q

def main():
    q1 = Q.Queue()
    tickets = list(pendingTickets.keys())
    t = BST.binarySearchTree(tickets)
    t.root = BST.Node(tickets[0])
    t.setElement()
    #t.displayTree(t.root)
    t.descendingOrder(q1,t.root)
    
    #q1.display()
    # Print the Tickets:
    while not q1.isEmpty():
        print(pendingTickets[q1.dequeue()])
        
        
main()


