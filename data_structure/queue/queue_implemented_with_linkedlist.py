class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self, head=None):
		self.head = None

	def insert(self, data):
		newNode = Node(data)
		if(self.head == None):
			self.head = newNode
		else:
			newNode.next = self.head
			self.head = newNode

	def pop(self):
		if(self.head == None):
			return
		else:
			cur = self.head
			while(cur.next.next != None):
				cur = cur.next
			cur.next = None

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
			print("Not Found")
		elif(cur == self.head):
			self.head = self.head.next
			cur.next = None
		else:
			prev.next = cur.next
			cur.next = None 

	def print_linked_list(self):
		cur = self.head
		print('Last : ', end = '')
		while(cur is not None):
			print(cur.data, end = ' ')
			cur = cur.next
		print(': Front')

class Queue:
  def __init__(self):
    self.q = LinkedList()
    self.size = 0

  def size(self):
    return self.size

  def is_Empty(self):
    return self.size() == 0

  def enqueue(self, data):
    self.q.insert(data)

  def dequeue(self):
    self.q.pop()

  def print_queue(self):
    self.q.print_linked_list()

q = Queue()
q.enqueue(3)
q.enqueue(5)
q.print_queue()