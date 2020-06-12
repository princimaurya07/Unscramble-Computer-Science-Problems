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
my_set=set()

for i in range(len(texts)):
    my_set.add(texts[i][0])
    my_set.add(texts[i][1])
 
for i in range(len(calls)):
    my_set.add(calls[i][0])
    my_set.add(calls[i][1])
       
k=str(len(my_set))    
    
print("There are " + k + " different telephone numbers in the records.")    
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
