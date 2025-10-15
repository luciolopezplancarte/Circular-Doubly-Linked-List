#Lucio Plancarte

class Item:

    def __init__(self, description):
        """
        Constructor for Item class. It initializes with
        the description of an item.
        PARAMETERS:
        ---------------
            description: String. Description of an item
        """
        self._description = description
        

    def get_description(self):
        """
        Method that returns the description of an item.
        The method returns a String.
        """
        return self._description

