# HashTable Implementation

class HashNode:
  def __init__(self, key, value):
    self.next = None
    self.key = key
    self.value = value

class HashTable:
  def __init__(self):
    self.table = [None] * 101

  def hash(self, key):
    hashed = 0
    for i in range(len(key)):
      hashed = (256 * hashed + ord(key[i])) % 101
    return hashed

  def add(self, key, value):
    bucket = self.hash(key)
    if not self.table[bucket]:
      self.table[bucket] = HashNode(key, value)
    else:
      temp = self.table[bucket]
      while(temp.next):
        temp = temp.next
        temp.next = HashNode(key, value)

  def find(self, key):
    bucket = self.hash(key)
    if(not self.table[bucket]):
      return False
    else:
      temp = self.table[bucket]
      while temp:
        if temp.key == key:
          return temp.value
        temp = temp.next
      return False

  def delete(self, key):
    bucket = self.hash(key)
    if(not self.table[bucket]):
      return False
    else:
      if self.table[bucket].key == key:
        self.table[bucket] = None
      else:
        temp = self.table[bucket]
        while(temp):
          if(temp.next.key == key):
            temp.next = temp.next.next
            return
          temp = temp.next
        return False