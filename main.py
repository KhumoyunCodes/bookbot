from stats import count_symbols, count_words, chars_dict_to_sorted_list
import sys




        
def main():
    # file_path = "books/frankenstein.txt"
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(file_path)
    num_words = count_words(text)
    chars_dict = count_symbols(text)
    sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(file_path, num_words, sorted_list)


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def print_report(file_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item['char'].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("==================END===================")

main()