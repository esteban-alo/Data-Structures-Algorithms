# Project Explanation

## Project 1
For the LRU Cache problem, I decided a dictionary as the cache. The concept that I tried to apply in this excercise is the Queue Data Structure. Where the most oldest value in the dictionary (First Value) is removed when the dictionary capacity is full. The LRU_Cache class has two methods get and set where:
* get(): Retrieves item from provided key using the pop method if the key does not exit in the dictionary return -1
* set(): Set  a new value in the dictionary. If the capacity of the dictionary is out of space removes the oldest item and set the new value.

### Time and Space complexity
* Time complexity for methoDs set() and get() is O(1) is beacuse it takes a constant time perfoming the operations. 
* The Space complexity of the LRU Cache is O(n) because it depends the number of the dataset that would be provided to the dictionary (n) in this case when the size of the cache is full

## Project 2
For the File Recursion problem, I used a recursive method `find_files`. In this method I decied to add it an extra parameter called "found_files". With this parameter I save all the files founded on every folder iteration.


### Time and Space complexity
* Time complexity for this algorithm is O(n) where n is the depth of of folders in this case the iterations that the algorithm has to search.
* Space complexiy is O(n) this us because the memory space that would be used depends on the number of times that `find_files` has to be called will consume memory space 

## Project 3
For the Huffman Encoding problem, I decided to use de heapq library wich is a data structure wich provides an ordered tree of a list of elements. In this case a list of char items. To resolve this excercise I divide this problem in different classes. 
- Node(object):
	# Features
	- Char property: where the character item will be saved, 
	- Frequency property: number of times that character appears in the string.
	- Left, Right property: where stores new Nodes objects depending their weight in the tree.
	# "Magic Methods"
	- lt, gt, cmp: compares the elements that will be added to the heap list and set the order depending on a comparation of the char frecuency with the length of the string
	
- HuffmanCoding(object):
	#Features
	- heap: list
	- coded_chars_dict: dictionary of character and coded value
	# Methods
	- get_char_frequency: counts the number of times that a character is on the string. It returns a a key, value dictionary where key is the letter and the value is the number of times that is on the string.
	- create_heap_nodes: receives a dictionary from the get_char_frecuency function and creates a group of nodes that are added to the heap list.
	- create_heap_tree: iteration where merge the nodes and create a tree based on the weight of each tree
	- set_heap_codes: recursive method that evaluates each node and set them a value depending the position (0 or 1) and save each value on the coded_chars_dict dictionary
	- get_encoded_text: iterates over the original text and search each letter on the coded_chars_dict to get de coded value and create a coded string. Returns the coded string and the coded_chars_dict

- huffman_encoding(function): call all methods of HuffManCoding object
- huffman_decoding(functions): gets the coded_chars_dict and creates an inversed dictionary from to iterate it and create a decoded string


### Time and Space complexity
- Time complexity for this  is O(n log n) the main reason for this notation is based on number of the weight. Additonally Heapq is binary heap, with O(log n) for push() and pop() operation. In the excercise we have some extra operations that turns into a O(n log n)
- The _space complexity_, it is directly related to the of the iteration in the alphabet and the validations required to set the coding for each letter and the decoding process, resulting in O(nlogn).


## Project 4
For Active Directory excercise, I used recursive method `is_user_in_group` to check if the user is group's name or user is users group.

### Time and Space complexity
* Time complexity for this problem it's similar than Project 2, where the number calls of the search method depends on the depth of the group list and the user. Based in this arguement  we can define this the space complexity O(n * m),
* The space complexity of this problem due the number of validations same as the problem 02 ("Find files") depends on the number of calls that `is_user_in_group` will be called O(n) but the validations to check if the user is in the group or not turns this algorithm to O(n^2)

## Project 5
For the Block chain problem, I used a Doubly Linked List based on the explanations of the course this excercise require a back step to get the value of the prevous hash.
The main method for this excercise is the "append" method, where is used to add new nodes to the double LinkedlIst

### Time and Space complexity
* Time complexity is defined by the linked list append operation which is an O(1) which adds a new node item to the list
* The space complexity is O(n) where n is the number of nodes that the LinkedList will have

## Project 6
For the Union and Intersection problem, in the Linkedlist object I add a "to_list" and "search" methods. Which helps me get all the items of the LinkedList, create new LinkedList. The transformation of the Linked List to list takes an O(n) time complexity.


### Time and Space complexity
* For union function goes through each list element by element O(n) and appends the element O(1) in a new Linked List, so time xomplexity can be defined in this function as 0(n). The space complexity depends in the lenght of the provided LinkedList and every call to `to_list` function
* The intersect goes through one list element by element, O(n) and searches for it in the second list and also in the intersect list before it adds it - worst case O(n^2) for each search where is a validation nested in a loop. Same as the union the function the space complexity due the number of validations doing in the iteration loop to avoid repeated elements in the resulting list makes that this algorithm could be an O(n^2)