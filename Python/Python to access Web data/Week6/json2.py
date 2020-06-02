import json

data = '''[
    { "id" : "001",
      "x" : "2",
      "name" : "axat"
    },
    { "id" : "009",
      "x" : "6",
      "name" : "Axat"
    }
]'''

#Here Info is a list bcz we are using '[]' brackets
info = json.loads(data)
print('User Count : ',len(info))
for item in info:
    print('Name : ',item['name'])
    print('Id : ',item['id'])
    print('Attribute : ',item['x'])
