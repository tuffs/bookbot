# BookBot

A Python CLI program for analyzing book word count and character counts.

## Features

- Count total words in a text file
- Count total characters (including whitespace)
- Count characters excluding whitespace  
- Count unique alphabetic characters
- Display character frequency analysis (sorted by frequency)
- Command-line interface with helpful error messages

## Usage

```bash
python main.py <book_file>
```

### Examples

```bash
# Analyze a book file
python main.py frankenstein_sample.txt

# Show help
python main.py --help

# Show version
python main.py --version
```

### Sample Output

```
--- Begin report of frankenstein_sample.txt ---
599 words found in the document

Character frequency (alphabetic characters only):
The 'e' character was found 375 times
The 't' character was found 260 times
The 'a' character was found 210 times
...

--- Summary ---
Total characters: 3489
Characters (excluding whitespace): 2884
Unique alphabetic characters: 26
--- End report ---
```

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

## Files

- `main.py` - Main CLI program
- `frankenstein_sample.txt` - Sample text file for testing
- `.gitignore` - Git ignore file for Python projects