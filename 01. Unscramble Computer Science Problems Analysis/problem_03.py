"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
phone_time_dict = {}

def check_phone(phone_number, time_spent):
    if phone_number in phone_time_dict: 
        phone_time_dict[phone_number] += int(time_spent)
    else:
        phone_time_dict[phone_number] = int(time_spent)

def sort_dictionary(dictionary):
    tmp = []
    for key, value in dictionary.items():
        tmptuple = (value, key)
        tmp.append(tmptuple)
    # sort the list in ascending order
    return sorted(tmp)

for item in calls:
    check_phone(item[0], int(item[-1]))
    check_phone(item[1], int(item[-1]))   

sort_dict = sort_dictionary(phone_time_dict)
print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(sort_dict[-1][1], sort_dict[-1][0]))