'''
Following Links in Python
In this assignment you will write a Python program that expands on http://www.pythonlearn.com/code/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.
We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment
Sample problem: Start at http://python-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah
Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Mikella.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: L
'''
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
from urllib import parse

#ignore ssl certification error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -- ')

count = int(input('Enter Count : '))
pos = int(input('Enter Position : '))

p = 0
s = []
t = []
for i in range(count-1):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    #Retrive all anchor tag
    for tag in tags:
        p += 1
        if p == pos:
            x = tag.get('href', None)
            s.append(x)
            y = tag.text
            t.append(y)
            p = 0
            print(s)
            print(t)
            break
# print(s[pos-1])
# print(t[pos-1])
# url = s[pos-1]


# lst0 = []
# lst1 = []
#
# #Retrive all the anchor tag
# tags = soup('a')
# for tag in tags:
#     x = tag.get('href',None)
#     lst0.append(x)
#     y = tag.text
#     lst1.append(y)
#
# print(lst0[pos-1])
# print(lst1[pos-1])
