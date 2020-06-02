#Practice program for JSON
import json
data = '''{
    "name" : "Axat",
    "phone" : {
        "type" : "init",
        "number" : "+91 8493928928"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

#Here info is a dictionary because we used '{}' brackets
info = json.loads(data)

# in dictionary we are fetching value by accessing it's key
print('Name : ',info["name"])
print('Phone : ',info["phone"]["number"])
print('Hide : ',info["email"]["hide"])
