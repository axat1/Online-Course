import urllib.request, urllib.parse, urllib.error
import json
# http://py4e-data.dr-chuck.net/json?
servicecourl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter Location : ')
    if len(address) < 1: break

    url = servicecourl + urllib.parse.urlencode({'address': address})

    print('Retriving : ', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrived', len(data),'Characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != "OK":
        print('===== Failure To Retrive =====')
        print(data)
        continue

    print(json.dumps(js, indent = 4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat : ',lnt,' lng : ',lng)
    location = js['results'][0]['formatted_address']
    print(location)
