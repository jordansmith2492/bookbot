# word_count function
# This function takes a string as input and returns the number of words in the string
# It splits the string into words using whitespace as the delimiter
# and counts the number of words
# It also removes any leading or trailing whitespace from the string
def word_count(book_text):
    words = book_text.split()
    return len(words)

# char_count function for counting the number of characters in a book
# This function counts the number of occurrences of each character in the book text
# and returns a dictionary with the character as the key and the count as the value
# It also converts all characters to lowercase to ensure case insensitivity
# It ignores non-alphabetic characters and only counts alphabetic characters
def char_count(book_text):
    char_dict = {}
    for char in book_text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return(char_dict)

# get_sorted_char_list function for sorting the character count dictionary
# This function takes a dictionary of character counts as input
# and returns a sorted list of dictionaries with the character and its count
# The list is sorted in descending order based on the count of each character
# It ignores non-alphabetic characters and only includes alphabetic characters in the sorted list
def get_sorted_char_list(char_dict):
    def sort_on(dict):
        return dict["num"]

    sorted_list = []

    for char, count in char_dict.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list