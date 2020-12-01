import circle
import triangle
import rectangle

def main():
  s1 = circle.Circle(10)
  s2 = rectangle.Rectangle(10, 5)
  s3 = rectangle.Square(5)

  triangles = [
    triangle.IsocelesTriangle(10, 10),
    triangle.EquilateralTriangle(5)
  ]

  shapes = [s1,s2,s3] + triangles
  for s in shapes:
    s.print_all()

# Call the main function.
main()
