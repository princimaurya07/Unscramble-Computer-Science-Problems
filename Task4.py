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
s=set()
res=set()
for row in texts:
    s.add(row[0])
    s.add(row[1])
for row in calls:
    res.add(row[0])
    s.add(row[1]) 
l1=list(res)
l2=list(s)    
for i in l2:
    for e in l1:
        if(e==i):
            l1.remove(e)
            break
            
    
l1.sort() 
          
print("These numbers could be telemarketers: ")      
for ele in l1:
    print(ele)
  
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

