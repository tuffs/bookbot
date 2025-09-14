from stats import get_args, get_book_text, get_word_count, get_char_counts, character_count_dictionaries

def main():
    path_to_file = get_args()
    book_word_count = get_word_count(get_book_text(path_to_file))  # Fixed: 4 spaces
    sorted_list_of_dicts = character_count_dictionaries(path_to_file)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print("--------- Character Count -------")
    for dicts in sorted_list_of_dicts:
        char = dicts['char']
        num = dicts['num']
        print(f"{char}: {num}")
    print("============= END ===============")
main()