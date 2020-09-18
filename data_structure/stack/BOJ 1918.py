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

stack = []


  for p in parenthesis:
    if(p == '('):
      stack.push(1)
    elif(p == ')'):
      if(stack.pop() == -1):
        result = "NO"
        break

  if(stack.is_empty() and len(result) == 0):
    result = "YES"
  else:
    result = "NO"

  print(result)

# pop 할 때 empty가 발생하면 => NO
# 다 끝난 이후에 empty => YES
# empty아니고 남아있으면 => NO