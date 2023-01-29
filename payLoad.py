from utilities.configurations import *


# Using local dictionary
def addBookPayload(isbn, aisle):
    body = {

        "name": "Learn Appium Automation with Java",
        "isbn": isbn,
        "aisle": aisle,
        "author": "John Hoe"
    }
    return body


# using database
def buildPayLoadFromDB(query):

    addBody = {}
    tp = getQuery(query)
    addBody['name'] = tp[0]
    addBody['isbn'] = tp[1]
    addBody['aisle'] = tp[2]
    addBody['author'] = tp[3]
    return addBody
