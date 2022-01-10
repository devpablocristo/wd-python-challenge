import requests

class Book:

    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def getBookTitle(self):
        return self.name

    def getStockNumber(self):
        return self.stock

def getBookList():
    apiURL = 'https://smth.com/books/'
    response = requests.api(apiURL)
    response.json()

def getBook(name):
    apiURL = 'https://books/'
    response = requests.api(apiURL)
    response.json()

def addBook(name, stock):
    apiURL = 'https://addBook'
    book = {'bookName': name, 'bookStock': stock}
    response = requests.post(apiURL, json= book)
    response.json()

def editBook(name, stock):
    apiURL = 'https://editBook/{name}'
    response = requests.get(apiURL)
    response.json()
    book = {'bookStock': stock}
    response = requests.put(apiURL, json=book)
    response.json()

def deleteBookCopies(name, numberOfCopies):
    apiURL = 'https://editBook/{name}'
    response = requests.get(apiURL)
    response.json()
    book = {'bookStock': {stock} - numberOfCopies}
    response = requests.patch(apiURL, json=book)
    response.json()


def addBook(name, stock):
    apiURL
    requests.get()
    for value in values:
        title = value['title']
        stock = value['stock']
        response = requests.get(apiURL/name)
        if response != Null:
            book = {'bookName': title, 'bookStock': stock}
            response = requests.post(apiURL, json= book)
            response.json()
        else:
