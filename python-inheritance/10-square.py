#usr/bin/python3
#class square inherits from Rectangle (9-rectangle.py)
Rectangle=__import__('9-rectangle.py').Rectangle


class square (Rectangle):
    """
    Represantation of square
    
    """
    def __init__(self,size):
        """

        initialize a new 'square'
        args:
        size(int):size of new square
        """
        self.integer_validator("size",size)
        self.__size = size
