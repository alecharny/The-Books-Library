from sys import argv
from book_class import *
import requests
from bs4 import BeautifulSoup

def add_book(book_to_add):
    new_book_instance = book()
    new_book_instance.name = book_to_add
    return new_book_instance

def scrap_book(book_to_add):
    pass
    
if __name__ == "__main__":
    book_terminal = argv[1]
    new_book = add_book(book_terminal)
    print(new_book)
    scrap_book(new_book.name)
