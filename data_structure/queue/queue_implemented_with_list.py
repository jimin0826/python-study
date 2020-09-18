class Queue:
	def __init__(self, capacity=100):
		self.q = []
		self.capacity = capacity
		self.front = 0
		self.rear = -1
		self.count = 0

	def size(self):
		return self.count

	def is_Full(self):
		return self.size() == self.capacity

	def is_Empty(self):
		return self.size() == 0

	def append(self, data):
		if(self.is_Full()):
			print("Queue is Full Now")
		else:
			self.q.append(data)
			self.count += 1

	def pop(self):
		if(self.is_Empty()):
			print("Queue is Empty Now")
		else:
			data = self.q[self.front]
			del(self.q[self.front])
			self.count -= 1
			return data

	def print_queue(self):
		if(self.is_Empty()):
			print("Empty Queue")
		else:
			print("Front : ", end = '')
			print(*self.q)

	def leave(self, k): # k번째 사람이 줄을 이탈
		if(self.size() < k):
			print("Invalid Input")
		else:
			self.q = self.q[self.front : k-1] + self.q[-(self.size())+k : ]