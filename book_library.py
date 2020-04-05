from sys import argv
from book_class import *
import requests
import json
from bs4 import BeautifulSoup

def create_book_instance():
    return book()

def scrap_book(book_to_add):
    url = f'https://www.googleapis.com/books/v1/volumes?q={book_to_add}'
    response = requests.get(url).json()
    resource = response['items'][0]['volumeInfo']
    author = ', '.join(resource['authors'])
    genre = ', '.join(resource['categories'])
    return author, genre

def link_to_class_book(book_instance, name, author, genre):
    book_instance.name = name
    book_instance.author = author
    book_instance.genre = genre

def add_to_html(name, author, genre):
    with open('basic_html.html') as html_file_to_read:
        soup = BeautifulSoup(html_file_to_read, 'html.parser')
        new_div = soup.new_tag('div')
        new_div.string = 'Book: %s\n / Author: %s\n / Genre: %s' % (name, author, genre)
        soup.body.insert(0, new_div)
    with open('basic_html.html', 'w') as html_file_to_write:
        html_file_to_write.write(str(soup))

def nice_printing():
    print('---------------------')
    print('Adding a new book:')
    print('Name: ', book_instance.name)
    print('Author: ', book_instance.author)
    print('Genre: ', book_instance.genre)
    print('---------------------')

if __name__ == '__main__':
    book_instance = create_book_instance()
    link_to_class_book(book_instance, argv[1], *scrap_book(argv[1]))
    nice_printing()
    add_to_html(book_instance.name, book_instance.author, book_instance.genre )