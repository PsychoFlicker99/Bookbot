
def word_counter(book):
    as_string = book.split()
    counter = 0
    for words in as_string:
        counter += 1
    return print(f'{counter} words found in the document.')

def character_counter(book):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for_counting = []
    count = {}
    in_lower_case = book.lower()
    as_string = in_lower_case.split()
    for word in as_string:
        for letter in word:
            if letter in alphabet:
                for_counting.append(letter)
    for letter in alphabet:
        count[letter] = 0
    for letter in for_counting:
        if letter in count:
            count[letter] += 1
    return count

def sort_assist(dict_pairs):
    return dict_pairs['num']

def sorter(dict):
    list = []
    for pair in dict:
        new_dict = {'char': pair, 'num': dict[pair]}
        list.append(new_dict)
    list.sort(reverse=True, key=sort_assist)
    return print(list)
    


    


 