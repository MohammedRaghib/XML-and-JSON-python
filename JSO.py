import json

data = {
    'Contact': {
        'Name': 'Stefan',
        'Email': 'Stef@gmail.com'
    }
}
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

with open('data.json', 'r') as file:
    doc = json.load(file)
    print(doc['Contact']['Email'], doc['Contact']['Name'])