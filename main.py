import sys
from stats import count_words, character_count, book_report

def get_book_text(filepath):
    with open(filepath) as f:
        read_data = f.read()
    return read_data
    
def main():
    file_path = sys.argv[1]
    book = get_book_text(file_path)
    char_count = character_count(book)
    sorted_list = book_report(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book)} total words")
    print("--------- Character Count -------")

    for i in sorted_list:
        for k in i:
            if k.isalpha():
                print(f"{k}: {i[k]}")

    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()