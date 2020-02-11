class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

	def __repr__(self):
		return str(self.value)


class LinkedList:
	def __init__(self):
		self.head = None

	def __str__(self):
		cur_head = self.head
		out_string = ""
		while cur_head:
			out_string += str(cur_head.value) + " -> "
			cur_head = cur_head.next
		return out_string


	def append(self, value):

		if self.head is None:
			self.head = Node(value)
			return

		node = self.head
		while node.next:
			node = node.next

		node.next = Node(value)

	def size(self):
		size = 0
		node = self.head
		while node:
			size += 1
			node = node.next
		return size
	
	def to_list(self):
		out = []
		node = self.head
		while node:
			out.append(node.value)
			node = node.next
		return out
		
	def search(self, value):
		node = self.head
		while node:
			if node.value == value:
				return True
			node = node.next
		return False

def union(llist_1, llist_2):
	# Your Solution Here
	linkedList = LinkedList()
	
	union_list = llist_1.to_list() + llist_2.to_list()
	
	for item in union_list:
		linkedList.append(item)
	
	return linkedList

def intersection(llist_1, llist_2):
	# Your Solution Here
	common_set = []
	tmp_list = []
	linked_list = LinkedList()
	
	current_node_ll1 = llist_1.head
	current_node_ll2 = llist_2.head
	
	while current_node_ll1:
		if llist_2.search(current_node_ll1.value) and current_node_ll1.value not in tmp_list:
			tmp_list.append(current_node_ll1.value)
			linked_list.append(current_node_ll1.value)
		current_node_ll1 = current_node_ll1.next
	
	return linked_list
	

# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
	linked_list_1.append(i)

for i in element_2:
	linked_list_2.append(i)

print(union(linked_list_1,linked_list_2))
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 21 -> 6 -> 32 -> 4 -> 9 -> 6 -> 1 -> 11 -> 21 -> 1 -> 
print(intersection(linked_list_1,linked_list_2))
# 4 -> 6 -> 21 -> 

# Test case 2
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
	linked_list_3.append(i)

for i in element_2:
	linked_list_4.append(i)

print(union(linked_list_3,linked_list_4))
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 1 -> 
print(intersection(linked_list_3,linked_list_4))
# 

# Edge Case
element_1 = []
element_2 = []
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

for i in element_1:
	linked_list_3.append(i)
	
for i in element_2:
	linked_list_4.append(i)
	
print(union(linked_list_3, linked_list_4))
#
print(intersection(linked_list_3,linked_list_4))
#

element_1 = []
element_2 = [14, 21, 39]
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

for i in element_1:
	linked_list_3.append(i)
	
for i in element_2:
	linked_list_4.append(i)
	
print(union(linked_list_3, linked_list_4))
#
print(intersection(linked_list_3,linked_list_4))
# 14 -> 21 -> 39 ->