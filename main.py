def get_book_text(filepath):
    with open(filepath, encoding='utf-8') as bookfile:
        book_contents = bookfile.read()
    return book_contents
    
def main():
    filepath = "./books/frankenstein.txt"
    content = get_book_text(filepath)

if __name__ == '__main__':
    main()
