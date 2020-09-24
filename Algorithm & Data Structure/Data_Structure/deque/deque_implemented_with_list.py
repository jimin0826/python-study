class Deque:
  def __init__(self, capacity=100):
    self.deq = []
    self.capacity = capacity
    self.front = 0
    self.rear = -1
    self.count = 0

  def isFull(self):
    return self.size() == self.capacity

  def isEmpty(self):
    return self.size() == 0

  def size(self):
    return self.count

  def insertFront(self, data):
    if(self.isFull()):
      print("Deque is Full Now")
    else:
      self.deq = [data] + self.deq
      self.count += 1
      self.rear += 1

  def insertRear(self, data):
    if(self.isFull()):
      print("Deque is Full Now")
    else: 
      self.deq.append(data)
      self.count += 1
      self.rear += 1

  def deleteFront(self):
    if(self.isEmpty()):
      print("None")
    else:
      self.deq = self.deq[1: ]
      self.count -= 1
      self.rear -= 1

  def deleteRear(self):
    if(self.isEmpty()):
      print("None")
    else:
      self.deq = self.deq[0: self.size-1]
      self.count -= 1
      self.rear -= 1

  def getFront(self):
    if self.isEmpty():
      return None
    else:
      return self.deq[self.front]

  def getRear(self):
    if(self.isEmpty()):
      return None
    else:
      return self.deq[self.rear]

  def print_dequeu(self):
    print(*self.deq)


deque = Deque()
deque.insertFront(3)
deque.insertFront(5)
deque.insertRear(9)
deque.print_dequeu()