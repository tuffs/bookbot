from stats import get_book_text, get_word_count, get_char_counts, character_count_dictionaries

BOOK_INPUT_FILE_LOCATION = 'books/frankenstein.txt'

def main():
  # get word count for BOOK_INPUT_FILE_LOCATION
  # book_word_count = get_word_count(get_book_text(BOOK_INPUT_FILE_LOCATION))

  # produce character count dictionaries
  character_count_dictionaries(BOOK_INPUT_FILE_LOCATION)

  # setup a printable set of stdout statements to the console
  # print("============ BOOKBOT ============")
  # print(f"Analyzing book found at {BOOK_INPUT_FILE_LOCATION}...")
  # print("----------- Word Count ----------")
  # print(f"Found {book_word_count} total words")
  # print("--------- Character Count -------")
  # print("...rest of output based on dictionary sorting function with character counts...")

main()