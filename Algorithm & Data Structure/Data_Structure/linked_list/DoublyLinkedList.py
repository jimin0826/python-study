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
		print("<-", end = '')
		cur = self.tail
		while(cur is not None):
			if(cur.right is None):
				print(cur.data, end = '')
			else:
				print(cur.data, end = '<->')
			cur = cur.right
		print("->")

DoublyLinkedList = DoublyLinkedList()
DoublyLinkedList.insert_head(1)
DoublyLinkedList.insert_head(2)
DoublyLinkedList.insert_head(3)
DoublyLinkedList.insert_head(4)
DoublyLinkedList.insert_tail(1)
DoublyLinkedList.delete(4)
DoublyLinkedList.insert_tail(10)
DoublyLinkedList.insert_head(6)
DoublyLinkedList.print_list()