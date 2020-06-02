
import random
import os
import string
import time

books_folders = './en/'
cpositions = list()
books = list()

languge = input("Enter the language (En or Fa) >> ")
languge = languge.lower()

if languge == "en":
    books_folders = './en/'
elif languge == "fa":
    books_folders = './fa/'
else:
    raise Exception(f"Not Support '{languge}' Languge")


def find_books():
    files = os.listdir(books_folders)
    for file_name in files:
        books.append(books_folders+file_name)


def read_books():
    for book in books:
        read_book(book)


def get_compostion(words):
    cpositions = []
    for index in range(len(words)-1):
        cpositions.append([words[index], words[index+1]])
    return cpositions


def read_book(name):
    book = open(name)

    for line in book:
        line = line.lower().strip()
        line = line.replace(string.punctuation, " ")
        line = line.replace(",", " ")
        line = line.replace("*", " ")

        words = line.split()
        cpositions.extend(get_compostion(words))


def make_sentence(first=[]):
    if len(first) == 0:
        first = [random.choice(cpositions)[0]]
    last_word = first[len(first)-1]

    new_words = list()

    for i in range(len(cpositions)):
        if last_word == cpositions[i][0]:
            new_words.append(cpositions[i][1])

    if len(new_words) > 0:
        first.append(random.choice(new_words))
        return make_sentence(first)
    else:
        return " ".join(first)


def talk():
    find_books()
    read_books()

    print(f"""

Liona Say :

{make_sentence()}

    """)


print("Start Finding Books ...")
find_books()
print("Finding books was a success")


print("Start Reading Books ...")
read_books()
print("Reading books was a success")


print("Start Thinking ...")
talk()


print("Goodbye , See You later")
print("Liona 1.0.0")
