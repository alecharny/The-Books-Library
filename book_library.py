from sys import argv
from book_class import *
import requests
import json
from bs4 import BeautifulSoup

# Helper functions

def create_book_instance():
    return book()

def scrap_book(book_to_add):
    url = f'https://www.googleapis.com/books/v1/volumes?q={book_to_add}'
    response = requests.get(url).json()
    # with open('json_output.json', 'w') as json_file:
    #     json.dump(response, json_file, indent = 4, ensure_ascii = False)
    resource = response['items'][0]['volumeInfo']
    try: 
        author = ', '.join(resource['authors'])
        genre = ', '.join(resource['categories'])
        book_summary = resource['description']
    except:
        author = 'Not Found'
        genre = 'Not Found'
        book_summary = 'Not Found'
    return author, genre, book_summary

def link_to_class_book(book_instance, name, author, genre, description):
    book_instance.name = name
    book_instance.author = author
    book_instance.genre = genre
    book_instance.description = description

def add_to_html(name, author, genre, description):
    global indice 
    global list_descriptors
    indice = 0
    list_descriptors = ['Book Summary: ', 'Genre: ', 'Author(s): ', 'Name: ']
    with open('book_library.html') as html_file_to_read:
        soup = BeautifulSoup(html_file_to_read, 'html.parser')
        add_nice_html_section(soup)
        for element in [description, genre, author, name]:
            add_html_element(soup, element)
            add_html_break_line(soup)
            indice += 1
    with open('book_library.html', 'w') as html_file_to_write:
        html_file_to_write.write(str(soup))

# Printing + HTML sections

def nice_printing():
    print('---------------------')
    print('Adding a new book:')
    print('Name: ', book_instance.name)
    print('Author: ', book_instance.author)
    print('Genre: ', book_instance.genre)
    print('Book Summary: ', book_instance.description)
    print('---------------------')

def add_nice_html_section(soup):
    new_book_div = soup.new_tag('p')
    new_book_div.string = '-------------------'
    soup.body.insert(0, new_book_div) 

def add_html_break_line(soup):
    new_break = soup.new_tag('br')
    soup.body.insert(0, new_break)

def add_html_element(soup, element):
    new_book_div = soup.new_tag('div')
    new_book_div.string = list_descriptors[indice] + '%s' % element
    soup.body.insert(0, new_book_div) 

# Main

if __name__ == '__main__':
    book_instance = create_book_instance()
    link_to_class_book(book_instance, argv[1], *scrap_book(argv[1]))
    nice_printing()
    add_to_html(book_instance.name, book_instance.author, book_instance.genre, book_instance.description)
