class Node:

    def __init__(self, initial_data):
        """
        Constructor for the class. 
        It initializes a node with the recieved data and the pointers
        for the previous and next nodes
        """
        self.data = initial_data
        self.next = None
        self.prev = None
