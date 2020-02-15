def rotated_array_search(input_list, number):
	"""
	Find the index by searching in a rotated sorted array

	Args:
	   input_list(array), number(int): Input array to search and the target
	Returns:
	   int: Index or -1
	"""
	try:
		len_input_list = len(input_list)  # length of list
		start_index = 0
		end_index = len_input_list
		pivot = 0
		
		while start_index <= end_index:
			pivot = (start_index + end_index) // 2
			if input_list[0] < input_list[len_input_list - 1] or pivot == len_input_list - 1:
				pivot = 0
				break
			if input_list[pivot - 1] > input_list[pivot]:
				break
			elif input_list[0] < input_list[pivot]:
				start_index = pivot
			elif input_list[0] > input_list[pivot]:
				end_index = pivot
		if input_list[pivot] <= number <= input_list[len_input_list - 1]:
			start_index = pivot
			end_index = len_input_list
		else:
			start_index = 0
			end_index = pivot
			
		while start_index <= end_index:
			pivot = (start_index + end_index) // 2
			if input_list[pivot] == number:
				return pivot
			elif input_list[pivot] < number:
				start_index = pivot + 1
			else:
				end_index = pivot - 1
		return -1
	except:
		return 0

def linear_search(input_list, number):
	for index, element in enumerate(input_list):
		if element == number:
			return index
	return -1

def test_function(test_case):
	input_list = test_case[0]
	number = test_case[1]
	if linear_search(input_list, number) == rotated_array_search(input_list, number):
		print("Pass")
	else:
		print("Fail")

# Normal Cases
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6]) # Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1]) # Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8]) # Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1]) # Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10]) # Pass

# Edge Case
test_function([[None], 1]) # Pass
test_function([[2], 10]) # Pass
test_function([[], None]) # Fail