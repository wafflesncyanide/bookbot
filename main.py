from stats import get_word_count
from stats import get_character_counts
from stats import sort_on
from stats import listify
import sys

def  get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    print(file_contents)


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(F"Analyzing book found at {file_path}")
    word_count = get_word_count(file_path)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    char_counts = get_character_counts(file_path)
    #print(char_counts)
    list_counts=listify(char_counts)
    #print(list_counts)
    list_counts.sort(key=sort_on, reverse=True)
    #print(list_counts)
    print("------- Character Count -------")
    for dict in list_counts:
        if dict["name"].isalpha():
            print(f"{dict["name"]}: {dict["num"]}")


main()