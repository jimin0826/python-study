import sys

class STACK:
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
      return 'no'
    else:
      self.items.append(data)
      self.top += 1

  def pop(self):
    if(self.is_empty()):
      return 'no'
    else: 
      data = self.items[self.top]
      del(self.items[self.top])
      self.top -= 1
      return(data)


def main():
  while True:
    sentence = input()
    result = 'yes'
    stack = STACK()

    if (sentence == '.'):
      break
    for e in sentence:
      if (e == '('):
        stack.push('(')
      elif(e == ')'):
        if(stack.is_empty()):
          result = 'no'
        elif(stack.items[stack.top] == '['):
          result = 'no'
        else:
          stack.pop()
      elif (e == '['):
        stack.push('[')
      elif(e == ']'):
        if(stack.is_empty()):
          result = 'no'
        elif(stack.items[stack.top] == '('):
          result = 'no'
        else:
          stack.pop()

    if(stack.is_empty()):
      pass
    else:
      result = 'no'
    print(result)

main()