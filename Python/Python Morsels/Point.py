class Point:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
  def __repr__(self):
    return f'Point(x={self.x}, y={self.y}, z={self.z})'
  def __eq__(self, other):
    if self.x == other.x and self.y == other.y and self.z == other.z:
      return True
    else:
      return False
  def __add__(self, other):
    return Point(self.x + other.x, self.y + other.y, self.z + other.z)
  def __sub__(self, other):
    return Point(self.x - other.x, self.y - other.y, self.z - other.z)
  def __mul__(self, value):
    return Point(self.x * value, self.y * value, self.z * value)
  def __rmul__(self, value):
    return self * value
  def __iter__(self):
    yield self.x
    yield self.y
    yield self.z

if __name__ == '__main__':
  p1 = Point(1, 2, 3)
  p2 = Point(1, 2, 3)