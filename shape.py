
# The Shape class holds general data about a geometric shape.
class Shape:

  def __init__(self, name):
    self.__name = name

  def get_area(self):
    return 0.0

  def get_perimeter(self):
    return 0.0

  def get_name(self):
    return self._name

  def print_all(self):
    print('\nShape:', self.__name)
    print('\tArea:', self.get_area())
    print('\tPerimeter:', self.get_perimeter())
  
