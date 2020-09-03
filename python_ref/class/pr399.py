import sys
import math

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y 

  def sety(self, y):
    self.y = y

  def move(self, dx, dy):
    self.x += dx
    self.y += dy

  def info(self):
    print("({}, {})".format(self.x, self.y))

  def distance(self, p):
    result = (self.x - p.x)**2 + (self.y - p.y)**2
    result = math.sqrt(result)
    print("{:.3}".format(result))

def dist(p1, p2):
  result = (p1.x - p2.x)**2 + (p1.y - p2.y)**2
  result = math.sqrt(result)
  print("{:.3}".format(result))


p1 = Point(3, 5)
p2 = Point(6, 9)
dist(p1, p2)
p1.distance(p2)