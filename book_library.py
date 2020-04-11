from sys import argv
from book_class import *
import requests
import json
from bs4 import BeautifulSoup
from collections import OrderedDict

# Class Helper functions

def create_book_instance():
    return book()

def link_to_class_book(book_instance, name, author, genre, description, image):
    book_instance.name = name
    book_instance.author = author
    book_instance.genre = genre
    book_instance.description = description
    book_instance.image = image

# Main API and HTML Functions

def scrap_book(book_to_add):
    name = book_to_add
    url = f'https://www.googleapis.com/books/v1/volumes?q={book_to_add}'
    response = requests.get(url).json()
    # Add the two following lines to print the JSON output of the API call in a separate JSON file:
    # with open('json_output.json', 'w') as json_file:
    #     json.dump(response, json_file, indent = 4, ensure_ascii = False)
    resource = response['items'][0]['volumeInfo']
    try: 
        author = ', '.join(resource['authors'])
    except:
        author = 'Not Found'
    try:
        genre = ', '.join(resource['categories'])
    except:
        genre = 'Not Found'
    try:
        description = resource['description']
    except:
        description = 'Not Found'
    try:
        image = resource['imageLinks']['thumbnail']
    except:
        pass
    return name, author, genre, description, image

def generate_list_descriptors(book_instance):
    book_attributes_raw = OrderedDict(book_instance.__dict__)
    book_attributes = OrderedDict()
    for key in book_attributes_raw:
        new_key = key.capitalize() +': '
        book_attributes[new_key] = book_attributes_raw[key]
    list_descriptors = OrderedDict()
    for attribute in reversed(book_attributes):
        list_descriptors[attribute] = book_attributes[attribute]
    return list_descriptors

def add_to_html(book_instance):
    list_descriptors = generate_list_descriptors(book_instance)
    with open('book_library.html') as html_file_to_read:
        soup = BeautifulSoup(html_file_to_read, 'html.parser')
        update_html_counter(soup)
        add_html_section(soup)
        for key, value in list_descriptors.items():
            if key == 'Image: ':
                add_html_image(soup, value)
                add_html_break_line(soup)
            else: 
                line = key + value
                add_html_element(soup, line)
                add_html_break_line(soup)
    with open('book_library.html', 'w') as html_file_to_write:
        html_file_to_write.write(str(soup))

# Printing + HTML sections Function

def nice_printing():
    print('---------------------')
    print('Adding a new book:')
    print('Name: ', book_instance.name)
    print('Author(s): ', book_instance.author)
    print('Genre: ', book_instance.genre)
    print('Description: ', book_instance.description)
    print('---------------------')

def add_html_section(soup):
    new_book_div = soup.new_tag('p')
    new_book_div.string = '-------------------'
    soup.body.insert(0, new_book_div) 

def add_html_break_line(soup):
    new_break = soup.new_tag('br')
    soup.body.insert(0, new_break)

def add_html_element(soup, element):
    new_book_div = soup.new_tag('div')
    new_book_div.string = element
    soup.body.insert(0, new_book_div) 

def add_html_image(soup, image_url):
    new_book_image = soup.new_tag('img', src = image_url)
    soup.body.insert(0, new_book_image)

def update_html_counter(soup):
    counter = soup.find(id = 'number_of_books_read')
    new_counter = int(counter.text) + 1
    new_book_counter = soup.new_tag('span', id="number_of_books_read")
    new_book_counter.string = str(new_counter)
    soup.h3.span.replace_with(new_book_counter)

# Main

if __name__ == '__main__':
    book_instance = create_book_instance()
    link_to_class_book(book_instance, *scrap_book(argv[1]))
    nice_printing()
    add_to_html(book_instance)