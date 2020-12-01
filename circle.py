import math

from terminal_colors import TerminalColors
from shape import Shape

# Class representing a Circle.
class Circle(Shape):

  def __init__(self, radius):
    Shape.__init__(self, 'Circle')
    self.__radius = radius

  def get_area(self):
    return math.pi * self.__radius * self.__radius

  def get_perimeter(self):
    return 2 * math.pi * self.__radius

  def get_radius(self):
    return self.__radius

  def print_all(self):
    Shape.print_all(self)
    print(TerminalColors.OKGREEN,'\tRadius: ', self.__radius, TerminalColors.ENDC)