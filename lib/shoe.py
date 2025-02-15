class Shoe:
    def __init__(self, brand, size):
        '''Initializes the shoe with a brand and size.'''
        self.brand = brand
        self.size = size
        self.condition = "New"  # Default condition is "New"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):  # Ensure the size is an integer
            self._size = value
        else:
            print("size must be an integer")
            self._size = None  # This is optional, depending on how you'd want to handle invalid size.

    def cobble(self):
        '''Repairs the shoe and sets its condition to "New".'''
        print("Your shoe is as good as new!")
        self.condition = "New"
