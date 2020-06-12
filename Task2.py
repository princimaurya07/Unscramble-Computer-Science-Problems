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
dic=dict()    
for row in calls:
    if row[0] not in dic.keys(): 
        dic[row[0]]=int(row[3])
    else:
        dic[row[0]]+=int(row[3])    
    if row[1] not in dic.keys():     
        dic[row[1]]=int(row[3])
    else:
        dic[row[1]]+=int(row[3])   
        
res=max(dic.values())
res2=""
for e in dic.keys():
    if(dic[e]==res):
        res2=e
        break
   
print(res2+" spent the longest time, " + str(res) + " seconds, on the phone during" )
            
    

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

