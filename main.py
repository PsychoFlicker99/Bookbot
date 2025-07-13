import sys
from stats import word_counter
from stats import character_counter
from stats import sorter


def get_book_text(file_path):
    with open(file_path) as f:
        text = f.read()
        return text 

def main():
    return get_book_text('./books/frankenstein.txt')


sorter(character_counter(main()))

def just_nums(sorted_list):
    for dict in sorted_list:
        print (f'{dict['char']}: {dict['num']}')

print('============ BOOKBOT ============')
print(f'Analyzing book found at ./books/frankenstein.txt')
print('----------- Word Count ----------')
word_counter(main())  
print('--------- Character Count -------')
just_nums(sorter(character_counter(main())))
print('============= END ===============')

