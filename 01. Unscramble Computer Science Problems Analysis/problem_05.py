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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

send_sms_phones = set()
incoming_sms_phones = set()
send_call_phones = set()
incoming_call_phones = set()

for sms_item in texts:
    send_sms_phones.add(sms_item[0])
    incoming_sms_phones.add(sms_item[1])
    
for call_item in calls:
    send_call_phones.add(call_item[0])
    incoming_call_phones.add(call_item[1])
    
res = send_call_phones.difference(send_sms_phones, incoming_sms_phones, incoming_call_phones)
print('These numbers could be telemarketers: \n{}'.format('\n'.join(sorted(res))))