import requests
import json
import configparser
from utilities.configurations import *
from utilities.resources import *
from payLoad import *

add_book_url = getConfig()['API']['endpoint'] + ApiResources.addBook
del_book_url = getConfig()['API']['endpoint'] + ApiResources.delBook

book_headers = {'Content-Type': 'application/json'}
query = 'select * from Books'
addBook_response = requests.post(add_book_url, json=buildPayLoadFromDB(query), headers=book_headers, )

print(addBook_response.json())
response_json = addBook_response.json()
print(type(addBook_response.json()))

bookId = response_json['ID']

# Delete book

del_book_json = {

    "ID": bookId

}
delBook_response = requests.post(del_book_url, json=del_book_json, headers=book_headers, )

assert delBook_response.status_code == 200

print(delBook_response.json()['msg'])
assert delBook_response.json() == {'msg': 'book is successfully deleted'}


# Authentication
# verify = False - in case of SSL certification errors

# Establish session to not authenticate every get request from api
se = requests.session()
se.auth = ('apadlo', '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')

git_url = 'https://api.github.com/user'
git_response = requests.get(git_url, verify=False, auth=('apadlo', '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'))
print(git_response.status_code)

url2 = 'https://api.github.com/user/repos'

response = se.get(url2)
print(response.status_code)
