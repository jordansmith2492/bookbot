def word_count(book_text):
    words = book_text.split()
    return len(words)

def char_count(book_text):
    char_dict = {}
    for char in book_text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return(char_dict)

def get_sorted_char_list(char_dict):
    def sort_on(dict):
        return dict["num"]

    sorted_list = []

    for char, count in char_dict.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list