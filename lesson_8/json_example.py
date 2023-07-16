import json

# dict -> object {}
# list, tuple -> array []
# str -> string
# int, float -> number
# True, False -> true, false
# None -> null

data = {
    'name': 'John',
    'age': 40,
    'dogs': ['first', 'second'],
    'alive': True,
    'sens': None
}
with open('files/jhon.json', 'w') as writer_json1:
    json.dump(data, writer_json1, indent=4)
    json_str = json.dumps(data)  # перетворення dict на строку
    print(json_str)

# object -> dict
# array -> list
# string -> string
# number -> int, float
# true, false -> True, False
# null -> None

with open('files/jhon.json', 'r') as reader:
    data = json.load(reader)
    print(data)

json_string = '{"name": "Alex", "age": 50}'
data1 = json.loads(json_string)  # перетворення строки на dict
print(data1['name'])
