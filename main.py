from stats import word_counter
from stats import character_counter
from stats import sorter


def get_book_text(file_path):
    with open(file_path) as f:
        text = f.read()
        return text

def main():
    return get_book_text('./books/frankenstein.txt')



word_counter(main())  

character_counter(main())

sorter(character_counter(main()))




