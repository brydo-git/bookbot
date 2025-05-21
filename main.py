import sys
from stats import (
    word_count, 
    converter, 
    sorted_dict
)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    path = sys.argv[1]

    num_words = word_count(book_text)
    char_counts = converter(book_text)
    ch_sorted_list = sorted_dict(char_counts)
    print_report(path, num_words, ch_sorted_list)
    

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def print_report(path, num_words, ch_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in ch_sorted_list:
        if not i ["char"].isalpha():
            continue
        else:
            print(f"{i['char']}: {i['num']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
 
