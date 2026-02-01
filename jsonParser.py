import json

courses = '{"name": "RahulShetty", "languages": ["Java", "Python"]}'

# Loads method parse json string and it returns dictionary
dict_courses = json.loads(courses)


# Load method parse content present in Json file
with open('D:\\Python\\Python for Everybody\\roster_data.json') as f:
    data = json.load(f)
    print(type(data))


# Compare 2 json files

with open('D:\\Python\\Python for Everybody\\roster_data2.json') as f2:
    data2 = json.load(f2)

    assert data == data2


