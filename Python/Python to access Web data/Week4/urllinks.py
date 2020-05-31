import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
from urllib import parse

#ignore ssl certification error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -- ')
html = urllib.request.urlopen(url, context=ctx).read()
#
# #function added to update error
# def is_absolute(url):
#     return bool(parse.urlparse(url).netloc)
#
# href = html.get('href')
# if not is_absolute(href):
#     href = WEBSITE + href
#
# html = is_absolute(html)
# #
# print(html)
soup = BeautifulSoup(html, 'html.parser')

#Retrive all the anchor tag
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))
