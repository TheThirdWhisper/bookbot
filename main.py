from stats import word_count
from stats import character_count
from stats import sort_on
from stats import character_count_sort
def get_book_text(path_to_file):
    # This function will take a .txt file "path_to_file" and return the contents of that file as a string
    file_contents = "" #initializing file_contents as an empty string
    with open(path_to_file) as f: #using the With command to open the file and setting the contents to f
        file_contents = f.read() #using the read command to assign the f variables contents to "file_content" as a string
    return file_contents
def main():
    frankenstein = get_book_text("./books/frankenstein.txt")
    w_count = word_count(frankenstein)
    c_count = character_count(frankenstein)
    c_sorted = character_count_sort(c_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {w_count} total words")
    print("--------- Character Count -------")
    for key, value in c_sorted.items():
        if key.isalpha() is True:
            print(f"{key}: {value}")
main()