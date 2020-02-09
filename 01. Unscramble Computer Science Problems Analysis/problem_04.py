"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader) 

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def get_phone_prefix(phone_number):
    """
    return the prefix of a phone number.
    :param phone_number: int.telephone number
    :return: num_prefix
    """
    num_prefix = None
    if phone_number[0] == '(':
        num_prefix = phone_number[1:phone_number.index(')')]
    elif phone_number[0] in ('7', '8', '9') or phone_number[0:3] == '140':
        num_prefix = phone_number[0:4]
    return num_prefix

phone_code_set = set()
bangalore_phone_count = 0
total_phone_count = 0
for item in calls:
    if item[0][0:5] == '(080)':
        total_phone_count += 1
        if get_phone_prefix(item[1]):
            phone_code_set.add(get_phone_prefix(item[1]))
            if get_phone_prefix(item[1]) == '080':
                bangalore_phone_count += 1
                
percent_calls = round((bangalore_phone_count/total_phone_count*100), 2)

print('The numbers called by people in Bangalore have codes:\n{}'.format('\n'.join(sorted(phone_code_set))))
print('{}% percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(percent_calls))