from shape import Shape
from terminal_colors import TerminalColors

# Class representing a Rectangle.
class Rectangle(Shape):

  def __init__(self, base, height):
    Shape.__init__(self, 'Rectangle')
    self.__base = base
    self.__height = height

  def get_area(self):
    return self.__base * self.__height

  def get_perimeter(self):
    return 2 * self.__base + 2 * self.__height

  def get_base(self):
    return self.__base

  def get_height(self):
    return self.__height

  def print_all(self):
    Shape.print_all(self)
    print(TerminalColors.WARNING, '\tbase: ', self.__base)
    print('\theight: ', self.__height, TerminalColors.ENDC)

# Class representing a Square (Rectangle with same base and height).
class Square(Rectangle):

  def __init__(self, side_length):
    Rectangle.__init__(self, side_length,  side_length)
    self.__side_length = side_length
    # Override the name given by the parent.
    self._Shape__name = 'Square'

  def get_side_length(self):
    return self.__side_length

  def print_all(self):
    # Note that we are skipping the Rectangle overload and executing 
    # Shape's directly:
    Shape.print_all(self)
    #Rectangle.print_all(self)
    print(TerminalColors.FAIL,'\tside: ', self.__side_length, TerminalColors.ENDC)