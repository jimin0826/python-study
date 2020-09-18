class Node:
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

class DoublyLinkedList:
	def __init__(self, head=None, tail=None):
		self.head = None # head = right head pointer
		self.tail = None # tail = left head pointer

	def insert_head(self, data):
		newNode = Node(data)
		if(self.head is None):
			self.head = newNode
			self.tail = newNode
		else:
			newNode.left = self.head
			self.head.right = newNode
			self.head = newNode	
	
	def insert_tail(self, data):
		newNode = Node(data)
		if(self.tail is None):
			self.head = newNode
			self.tail = newNode
		else:
			newNode.right = self.tail
			self.tail.left = newNode
			self.tail = newNode

	def delete_head(self):
		self.head = self.head.left
		self.head.right.left = None
		self.head.right = None

	def delete_tail(self):
		self.tail = sefl.tail.right
		self.tail.left.right = None
		self.tail.left = None

	def delete(self, data):
		cur = self.head
		prev = None
		isFound = False

		while(cur != None and isFound == False):
			if(cur.data == data):
				isFound = True
			else: 
				prev = cur
				cur = cur.left

		if(cur is None):
			print("Not Found")
		elif(cur == self.head):
			self.head = self.head.left
			self.head.right.left = None
			self.head.right = None
		elif(cur == self.tail):
			self.tail = sefl.tail.right
			self.tail.left.right = None
			self.tail.left = None
		else:
			cur.right.left = cur.left
			cur.left.right = cur.right
			cur.left = None
			cur.right = None
			
	def print_list(self):
		print("<- ", end = '')
		cur = self.tail
		while(cur is not None):
			if(cur.right is None):
				print(cur.data, end = '')
			else:
				print(cur.data, end = ' <-> ')
			cur = cur.right
		print(" ->")

class Deque:
  def __init__(self):
    self.deq = DoublyLinkedList()
    self.size = 0

  def size(self):
    return self.size

  def is_Empty(self):
    return self.size() == 0

  def enqueue_front(self, data):
    self.deq.insert_head(data)

  def enqueue_rear(self, data):
    self.deq.insert_tail(data)

  def dequeue_front(self):
    self.deq.delete_head()

  def dequeue_rear(self):
    self.deq.delete_tail()

  def print_dequeue(self):
    self.deq.print_list()

deq = Deque()
deq.enqueue_front(2)
deq.enqueue_front(3)
deq.enqueue_rear(5)
deq.print_dequeue()