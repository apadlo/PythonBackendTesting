import os

from behave import *
import requests
from utilities.configurations import *
from utilities.resources import *
from payLoad import *


@given('the Book details which need to be added to Library')
def step_impl(context):
    context.add_book_url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.book_headers = {'Content-Type': 'application/json'}
    context.payLoad = addBookPayload("mark123", "187");


@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.add_book_url, json=context.payLoad, headers=context.book_headers, )


@then('book is successfully added')
def step_impl(context):
    print(context.response.json())
    response_json = context.response.json()
    context.bookId = response_json['ID']
    print(context.bookId)
    assert 'successfully added' in response_json["Msg"]


@given('the Book details with {isbn} and {aisle} need to be added to Library')
def step_impl(context, isbn, aisle):
    context.add_book_url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.book_headers = {'Content-Type': 'application/json'}
    context.payLoad = addBookPayload(isbn, aisle);


@given('I have github auth credentials')
def step_impl(context):
    username = os.getenv("GITHUB_USERNAME", "")
    token = os.getenv("GITHUB_TOKEN", "")
    if not username or not token:
        raise RuntimeError("Set GITHUB_USERNAME and GITHUB_TOKEN for GitHub API scenario")

    context.se = requests.session()
    context.se.auth = (username, token)




@when('I hit getRepo API of github')
def step_impl(context):
    context.response = context.se.get(ApiResources.githubRepo)


@then('status code of response should be {statusCode:d}')
def step_impl(context, statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode

