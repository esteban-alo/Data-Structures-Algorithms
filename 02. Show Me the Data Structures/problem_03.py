import heapq
import os
import sys

class Node:
	def __init__(self, char, freq):
		self.char = char
		self.freq = freq
		self.left = None
		self.right = None

	def __lt__(self, value):
		return self.freq < value.freq
			
	def __gt__(self, value):
		return self.freq > value.freq

	def __eq__(self, value):
		if(value == None):
			return False
		if(not isinstance(value, Node)):
			return False
		return self.freq == value.freq

class HuffmanCoding:
	def __init__(self):
		self.heap = []
		self.coded_chars_dict = {}

	def get_char_frequency(self, text):
		frequency = {}
		for character in text:
			if not character in frequency:
				frequency[character] = 0
			frequency[character] += 1
		return frequency

	def create_heap_nodes(self, frequency):
		for key in frequency:
			node = Node(key, frequency[key])
			heapq.heappush(self.heap, node)
	
	def create_heap_tree(self):
		while len(self.heap) > 1:
			node1 = heapq.heappop(self.heap)
			node2 = heapq.heappop(self.heap)
			merged = Node(None, node1.freq + node2.freq)
			merged.left = node1
			merged.right = node2
			heapq.heappush(self.heap, merged)
			
	def set_heap_codes(self):
			root = heapq.heappop(self.heap)
			current_code = ""
			self.create_encoded_dict(root, current_code)
			
	def create_encoded_dict(self, root, current_code):
		if(root == None):
			return

		if(root.char != None):
			self.coded_chars_dict[root.char] = current_code
			return
			
		self.create_encoded_dict(root.left, current_code + "0")
		self.create_encoded_dict(root.right, current_code + "1")
		
	

	def get_encoded_text(self, text):
		encoded_text = ""
		for character in text:
			encoded_text += self.coded_chars_dict[character]
			
		return encoded_text, self.coded_chars_dict
		

def huffman_encoding(text, huffman_coding):
	if text == "":
			return "0", None
		
	frequency_char_dict = huffman_coding.get_char_frequency(text)
	huffman_coding.create_heap_nodes(frequency_char_dict)
	huffman_coding.create_heap_tree()
	huffman_coding.set_heap_codes()
	encoded_text, encoded_dict = huffman_coding.get_encoded_text(text)	
	return encoded_text, encoded_dict 

def huffman_decoding(encoded_data, encoded_dict):
	current_char = ""
	decoded_text = ""
	decoded_char_dict = {}	
	
	
	try:
		if len(encoded_dict) == 1:
			key = next(iter(encoded_dict.keys()))
			decoded_char_dict['0'] = key
		
		else :	
			for key, value in encoded_dict.items():
				decoded_char_dict[value] = key
			
		for bit in encoded_data:
			current_char += bit
			if(current_char in decoded_char_dict):
				character = decoded_char_dict[current_char]
				decoded_text += character
				current_char = ""
	except:
		if encoded_dict is None:
			return
	return decoded_text

if __name__ == "__main__":
	huffman_coding = HuffmanCoding()
	a_great_sentence = "The bird is the word"
	print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
	print("The content of the data is: {}\n".format(a_great_sentence))
	encoded_data, tree = huffman_encoding(a_great_sentence, huffman_coding)
	print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
	print("The content of the encoded data is: {}\n".format(encoded_data))
	decoded_data = huffman_decoding(encoded_data, tree)
	print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
	print("The content of the encoded data is: {}\n".format(decoded_data))	
	print("\n")
	
	a_great_sentence = ""
	huffman_coding = HuffmanCoding()
	print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
	print("The content of the data is: {}\n".format(a_great_sentence))
	encoded_data, tree = huffman_encoding(a_great_sentence, huffman_coding)
	print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
	print("The content of the encoded data is: {}\n".format(encoded_data))
	decoded_data = huffman_decoding(encoded_data, tree)
	print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
	print("The content of the encoded data is: {}\n".format(decoded_data))
	print("\n")
	
	a_great_sentence = "AA"
	huffman_coding = HuffmanCoding()
	print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
	print("The content of the data is: {}\n".format(a_great_sentence))
	encoded_data, tree = huffman_encoding(a_great_sentence, huffman_coding)
	if len(encoded_data) == 0 :
		encoded_data = "0" * len(a_great_sentence)
	print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
	print("The content of the encoded data is: {}\n".format(encoded_data))
	decoded_data = huffman_decoding(encoded_data, tree)
	print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
	print("The content of the encoded data is: {}\n".format(decoded_data))
	