def sqrt(number):
	"""
	Calculate the floored square root of a number

	Args:
	   number(int): Number to find the floored squared root
	Returns:
	   int: Floored Square Root
	"""
	bottom = 0
	top = number
	
	if number == None:
		return None
	
	if number == 0 or number == 1:
		return number
		
	while bottom <= top:
		mid = (bottom + top) // 2
		mid_pow = mid * mid
		if mid_pow == number or mid_pow <= number < (mid + 1) ** 2:
			return mid
		elif mid ** 2 > number:
			top = mid
		else:
			bottom = mid

# Normal Cases
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

# Edge Case
print ("Pass" if  (4129 == sqrt(67190)) else "Fail") # Fail
print ("Pass" if  (4129 == sqrt(None)) else "Fail") # Fail
print ("Pass" if  (0 == sqrt(None)) else "Fail") # Fail