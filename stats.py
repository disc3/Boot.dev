def get_word_count(book_content):
    word_count = len(book_content.split())
    return word_count

def sort_on(dictionary):
    return dictionary["num"]

def sort_by_count(char_count):
    sorted_char_count = []
    for key, val in char_count.items():
        entry = {"char": key, "num": val}
        sorted_char_count.append(entry)
    sorted_char_count.sort(reverse=True, key=sort_on)
    return sorted_char_count

def print_sorted_count(book_content):
    sorted_count = sort_by_count(char_count=get_char_count(book_content))
    for item in sorted_count:
        print(f"{item["char"]}: {item["num"]}")
    pass
        

def get_char_count(book_content):
    char_count = {}
    for char in book_content:
        char = char.lower()
        if not char.isalpha():
            continue
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

