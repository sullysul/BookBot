from stats import get_num_words, get_char_counts


def get_book_text(filepath):
    """Reads the contents of a file and returns it as a string."""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    # Call get_book_text with the relative path to frankenstein.txt
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    char_counts = get_char_counts(text)
    print(char_counts)


# Execute the program
if __name__ == "__main__":
    main()

    
