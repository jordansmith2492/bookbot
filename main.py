import sys
from stats import word_count, char_count, get_sorted_char_list

# get_book_text function for reading the book text from a file
# This function takes a filename as input
# and reads the contents of the file
# It returns the contents of the file as a string
def get_book_text(filename):
    with open(filename) as f:
        file_contents = f.read()
    return file_contents

# main function for the script
# This function checks if the correct number of command line arguments are provided
# It takes the filename as input from the command line arguments
# It calls the get_book_text function to read the book text from the file
# It then calls the word_count, char_count, and get_sorted_char_list functions
# to analyze the book text
# It prints the results of the analysis to the console
# It also handles any errors that may occur during the execution of the script
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        book_text = get_book_text(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    words = word_count(book_text)
    char_dict = char_count(book_text)
    sorted_list = get_sorted_char_list(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filename}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")



main()