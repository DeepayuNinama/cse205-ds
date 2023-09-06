#Node class is to initialize node ( eg:[1|None] )

class  Node:
    def __init__(self,data):

        #This will create a node [1|None]->[2|None]->[3|None]-> and so on

        self.data = data
        self.next = None

#Linked List is to create linked list of our data (eg: Train coach)

class LinkedList:
    def __init__(self):
        self.head = None  #This will point the first node

    def print_LL(self):
        if self.head is None:   #This will check if our LL is empty or not
            print("Linked List is Empty")

        else:
            n = self.head   #Giving a smaller name to self.head

            #Running the while loop till we reach null value of n.next -> Null

            while n is not None:    
                print(n.data)
                n=n.next

    # Adding Node at the BEGINING
    # S1: Create new Node
    # S2: Link New Node to First Node 
    # S3: Link head to new node

    def add_begining(self,data): 
        new_node = Node(data) # S1
        new_node.next = self.head #S2
        self.head = new_node #S3

    # Adding Node at the END
    # S1: Create new Node
    # S2: Run a while loop to reach last node 
    # S3: Append Newly created Node to head (Pointer)

    def add_end(self,data):
        new_node = Node(data) #S1

        #Check whether list is empty or not
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                #Incrementing n (moving one step tracking the node)
                n = n.next
            n.next = new_node    




LL1 = LinkedList()

# Adding at the begining
LL1.add_begining(9)
LL1.add_begining(8)

# Adding at the END
LL1.add_end(10)
LL1.print_LL()         