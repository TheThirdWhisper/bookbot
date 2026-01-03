from stats import word_count
from stats import character_count
from stats import sort_on
from stats import character_count_sort
import sys
def get_book_text(path_to_file):
    # This function will take a .txt file "path_to_file" and return the contents of that file as a string
    file_contents = "" #initializing file_contents as an empty string
    with open(path_to_file) as f: #using the With command to open the file and setting the contents to f
        file_contents = f.read() #using the read command to assign the f variables contents to "file_content" as a string
    return file_contents
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = get_book_text(sys.argv[1])
        w_count = word_count(book)
        c_count = character_count(book)
        c_sorted = character_count_sort(c_count)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {w_count} total words")
        print("--------- Character Count -------")
        for key, value in c_sorted.items():
            if key.isalpha() is True:
                print(f"{key}: {value}")
main()