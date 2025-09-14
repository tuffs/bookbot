def get_book_text(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()
    return file_contents

def get_word_count(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

def get_char_counts(book_file):
    with open(book_file, 'r') as f:
      my_book = f.read()
      char_list = list(my_book.lower())
      char_count = {}

      for char in char_list:
          if char in char_count:
            char_count[char] += 1
          else:
            char_count[char] = 1

    return char_count

def sort_on(items):
    return items["num"]

def character_count_dictionaries(book_file):
    character_counts = get_char_counts(book_file)

    list_of_dicts = []
    for key, value in character_counts.items():
        new_dict = {"char": key, "num": value}
        list_of_dicts.append(new_dict)

    # sorted_list_of_dicts = sorted(list_of_dicts, key=lambda x: x["num"], reverse=True)
    sorted_list_of_dicts = sorted(list_of_dicts, key=lambda n: n["num"], reverse=True)
    sorted_list_of_dicts = [d for d in sorted_list_of_dicts if d["char"].isalpha()]

    # output results
    print(sorted_list_of_dicts)
    return sorted_list_of_dicts
