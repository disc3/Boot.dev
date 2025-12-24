from stats import get_word_count, get_char_count

def get_book_text(filepath):
    with open(filepath, encoding='utf-8') as bookfile:
        book_contents = bookfile.read()
    return book_contents

def main():
    filepath = "./books/frankenstein.txt"
    content = get_book_text(filepath)
    get_word_count(content)
    get_char_count(content)

if __name__ == '__main__':
    main()
