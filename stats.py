def get_word_count(book_content):
    word_count = len(book_content.split())
    return print(f"Found {word_count} total words")

def get_char_count(book_content):
    char_count = {}
    for char in book_content:
        char = char.lower()
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return print(char_count)