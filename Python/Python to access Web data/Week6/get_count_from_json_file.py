'''
In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_598302.json (Sum ends with 12)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
'''

import urllib.request, urllib.parse, urllib.error
import json

address = input('Enter url Address')
print('Retrivig url : ',address)


j_file = urllib.request.urlopen(address)
data = j_file.read().decode()
print('Retrived', len(data),'Characters')

try:
    js = json.loads(str(data))
except:
    js = None

sum = 0
count = 0
# print(js)
for item in js['comments']:
    count += 1
    sum += item['count']
    # print("Count : ",item['count'])

print('Count : ', count)
print('Sum : ', sum)
