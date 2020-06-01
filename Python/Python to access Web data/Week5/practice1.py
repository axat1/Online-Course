import xml.etree.ElementTree as ET
data = '''
<person>
    <name>Akshat</name>
    <phone type="intl">
        +91 8976937837
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name : ',tree.find('name').text)
print('Email : ',tree.find('email').get('hide'))
