# Assignment 3:

import xml.etree.ElementTree as ET
data = '''
<Contact>
    <Name>Caroline</Name>
    <Email required='yes'>Caro1@gmail.com</Email>
</Contact>
'''

xm = ET.fromstring(data)

with open('Test.xml', 'w') as file:
    file.write(data)

doc = ET.parse('Test.xml')

print('Name: ', doc.find('Name').text)
print('Email required? ', doc.find('Email').get('required'))
print('Email: ', doc.find('Email').text)