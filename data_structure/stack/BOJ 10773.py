import sys

class Stack:
  def __init__(self, max_length=100):
    self.items = []
    self.top = -1
    self.max_length = max_length

  def size(self):
    return self.top + 1

  def is_empty(self):
    return self.top == -1

  def is_full(self):
    return self.top == self.max_length - 1

  def push(self, data):
    if(self.is_full()):
      print("Stack is Full")
    else:
      self.items.append(data)
      self.top += 1

  def pop(self):
    if(self.is_empty()):
      return -1
    else:
      data = self.items[self.top]
      del(self.items[self.top])
      self.top -= 1
      return data

def main():
	stack = Stack(100000)
	N = int(sys.stdin.readline())
	for _ in range(N):
		num = int(sys.stdin.readline())
		if(num == 0):
			stack.pop()
		else:
			stack.push(num)
	
	sum = 0
	n = stack.size()
	for i in range(n):
		sum += stack.items[i]
	print(sum)