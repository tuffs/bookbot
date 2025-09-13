#!/usr/bin/env python3
"""
BookBot - A Python CLI program for analyzing book word count and character counts.
"""

import argparse
import sys
import os
from collections import Counter


def read_book(file_path):
    """
    Read the contents of a book file.
    
    Args:
        file_path (str): Path to the book file
        
    Returns:
        str: Contents of the file
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        IOError: If there's an error reading the file
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Book file not found: {file_path}")
    except IOError as e:
        raise IOError(f"Error reading file {file_path}: {e}")


def count_words(text):
    """
    Count the total number of words in the text.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        int: Number of words
    """
    # Split on whitespace and filter out empty strings
    words = [word for word in text.split() if word.strip()]
    return len(words)


def count_characters(text):
    """
    Count different types of characters in the text.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        dict: Dictionary containing different character counts
    """
    # Convert to lowercase for character frequency analysis
    text_lower = text.lower()
    
    # Count total characters
    total_chars = len(text)
    
    # Count characters excluding whitespace
    non_whitespace_chars = len([c for c in text if not c.isspace()])
    
    # Count unique characters (case-insensitive, alphabetic only)
    alphabetic_chars = [c for c in text_lower if c.isalpha()]
    char_frequency = Counter(alphabetic_chars)
    unique_chars = len(char_frequency)
    
    return {
        'total': total_chars,
        'non_whitespace': non_whitespace_chars,
        'unique_alphabetic': unique_chars,
        'frequency': char_frequency
    }


def display_results(file_path, word_count, char_counts):
    """
    Display the analysis results in a formatted way.
    
    Args:
        file_path (str): Path to the analyzed file
        word_count (int): Total word count
        char_counts (dict): Character count information
    """
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    print()
    
    print("Character frequency (alphabetic characters only):")
    # Sort characters by frequency (descending) then alphabetically
    sorted_chars = sorted(char_counts['frequency'].items(), 
                         key=lambda x: (-x[1], x[0]))
    
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")
    
    print()
    print("--- Summary ---")
    print(f"Total characters: {char_counts['total']}")
    print(f"Characters (excluding whitespace): {char_counts['non_whitespace']}")
    print(f"Unique alphabetic characters: {char_counts['unique_alphabetic']}")
    print("--- End report ---")


def main():
    """Main function to run the CLI program."""
    parser = argparse.ArgumentParser(
        description="Analyze word count and character counts in a book file",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py book.txt
  python main.py /path/to/novel.txt
        """
    )
    
    parser.add_argument(
        'file',
        help='Path to the book file to analyze'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='BookBot 1.0.0'
    )
    
    args = parser.parse_args()
    
    # Check if file exists
    if not os.path.exists(args.file):
        print(f"Error: File '{args.file}' not found.", file=sys.stderr)
        sys.exit(1)
    
    try:
        # Read the book
        text = read_book(args.file)
        
        # Analyze the text
        word_count = count_words(text)
        char_counts = count_characters(text)
        
        # Display results
        display_results(args.file, word_count, char_counts)
        
    except (FileNotFoundError, IOError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()