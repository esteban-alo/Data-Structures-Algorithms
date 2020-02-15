def rearrange_digits(input_list):
	"""
	Rearrange Array Elements so as to form two number such that their sum is maximum.

	Args:
	   input_list(list): Input List
	Returns:
	   (int),(int): Two maximum sums
	"""

	input_len = len(input_list)
	input_freq = [0] * 10
	pivot = 1
	merge_opt1 = []
	merge_opt2 = []
	
	if input_len == 0 or input_len == 1:
		return [-1, -1]
		
	if input_len % 2 != 0:
		pivot = 2
		
	for num in input_list:
		input_freq[num] += 1
		
	for item in range((len(input_freq) - 1), -1, -1):
		while input_freq[item]:
			if pivot:
				merge_opt1.append(str(item))
				pivot -= 1
			else:
				pivot += 1
				merge_opt2.append(str(item))
			input_freq[item] -= 1
	return [int(''.join(merge_opt1)), int(''.join(merge_opt2))]

def test_function(test_case):
	output = rearrange_digits(test_case[0])
	solution = test_case[1]
	if sum(output) == sum(solution):
		print("Pass")
	else:
		print("Fail")

# Normal Cases
test_function([[1, 2, 3, 4, 5], [542, 31]]) # Pass
test_function([[4, 6, 2, 5, 9, 8], [964, 852]]) # Pass
test_function([[1, 2, 3], [31, 2]]) # Pass

# Edge Cases
test_function([[0, 1, 2, 5, 6, 7], [752, 167]]) # Fail
test_function([[1,  9, 1], [10, 1]]) # Fail
test_function([[], []]) # Fail