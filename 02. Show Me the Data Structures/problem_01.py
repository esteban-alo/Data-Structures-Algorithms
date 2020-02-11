from collections import OrderedDict


class LRU_Cache(object):

	def __init__(self, capacity):
		# Initialize class variables
		self.cache = OrderedDict()
		self.capacity = capacity

	def get(self, key):
		# Retrieve item from provided key. Return -1 if nonexistent.
		try:
			value = self.cache.pop(key)
			self.cache[key] = value
			return value
		except KeyError:
			return -1

	def set(self, key, value):
		# Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.		
		if self.capacity == 0:
			print("Capacity must be greater than 0")
			return None
		try:
			self.cache.pop(key)
		except KeyError:		
			if len(self.cache) >= self.capacity:
				self.cache.popitem(last=False) # Removes oldest element in the dictionary
		# Assigning value to the key
		self.cache[key] = value

our_cache = LRU_Cache(5)
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);
our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache
our_cache.set(5, 5) 
our_cache.set(6, 6)
our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Test Cases
our_cache = LRU_Cache(3)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(2, 5)
our_cache.get(1)        # returns 1
our_cache.get(2)       # returns 5

our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(4, 3)
our_cache.set(3, 8)
our_cache.set(4, 6)
our_cache.get(3)        # returns 8
our_cache.get(6)       # returns -1

# Edge case
our_cache = LRU_Cache(0)
our_cache.set(1, 1)       # Capacity must be greater than 0
our_cache.get(1)       # returns -1