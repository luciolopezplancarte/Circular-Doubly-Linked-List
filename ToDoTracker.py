#Lucio Plancarte

from Item import Item
from CDLinkedList import CDLL

class ToDo(CDLL):

    def add_item(self, description):
        """
        Method that appends a new Item object to the ToDo list
        PARAMETERS:
        -------------
        description: String. The Item's description
        """

    def search(self,description):
        """
        Method that searches for an item given its description
        This method OVERRIDES the search method from the parent class
        It returns the item's position or -1.
        PARAMETERS:
        ------------
        name: String. The item's name
        """

    def remove(self,description):
        """
        Method that removes an item from the Todo list.
        This method OVERRIDES the remove method from the CDLL
        If the ToDo list is empty, just returns
        If the item is not in the ToDo list it presents a message to the user
        "Item with description ____ not found" and it returns
        Otherwise it removes the item
        PARAMETERS:
        ------------
        name: String. The Item's name
        """

    def __str__(self):
        """
        Method that shows the content of the ToDo list.
        It OVERRIDES the parent's method.
        If the list is empty it shows "No items in the ToDO list.
        Otherwise, it presents the items in the ToDo list, one item per row
        """




