"""
CONTROL FLOW:
1. start program
2. Read the file and store as a dictionary
3. make changes in the dictionary(append, update)
4. Write in file
5. End program
"""
                        # IMPORTS
import random as random
import csv
import HashTableImplementationV3 as HT
import BSTtickets as BST
import LinkedQueue as Q



                        # DATA 
# User - Dictionary {Username: Password}
"This dictionary will be built before the run time"
user = {"Shreyaa": "128", "Sindhuja": "129", "Singaram": "130", 
        "Sneha": "131", "Sneha Senthil": "132", "Sreekar": "133"}

# Agent - Dictionary {Username: (Password, category)}
"Building the Agent Dictionary as a ashTable"
agent = HT.hashTable(10)
agent["XYZ"] = (["XYZ", "electrical"])
agent["ABC"] = (["ABC", "plumbing"])
agent["DEF"] = (["DEF", "furniture"])


# FilePath - Dictionary {category: FilePath}
filePathDict = {"electrical": "C:\\Users\\sneha\\OneDrive - SSN Trust\\Electrical Tickets.csv",
            "furniture": "C:\\Users\\sneha\\OneDrive - SSN Trust\\Furniture Tickets.csv",
            "plumbing": "C:\\Users\\sneha\\OneDrive - SSN Trust\\Plumbing Tickets.csv"}

# Ticket - Dictionary {Category: [[TicketNum, UserName, Category, Issue, Status]]}
" Implement this as a class and maintain the value as a linked list"
ticketDict = {"electrical": [], "plumbing": [], "furniture": []}


# Ticket numbers - List
ticketNos = []
                        # CLASS DEFINITIONS:

# Class to create ticket objects
class ticketObj():
    """
    Data Memebers: self.userName, self.category, self.issue, self.status
    Memeber functions: print(), setStatus
    """
    def __init__(self, ticketNum, userName, category, issue, status = "Yet to be viewed", priority = 0):
        self.ticketNum = ticketNum
        self.userName = userName
        self.category = category
        self.issue = issue
        self.status = status
        self.priority = priority
        
    
    def __str__(self):
        content = "Ticket Number: {} \nUsername : {} \nCategory : {} \nIssue: {} \nStatus: {}". format(self.ticketNum, self.userName, self.category, self.issue, self.status)
        return content
    
    def setStatus(self, status):
        # Allows the agent to change the status of the ticket
        self.status = status
        return
    
    def getTicketNum(self):
        # Returns the ticket number of an object
        return self.ticketNum
    
    def returnAsList(self):
        # Return the information as a list
        # [Ticket number, username, category, issue, status,priority]
        return [self.ticketNum, self.userName, self.category, self.issue, "Yet to be viewed", self.priority]

                        # FUNCTIONS:
                        # COMMON FUNCTIONS:
def fileToDictionary():
    for category in ticketDict.keys():
        filePath = filePathDict[category]
        with open(filePath, "r") as file:
            ticketList = csv.reader(file,delimiter = "\t")
            for ticket in ticketList:
                if len(ticket)!= 0:
                    ticketDict[category].append(ticket[0].split(","))
       

def dictionaryToFile():
    for category in ticketDict.keys():
        filePath = filePathDict[category]
        ticketList = ticketDict[category]
        with open(filePath, "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerows(ticketList)
                        #USER FUNCTIONS:
# Function to generate a unique ticket number
def generateTicketNo():
    ticketNum = random.randint(100, 1000)
    if ticketNum in ticketNos:
        return generateTicketNo()
    ticketNos.append(str(ticketNum))
    return str(ticketNum)

# Function to raise ticket, take input and store in dictionary ticket
def raiseTicket(U):
    userName = U
    ticketNumber = generateTicketNo()
    print("Your ticket number is: ", ticketNumber)
     
    "Print the categories"
    category = input("Enter the category of issue: ").lower()
    issue = input("Briefly explain the issue: ")
     
    "Creating a ticket object: "
    ticket = ticketObj(ticketNumber, userName, category, issue)
    
    "Call a function to write the new ticket information in the file"
    updateTicketDictionary(ticket, category)
    return

# Function to update the generated ticket to the ticket dictionary:  
def updateTicketDictionary(obj, category):
    if category not in ticketDict:
        print("Invalid Category")
        return
    ticketDict[category].append(obj.returnAsList())
    return

# Function to view status
def viewStatus(category, ticketNumber):
    ticketList = ticketDict[category]
    for ticket in ticketList:
        if ticket[0] == ticketNumber:
            content = "Ticket Number: {} \nUsername : {} \nCategory : {} \nIssue: {} \nStatus: {}". format(ticket[0], ticket[1], ticket[2], ticket[3], ticket[4])
            print(content)
            return
    print("Invalid Ticket Number")
    return

def RemindAgain(category, ticketNumber):
    ticketList = ticketDict[category]
    for ticket in ticketList:
        if ticket[0] == ticketNumber:
            priorityNum = int(ticket[-1])
            priorityNum += 1
            ticket[-1] = str(priorityNum)
            return
    print("Invalid Ticket Number")

def userFucntion(userName):
    print("UserName and Password verified")
    
    while(True):
        # Now user can either raise a ticket or view ticket status
        
        print("\n Welcome {}! What would you like to do?".format(userName))
        print("Enter 1 for raising a ticket")
        print("Enter 2 to view ticket status")
        print("Enter 3 to remind again")
        print("Enter Q to quit to login page")
        
        menu = input("Enter: ")
        if menu == "1":
            print("Raise Ticket")
            raiseTicket(userName)
        
        elif menu == "2":
            print("View status")
            ticketNumber = input("Enter the ticket number: ")
            C = input("Enter category: ").lower()
            if C not in ticketDict:
                print("Invalid Category")
                return userFucntion(userName)
            viewStatus(C, ticketNumber)
        
        elif menu == "3":
            print("Remind Again")
            ticketNumber = input("Enter the ticket number: ")
            C = input("Enter category: ").lower()
            if C not in ticketDict:
                print("Invalid Category")
                return userFucntion(userName)
            RemindAgain(C, ticketNumber)
            
        
        elif menu == "Q":
            return
        
        else:
            print("Invalid Entry")
                                
                            # AGENT FUNCTIONS
# Fucntion that prints all the tickets in that category           
def viewTickets(category):
    ticketList = ticketDict[category]
    pendingTickets , priorityQueue = prioritizeTickets(ticketList)
    while not priorityQueue.isEmpty():
        ticket = pendingTickets[priorityQueue.dequeue()]
        content = "Ticket Number: {} \nUsername : {} \nCategory : {} \nIssue: {} \nStatus: {} \nPriority: {} ". format(ticket[0], ticket[1], ticket[2], ticket[3], ticket[4], ticket[-1])
        print(content,"\n")
    return

def prioritizeTickets(ticketList):
    pendingTickets = {(ticket[0], int(ticket[-1])): ticket for ticket in ticketList if ticket[4] != "completed"}
    q1 = Q.Queue()
    tickets = list(pendingTickets.keys())
    t = BST.binarySearchTree(tickets)
    t.root = BST.Node(tickets[0])
    t.setElement()
    #t.displayTree(t.root)
    t.descendingOrder(q1,t.root)
    return (pendingTickets, q1)
       
def changeStatus(ticketNumber, category):
    ticketList = ticketDict[category]
    for ticket in ticketList:
        if ticket[0] == ticketNumber:
            status = input("Enter new status: ").lower()
            ticket[-1] = status
            return
    print("invalid Ticket Number")
    return

def agentFunction(userName):
    print("UserName and Password verified")
    
    while(True):
        # Now agent can either view all the tickets or change the status
        
        print("\n Welcome {}! What would you like to do?".format(userName))
        print("Enter 1 for viewing all the tickets")
        print("Enter 2 to change the status")
        print("Enter Q to quit to login page")
        
        # Find the category and file path which is common to all functions
        category = agent[userName][1]
        
        menu = input("Enter: ")
        if menu == "1":
            print("\nRaised Tickets: ")
            # Call function viewTickets
            viewTickets(category)
    
        
        elif menu == "2":
            print("Change Status")
            ticketNumber = input("Enter the ticket number: ")
            # call function changeStatus
            changeStatus(ticketNumber , category)
    
        elif menu == "Q":
            return
        
        else:
            print("Invalid Entry")
    
def main():
    fileToDictionary()
    while(True):
        print("Welcome to SSN IT HelpDesk login page")
        print("To exit application enter Exit")
        signIn = input("Sign in(User/Agent): ")
       
        if signIn == "User":
                                                  # USER
            print("Signed in as user")
            userName = input("Enter username: ")
            password = input("Enter password: ")
            
            # Check if username is in the authorized list of users and if the password is correct
            if (userName in user) and (user[userName] == password):
               userFucntion(userName)
            else:
                print("Acess Denied. Invalid Username or Password")
        
        elif signIn == "Agent":
                                                    # AGENT
            print("\nSigned in as Agent\n")
            userName = input("Enter username: ")
            password = input("Enter password: ")
            
            # checks if the username is in the authorized list of agents and if the password in correct
            if (userName in agent) and (agent[userName][0] == password):
                agentFunction(userName)
            else:
                print("Acess Denied. Invalid Username or Password")
        
        elif signIn == "Exit":
            print("Thank you")
            break
        
        else:
            print("Invalid Entry")
        
    dictionaryToFile()
main()           