'''
In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
Sample data: http://python-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_598301.xml (Sum ends with 1)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
'''
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
from urllib import parse
import xml.etree.ElementTree as ET

#ignore ssl certification error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -- ')
html = urllib.request.urlopen(url, context=ctx)

# print(html)
data = html.read()

# print('Retrieved', len(data), 'characters')
# print(data.decode())

tree = ET.fromstring(data)

counts = tree.findall('comments/comment')
print(counts)
total = 0
i = 0
for count in counts:
    x = int(count.find('count').text)
    # print(x)
    i += 1
    total += x

print(i)
print(total)
