def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    try:
        if len(ints) == 0:
            return None

        max_value = - float("inf")
        min_value = float("inf")

        for int in ints:
            if int > max_value:
                max_value = int
            if int < min_value:
                min_value = int

        return (min_value, max_value)
    except:
        return None

## Example Test Case of Ten Integers
import random

# Normal Cases
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")  # Pass
print("Pass" if ((0, 9) == get_min_max([0])) else "Fail")  # Fail
print("Pass" if ((0, 0) == get_min_max([0])) else "Fail")  # Pass
print("Pass" if (None is get_min_max([])) else "Fail")  # Pass

# Edge Cases
l = [i for i in range(-10, 10)]  # a list containing 0 - 9
random.shuffle(l)
print("Pass" if (None == get_min_max(1)) else "Pass")  # Pass
print("Pass" if ((-11, 9) == get_min_max([0])) else "Fail")  # Fail
print("Pass" if ((10, None) == get_min_max(l)) else "Fail")  # Fail