import requests
import json

get_book_url = 'http://216.10.245.166/Library/GetBook.php'

response = requests.get(get_book_url, params={'AuthorName':'Rahul Shetty'},)

json_response = response.json()

print(type(json_response))
print(len(json_response))

assert response.status_code == 200

print(response.headers)
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'

# Retrieve book details with ISBN RGHCC

for book in json_response:
    if book['isbn'] == 'RGHCC':
        actual_book = book
        break

expected_book = {'book_name': 'Learn with Java', 'isbn': 'RGHCC', 'aisle': '222'}

assert actual_book == expected_book
