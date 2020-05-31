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

import urllib
from bs4 import BeautifulSoup

# address = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html'
# address = 'http://py4e-data.dr-chuck.net/known_by_Mikella.html'
address = input('Enter Link : ')

# Number of repeated processes
n = 0
count = int(input('Enter Count : '))
position = int(input('Enter Position : '))
# Position counter
x = 0

## address1 (AKA sample problem)
# while n < count:
#
#     html = urllib.urlopen(address).read()
#     soup = BeautifulSoup(html)
#     tags = soup('a')
#
#     for link in tags:
#         x = x + 1
#         if x == pos:
#             address = link.get('href', None)
#             print address
#             x = 0
#             break
#     n = n + 1

## address2 (AKA actual problem)
s = list()
t = list()
while n < count:
    html = urllib.request.urlopen(address).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for link in tags:
        x = x + 1
        if x == position:
            address = link.get('href', None)
            print(address)
            x = 0
            break
    n = n + 1
