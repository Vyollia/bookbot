def main():
    path_to_book = "books/frankenstein.txt"
    book = read_book(path_to_book)
    lower = lower_case(book)
    letters = character_count(lower)
    letter_list = convert_dict(letters)
    letter_list.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(word_count(book), "words found in the document")
    for items in letter_list:
        print(f"The '{items['letter']}' character was found {items['num']} times")
    print("--- End report ---")

def read_book(path_to_book):
    with open(path_to_book) as f: 
        return f.read()

def word_count(book):
    return len(book.split())
    
def lower_case(book):
    return book.lower()

def character_count(lower):
    letters = {} 
    for letter in lower:
        if letter.isalpha():
            if letter in letters:
                letters[letter] += 1
            else: 
                letters[letter] = 1
    return letters

def convert_dict(letters):
    letter_list = [{"letter": k, "num": v} for k, v in letters.items()]
    return letter_list

def sort_on(letter_list):
        return letter_list["num"]

main()