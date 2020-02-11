# Libraries
import hashlib
import datetime

	
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

	def __repr__(self):
		return str(self.value)


class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def append(self, timestamp, data):
		if self.head is None:
			self.head = Node(Block(timestamp, data, 0))	
			self.tail = self.head
			return
		node = self.tail
		self.tail.next = Node(Block(timestamp, data, 0))
		self.tail.previous_hash = node
		return
		
class Block:
	def __init__(self, timestamp, data, previous_hash):
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.calc_hash()
		
	def calc_hash(self):
		sha = hashlib.sha256()
		# hash_str = "We are going to encode this string of data!".encode('utf-8')
		hash_str = "{} \n {} \n {}".format(self.timestamp, self.data, self.previous_hash).encode('utf-8')
		sha.update(hash_str)
		return sha.hexdigest()
		
def get_timestamp():
	return datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")

# Test
block_zero = Block(get_timestamp(), "Test data block zero", 0)
block_one = Block(get_timestamp(), "Test data block one", block_zero)
block_two = Block(get_timestamp(), "Test data block two", block_one)
print("Block Zero data : ", block_zero.data)
print("Block Zero hash : ", block_zero.hash)
print("Block Zero timestamp : ", block_zero.timestamp)
linked_list = LinkedList()
linked_list.append(get_timestamp(), "Information A")
linked_list.append(get_timestamp(), "Information B")
print("Block one's previous block's data : ", block_one.previous_hash.data)
print("Linked list last data : ", linked_list.tail.next.value.data)
print("Linked list last's previous hash data : ", linked_list.tail.previous_hash.value.data) 

print("\n")

# Edge Case
block_zero = Block(get_timestamp(), "", 0)
block_one = Block(get_timestamp(), "Test data block one", block_zero)
block_two = Block(get_timestamp(), "Test data block two", block_one)
print("Block Zero data : ", block_zero.data)
print("Block Zero hash : ", block_zero.hash)
print("Block Zero timestamp : ", block_zero.timestamp)
linked_list = LinkedList()
linked_list.append(get_timestamp(), "")
linked_list.append(get_timestamp(), "")
print("Block one's previous block's data : ", block_one.previous_hash.data)
print("Linked list last data : ", linked_list.tail.next.value.data)
print("Linked list last's previous hash data : ", linked_list.tail.previous_hash.value.data)