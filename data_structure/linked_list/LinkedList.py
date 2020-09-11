
class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self, head=None):
    self.head = None

  def insert(self, data):
    print("insert", data)
    newNode = Node(data)
    if(self.head == None):
      self.head = newNode
    else:
      newNode.next = self.head
      self.head = newNode

  def delete(self, data):
    print("delete", data)
    cur = self.head
    prev = None
    isFound = False

    while(cur != None and isFound == False):
      if(cur.data == data):
        isFound = True
      else:
        prev = cur
        cur = cur.next

    if(cur is None):
      print("not found")
    elif(cur == self.head):
      self.head = self.head.next
      cur.next = None
    else:
      prev.next = cur.next
      cur.next = None

  def print_linked_list(self):
    cur = self.head
    while(cur is not None):
      print(cur.data, end = '->')
      cur = cur.next
    print('None')

LinkedList = LinkedList()
LinkedList.insert(3)