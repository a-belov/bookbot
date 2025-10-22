import sys
import stats

def main():
    book_path = get_book_path(sys.argv)
    book_text = get_book_text(book_path)
    number_of_words = stats.get_num_words(book_text)
    characters_dict = stats.get_characters_count(book_text)
    sorted_characters_dict = stats.dictionary_sort(characters_dict)

    print_report(number_of_words, sorted_characters_dict, book_path)


def get_book_path(arguments):
    if len(arguments) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        return arguments[1]


def get_book_text(fpath) -> str:
    with open(fpath, 'r', encoding='utf8') as f:
        file_contents = f.read()
    return file_contents


def print_report(number_of_words, sorted_characters_dict, book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for c in sorted_characters_dict:
        if c["name"].isalpha():
            print(f"{c["name"]}: {c["num"]}")
    print("============= END ===============")


if __name__ == '__main__':
    main()
