import urllib.request, urllib.parse, urllib.error
import ssl
import json
# http://py4e-data.dr-chuck.net/json?

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

#i had this issue that url was not taking key value with it so
#i have to concate it at the end of the url
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'+'key=42&'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


while True:
    address = input('Enter Location : ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retriving : ', url)
    data = urllib.request.urlopen(url).read()
    # data = uh.read().decode()
    print('Retrived', len(data),'Characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != "OK":
        print('===== Failure To Retrive =====')
        print(data)
        continue

    # print(json.dumps(js, indent = 4))

    # lat = js["results"][0]["geometry"]["location"]["lat"]
    # lng = js["results"][0]["geometry"]["location"]["lng"]
    # print('lat : ',lnt,' lng : ',lng)
    location = js["results"][0]["place_id"]
    print(location)
