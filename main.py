from stats import get_word_count, print_sorted_count

def get_book_text(filepath):
    with open(filepath, encoding='utf-8') as bookfile:
        book_contents = bookfile.read()
    return book_contents

def main():
    filepath = "./books/frankenstein.txt"
    content = get_book_text(filepath)
    print(f"Found {get_word_count(content)} total words")
    print(print_sorted_count(content))

if __name__ == '__main__':
    main()
