class CDLL:

    def __init__(self):
        """
        Constructor for the clas. It initialized the head, tail and size.
        For an empty CDLL, the head and tail are None.
        """
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """
        Method to return the length of the list
        """
        return self._size

    def isEmpty(self):
        """
        Method to check if the list is empty
        The method returns True or False
        """

    def _find_node_by_value(self,value):
        """
        Private helper method to find a node by its data value.
        If the list is empty or if the node is not in the list it returns None
        Otherwise, it searches for the first node with the given value and it
        returns the node.
        PARAMETERS:
        -----------
            value: any. The value to search in the list
        
        """

    def reverse(self):
        """
        Method to reverse the order of the list
        If the list is empty or with only one element, it just return
        """

    def append(self, data):
        """
        Method to append a new node to the end of the list.
        The method recieves the data for the new node
        It checks if the list is empty and inserts the node accordingly
        The method updates the size of the list
        *Important*: Maintain circular links. New head's previous points to tail,
                     tail's next points to new head.
        PARAMETERS:
        -----------
            data: The data to store in the list

        """

    def prepend(self, data):
        """
        Method to prepend a new node at the front of the list
        The method recieves the data for the new node
        It checks if the list is empty and insters the node accordignly
        THe method updates the size of the list
        *Important*: Maintain circular links. New head's previous points to tail,
                     tail's next points to new head.
        PARAMETERS:
        ------------
            data: The data to store in the list

        """

    def insert_after(self, exisiting_value, data):
        """
        Method to insert node after another node.
        The method recieves a value for an exisiting node and the data to insert for the new node
        The method needs to insert the new node after the node with the given value
        The method updates the size of the list
        The method needs to check if the list is empty and stores the node accordingly
        The method needs to check if the current node is the last nde, the it can use append().
        Keep in mind the size of the list.
        The method uses the _find_node_by_value() helper method to check if there is a node witht the current_value in the list.
        If the node does not exist, the method shows the message:
            "Node with value _____ not found. Cannot insert after."
            And returns.
        Note: Inserting after the tail, its equivalent to append.
        PARAMETERS:
        ------------
            exisiting_value: any. The data of the node after which to insert
            data: The data for the new node to be inserted

        """

    def insert_befor(self, exisiting_value, data):
        """
        Method to insert node before another node
        The method recieves a value for an exisiting node and the data to insert as the new node
        The method needs to insert the new node before the node with the given value
        The method updates the size of the list
        The method needs to check if the list is empty and stores the node accordingly
        The method needs to check if the current node is the first node, the it can use prepend().
        Keep in mind the size of the list.
        The method uses the _find_node_by_value() helper method to check if there is a node witht the current_value in the list.
        If the node does not exist, the method shows the message:
            "Node with value _____ not found. Cannot insert before."
            And returns.
        Note: Inserting before the head, its equivalent to prepend.
        PARAMETERS:
        ------------
            exisiting_value: any. The data of the node before which to insert
            data: The data for the new node to be inserted

        """

    def remove(self, value_to_remove):
        """
        Method to remove a node with a given data value from list
        The method updates the sizeo fht elist
        If the list is empty it just returns
        If the list has just one element, it empties the list and assigns the head and tail accordingly and returns
        The method uses the _find_node_by_value() helper method.
        If no node is found the method shows the message:
            "Node with value _____ nt found. Cannot remove" and returns
        If the node to remove is the head or tail node, the method updates their links.
        The method reduces the size of the list.
        Note: Update head/tail if value_to_remove was the head or tail
        PARAMETERS:
        ___________
            value_to_remove: any The data value of the node to be removed

        """

    def remove_by_index(self,index):
        """
        Method to remove a node by its 'index'
        It checks if the list is empty. If it is is it prints the message:
            "List is empty. Cannot remove by index." and returns
        Print a message if the index is out of bounds:
            "Index to remove out of bounds". and returns
        It uses the remove() method to avoid duplicating cases.
        PARAMETERS:
        ------------
            index: int. The 'index' (position) of the node to remove

        """

    def remove_before(self, value):
        """
        Method to remove a node before another node
        The method recieves the value for a node. It uses the _find_node_by_value() helper to find the ndoe to use for removing the node before it.
        It chekcs if the list is empty or if it has only one element.
        If it does, it just returns
        If there is no node with the given value it shows the message:
            "Node with value ____ not  found. Cannot remove before." and returns
        As this is a circular list, if the current node is the head, then the node to remove is the tail.
        It uses the remove() method to avoid duplicating cases.
        The method updates the size of the list
        PARAMETERS:
        ------------
            current_node: any. The data of the current node

        """

    def remove_after(self, value):
        """
        Method to remove a node after another node
        The method recieves the value for a node. It uses the _find_node_by_value() helper to find the ndoe to use for removing the node after it.
        It chekcs if the list is empty or if it has only one element.
        If it does, it just returns
        If there is no node with the given value it shows the message:
            "Node with value ____ not  found. Cannot remove after." and returns
        As this is a circular list, if the current node is the tail;, then the node to remove is the head.
        It uses the remove() method to avoid duplicating cases.
        The method updates the size of the list
        PARAMETERS:
        ------------
            current_node: any. The data of the current node

        """

    def search(self, value):
        """
        Method to search for a node witha particular value
        It is different that the helper method because this method returnst he POSITION( i.e, index) of the nodes starting with 0
        Otherwise, it returns -1
        If the list is empty, it returns -1
        PARAMETERS:
        -----------
        value: any. The data of the node to find.

        """

    def __str__(self):
        """
        Method to show the content of the list
        This method returns a String with the representation of the list
        For example, [1 2 3 4]
        """



