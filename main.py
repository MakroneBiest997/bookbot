from stats import count_words
from stats import count_each_character
from stats import unsorted_dictionary_list
from stats import get_sort_key
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def print_ordered_char_list(dic_list):
    return 0

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    book_dictionary = count_each_character(book_text)
    
    unordered_dic_list = unsorted_dictionary_list(book_dictionary)
    unordered_dic_list.sort(reverse=True, key=get_sort_key)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")  
    print("--------- Character Count -------")
    
    for item in unordered_dic_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    
    print("============= END ===============")

main()

