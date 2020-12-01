import math

from shape import Shape
from terminal_colors import TerminalColors

# Class representing an Equilateral Triangle (all 3 sides are equal).
class EquilateralTriangle(Shape):

  def __init__(self, side_length):
    Shape.__init__(self, 'Equilateral Triangle')
    self.__side_length = side_length

  def get_area(self):
    return self.__side_length * self.__side_length * (math.sqrt(3) / 4)

  def get_perimeter(self):
    return 3 * self.__side_length

  def get_side_length(self):
    return self.__side_length

  def print_all(self):
    Shape.print_all(self)
    print(TerminalColors.OKBLUE, '\tside: ', self.__side_length, TerminalColors.ENDC)

# Class representing an Isoceles Triangle (2 sides are equal)
class IsocelesTriangle(Shape):

  def __init__(self, base, height):
    Shape.__init__(self, 'Isoceles Triangle')
    self.__base = base
    self.__height = height

  def get_area(self):
    return self.__base * self.__height / 2

  def get_perimeter(self):
    # It is actually more complicated... Need to calculate the length of the equal sides by trigonometry.
    return self.__base + 2 * self.__height

  def get_base(self):
    return self.__base

  def get_height(self):
    return self.__height

  def print_all(self):
    Shape.print_all(self)
    print(TerminalColors.OKBLUE, '\tbase: ', self.__base)
    print('\theight: ', self.__height, TerminalColors.ENDC)
