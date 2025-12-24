def get_book_text(filepath):
    with open(filepath, encoding='utf-8') as bookfile:
        book_contents = bookfile.read()
    return book_contents

def get_word_count(book_content):
    word_count = len(book_content.split())
    return print(f"Found {word_count} total words")
    
def main():
    filepath = "./books/frankenstein.txt"
    content = get_book_text(filepath)
    get_word_count(content)

if __name__ == '__main__':
    main()
