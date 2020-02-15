def sort_012(input_list):
	"""
	Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

	Args:
	   input_list(list): List to be sorted
	"""
	index = 0
	mid_index = 0
	last_index = len(input_list) - 1
	
	if not input_list:
		return "Fail"

	while index <= last_index:
		if input_list[index] == 0:
			input_list[index] = input_list[mid_index]
			input_list[mid_index] = 0
			mid_index += 1
			index += 1

		elif input_list[index] == 2:
			temp_val = input_list[last_index]
			input_list[last_index] = 2
			input_list[index] = temp_val
			last_index -= 1

		else:
			index += 1

	return input_list
		
def test_function(test_case):
	sorted_array = sort_012(test_case)
	if sorted_array == sorted(test_case):
		print("Pass")
	else:
		print("Fail")

# Normal Cases
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]) # Pass
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]) # Pass
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]) # Pass

# Edge Cases
test_function([]) # Fail
test_function([1, 1]) # Pass
test_function([0]) # Pass