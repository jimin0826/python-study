import sys

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
			return None
		else:
			self.q.append(data)
			self.count += 1

	def pop(self):
		if(self.is_Empty()):
			return -1
		else:
			data = self.q[self.front]
			del(self.q[self.front])
			self.count -= 1
			return data

	def print_queue(self):
		if(self.is_Empty()):
			return None
		else:
			print("Front : ", end = '')
			print(*self.q)

	def leave(self, k): # k번째 사람이 줄을 이탈
		if(self.size() < k):
			return None
		else:
			self.q = self.q[self.front : k-1] + self.q[-(self.size())+k : ]

n = int(sys.stdin.readline())
q = Queue()
for _ in range(n):
  a = sys.stdin.readline().split()

  if len(a) == 2:
    q.append(int(a[1]))
  else:
    if a[0] == 'pop':
      print(q.pop())
    elif a[0] == 'size':
      print(q.size())
    elif a[0] == 'empty':
      if q.is_Empty():
        print(1)
      else:
        print(0)
    elif a[0] == 'front':
      if q.is_Empty():
        print(-1)
      else:
        print(q.q[q.front])
    else:
      if q.is_Empty():
        print(-1)
      else:
        print(q.q[q.rear])
